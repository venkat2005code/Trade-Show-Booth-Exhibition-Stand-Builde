"""Tiny isometric SVG engine used to author the Standform illustration set."""
import math, random
from xml.sax.saxutils import escape

C30 = math.cos(math.radians(30))
K = 0.5
EX, EY = 1.2247, 0.7071  # ground-circle -> iso ellipse radii factors


def h2r(h):
    h = h.lstrip('#')
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def r2h(c):
    return '#%02x%02x%02x' % tuple(max(0, min(255, int(round(v)))) for v in c)


def shade(h, t):
    r = h2r(h)
    if t >= 0:
        return r2h([v + (255 - v) * t for v in r])
    return r2h([v * (1 + t) for v in r])


def mix(a, b, t):
    A, B = h2r(a), h2r(b)
    return r2h([x + (y - x) * t for x, y in zip(A, B)])


class Scene:
    def __init__(self, w=800, h=600, W=30, D=30, H=12, fit=.8, cy=.56, zoom=1.0, focus=None, seed=1):
        self.w, self.h, self.W, self.D, self.H = w, h, W, D, H
        s = min(fit * w / ((W + D) * C30), .8 * h / ((W + D) * K + H)) * zoom
        self.s = s
        self.ox = w / 2 - (W - D) / 2 * C30 * s
        self.oy = h * cy - (-H + (W + D) / 2) * s / 2
        if focus:
            fx, fy = self.P(*focus)
            self.ox += w / 2 - fx
            self.oy += h * .55 - fy
        self.defs = []
        self.items = []
        self.ov = []
        self.bg = ''
        self.n = 0
        self.rnd = random.Random(seed)

    # ---- projection ----
    def P(self, x, y, z=0):
        return (self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * K * self.s - z * self.s)

    def _pts(self, pts):
        return ' '.join('%.1f,%.1f' % p for p in pts)

    def _poly(self, pts, fill, stroke=None, sw=.6):
        if fill.startswith('url'):
            st = 'none'
        else:
            st = stroke or fill
        return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (self._pts(pts), fill, st, sw)

    def lin(self, stops, x1=0, y1=0, x2=0, y2=1):
        self.n += 1
        gid = 'g%d' % self.n
        st = ''.join('<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % (s[0], s[1], s[2] if len(s) > 2 else 1) for s in stops)
        self.defs.append('<linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient>' % (gid, x1, y1, x2, y2, st))
        return gid

    def rad(self, stops):
        self.n += 1
        gid = 'r%d' % self.n
        st = ''.join('<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % (s[0], s[1], s[2] if len(s) > 2 else 1) for s in stops)
        self.defs.append('<radialGradient id="%s">%s</radialGradient>' % (gid, st))
        return gid

    def add(self, bb, svg):
        self.items.append((bb, svg))

    # ---- backgrounds ----
    def hall(self, c1, c2, glow='#ffffff', grid=.05, gridc='#ffffff'):
        w, h = self.w, self.h
        d = self.lin([(0, c1), (1, c2)])
        r = self.rad([(0, glow, .20), (1, glow, 0)])
        v = self.rad([(.55, '#000', 0), (1, '#000', .45)])
        s = '<rect width="%d" height="%d" fill="url(#%s)"/>' % (w, h, d)
        for i in range(5):
            s += '<ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="url(#%s)"/>' % (w * (.08 + .21 * i), -h * .04, w * .16, h * .28, r)
        ln = ''
        for i in range(-24, int(self.W) + 25, 4):
            a, b = self.P(i, -24, 0), self.P(i, self.D + 24, 0)
            ln += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (a[0], a[1], b[0], b[1])
        for j in range(-24, int(self.D) + 25, 4):
            a, b = self.P(-24, j, 0), self.P(self.W + 24, j, 0)
            ln += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (a[0], a[1], b[0], b[1])
        s += '<g stroke="%s" stroke-opacity="%s" stroke-width="1">%s</g>' % (gridc, grid, ln)
        s += '<rect width="%d" height="%d" fill="url(#%s)"/>' % (w, h, v)
        self.bg = s

    # ---- primitives ----
    def box(self, x, y, z, dx, dy, dz, c, top=None, left=None, right=None, op=1, edge=True):
        P = self.P
        x1, y1, z1 = x + dx, y + dy, z + dz
        L, R, T = left or c, right or shade(c, -.32), top or shade(c, .2)
        g = (self._poly([P(x, y1, z), P(x1, y1, z), P(x1, y1, z1), P(x, y1, z1)], L)
             + self._poly([P(x1, y, z), P(x1, y1, z), P(x1, y1, z1), P(x1, y, z1)], R)
             + self._poly([P(x, y, z1), P(x1, y, z1), P(x1, y1, z1), P(x, y1, z1)], T))
        if edge:
            g += '<polyline points="%s" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width=".8"/>' % self._pts([P(x, y1, z1), P(x1, y1, z1), P(x1, y, z1)])
        if op < 1:
            g = '<g opacity="%s">%s</g>' % (op, g)
        self.add((x, y, z, x1, y1, z1), g)

    def wire(self, x, y, z, dx, dy, dz, c='#fff', op=.7, sw=1.2, dash=None):
        P = self.P
        x1, y1, z1 = x + dx, y + dy, z + dz
        e = [((x, y, z), (x1, y, z)), ((x1, y, z), (x1, y1, z)), ((x1, y1, z), (x, y1, z)), ((x, y1, z), (x, y, z)),
             ((x, y, z1), (x1, y, z1)), ((x1, y, z1), (x1, y1, z1)), ((x1, y1, z1), (x, y1, z1)), ((x, y1, z1), (x, y, z1)),
             ((x, y, z), (x, y, z1)), ((x1, y, z), (x1, y, z1)), ((x1, y1, z), (x1, y1, z1)), ((x, y1, z), (x, y1, z1))]
        d = ''.join('M%.1f %.1f L%.1f %.1f' % (P(*a) + P(*b)) for a, b in e)
        da = ' stroke-dasharray="%s"' % dash if dash else ''
        self.add((x, y, z, x1, y1, z1), '<path d="%s" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="%s"%s/>' % (d, c, op, sw, da))

    def frame(self, x, y, z, dx, dy, dz, c='#d9d9d9', t=.5):
        for a in (x, x + dx - t):
            for b in (y, y + dy - t):
                self.box(a, b, z, t, t, dz, c, edge=False)
        for a in (x, x + dx - t):
            self.box(a, y, z + dz - t, t, dy, t, c, edge=False)
        for b in (y, y + dy - t):
            self.box(x, b, z + dz - t, dx, t, t, c, edge=False)

    def fy(self, x0, x1, z0, z1, y, fill, op=1):
        P = self.P
        g = self._poly([P(x0, y, z0), P(x1, y, z0), P(x1, y, z1), P(x0, y, z1)], fill)
        if op < 1:
            g = '<g opacity="%s">%s</g>' % (op, g)
        self.add((x0, y, z0, x1, y + .02, z1), g)

    def fx(self, y0, y1, z0, z1, x, fill, op=1):
        P = self.P
        g = self._poly([P(x, y0, z0), P(x, y1, z0), P(x, y1, z1), P(x, y0, z1)], fill)
        if op < 1:
            g = '<g opacity="%s">%s</g>' % (op, g)
        self.add((x, y0, z0, x + .02, y1, z1), g)

    def ground(self, x0, y0, dx, dy, fill, z=.02, op=1):
        P = self.P
        g = self._poly([P(x0, y0, z), P(x0 + dx, y0, z), P(x0 + dx, y0 + dy, z), P(x0, y0 + dy, z)], fill)
        if op < 1:
            g = '<g opacity="%s">%s</g>' % (op, g)
        self.add((x0, y0, z - .01, x0 + dx, y0 + dy, z), g)

    def screen_y(self, x0, x1, z0, z1, y, c1, c2, bars=3, bc='#fff', horiz=True):
        gid = self.lin([(0, c1), (1, c2)], 0, 0, 1, 1) if horiz else self.lin([(0, c1), (1, c2)])
        self.fy(x0, x1, z0, z1, y, 'url(#%s)' % gid)
        w, h = x1 - x0, z1 - z0
        for k in range(bars):
            bw = w * (.25 + .5 * self.rnd.random())
            bz = z0 + h * (.18 + .62 * k / max(1, bars))
            self.fy(x0 + w * .08, x0 + w * .08 + bw, bz, bz + h * .07, y + .01, bc, .85)

    def screen_x(self, y0, y1, z0, z1, x, c1, c2, bars=3, bc='#fff'):
        gid = self.lin([(0, c1), (1, c2)], 0, 0, 1, 1)
        self.fx(y0, y1, z0, z1, x, 'url(#%s)' % gid)
        w, h = y1 - y0, z1 - z0
        for k in range(bars):
            bw = w * (.25 + .5 * self.rnd.random())
            bz = z0 + h * (.18 + .62 * k / max(1, bars))
            self.fx(y0 + w * .08, y0 + w * .08 + bw, bz, bz + h * .07, x + .01, bc, .85)

    def ty(self, x, y, z, txt, size, fill='#fff', anchor='start', w=800, ls=0):
        px, py = self.P(x, y, z)
        wd = len(txt) * size * .66
        x0 = x - wd / 2 if anchor == 'middle' else x
        self.add((x0, y, z, x0 + wd, y + .02, z + size),
                 '<text transform="matrix(%.4f %.4f 0 1 %.1f %.1f)" font-family="Arial,Helvetica,sans-serif" font-size="%.1f" font-weight="%d" fill="%s" text-anchor="%s" letter-spacing="%.1f">%s</text>'
                 % (C30, K, px, py, size * self.s, w, fill, anchor, ls * self.s, escape(txt)))

    def tx(self, x, y, z, txt, size, fill='#fff', anchor='start', w=800, ls=0):
        px, py = self.P(x, y, z)
        wd = len(txt) * size * .66
        y1 = y + wd / 2 if anchor == 'middle' else y
        self.add((x, y1 - wd, z, x + .02, y1, z + size),
                 '<text transform="matrix(%.4f %.4f 0 1 %.1f %.1f)" font-family="Arial,Helvetica,sans-serif" font-size="%.1f" font-weight="%d" fill="%s" text-anchor="%s" letter-spacing="%.1f">%s</text>'
                 % (C30, -K, px, py, size * self.s, w, fill, anchor, ls * self.s, escape(txt)))

    def cyl(self, cx, cy, r, z, h, c, top=None):
        ox, oy = self.P(cx, cy, z)
        rx, ry, hh = r * self.s * EX, r * self.s * EY, h * self.s
        gid = self.lin([(0, shade(c, .18)), (.55, c), (1, shade(c, -.4))], 0, 0, 1, 0)
        g = ('<path d="M%.1f %.1f L%.1f %.1f A%.1f %.1f 0 0 0 %.1f %.1f L%.1f %.1f Z" fill="url(#%s)"/>'
             % (ox - rx, oy - hh, ox - rx, oy, rx, ry, ox + rx, oy, ox + rx, oy - hh, gid))
        g += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>' % (ox, oy - hh, rx, ry, top or shade(c, .22))
        self.add((cx - r, cy - r, z, cx + r, cy + r, z + h), g)

    def disc_y(self, x, y, z, r, fill, op=1):
        px, py = self.P(x, y, z)
        self.add((x - r, y, z - r, x + r, y + .02, z + r),
                 '<g transform="matrix(%.4f %.4f 0 1 %.1f %.1f)" opacity="%s"><circle r="%.1f" fill="%s"/></g>' % (C30, K, px, py, op, r * self.s, fill))

    def ring(self, cx, cy, z, r, th, c, inner=None):
        ox, oy = self.P(cx, cy, z)
        rx, ry = r * self.s * EX, r * self.s * EY
        g = '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="%s" stroke-width="%.1f"/>' % (ox, oy, rx, ry, c, th * self.s)
        if inner:
            g += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="%s" stroke-width="%.1f" stroke-opacity=".9"/>' % (ox, oy + th * self.s * .35, rx, ry, inner, th * self.s * .25)
        self.add((cx - r, cy - r, z - .3, cx + r, cy + r, z + .3), g)

    def cable(self, x, y, z0, z1, c='#8b93a1'):
        a, b = self.P(x, y, z0), self.P(x, y, z1)
        self.add((x - .1, y - .1, z0, x + .1, y + .1, z1),
                 '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1" stroke-opacity=".7"/>' % (a[0], a[1], b[0], b[1], c))

    def person(self, x, y, c='#8b93a1', h=1.0):
        self.cyl(x, y, .8, 0, 4.2 * h, c, top=shade(c, .1))
        px, py = self.P(x, y, 4.2 * h + .55)
        self.add((x - .5, y - .5, 4.2 * h, x + .5, y + .5, 4.2 * h + 1.2),
                 '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (px, py, .62 * self.s, shade(c, .35)))

    def plant(self, x, y, pot='#2a2f38', leaf='#3f8f5a'):
        self.cyl(x, y, .9, 0, 1.6, pot)
        for dx, dy, dz, r in ((0, 0, 3.1, 1.25), (-.55, .25, 2.4, .95), (.55, .1, 2.5, .95)):
            px, py = self.P(x + dx, y + dy, dz)
            self.add((x - 1, y - 1, 1.6, x + 1, y + 1, 4.2), '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (px, py, r * self.s, shade(leaf, -.1 * (dz - 2.4))))

    def car(self, x, y, z, c='#c8c8c8'):
        self.box(x + .5, y + .5, z + .2, 13, 5, 1.0, '#101215', edge=False)
        self.box(x, y, z + .9, 14, 6, 1.7, c)
        self.box(x + 3.6, y + .7, z + 2.6, 6.6, 4.6, 1.5, shade(c, .08))
        self.fy(x + 4.3, x + 9.6, z + 2.75, z + 3.9, y + 5.32, '#0f141b')
        for wx in (x + 2.6, x + 11.4):
            px, py = self.P(wx, y + 6.02, z + 1.0)
            self.add((wx - .9, y + 6.0, z, wx + .9, y + 6.05, z + 2),
                     '<g transform="matrix(%.4f %.4f 0 1 %.1f %.1f)"><circle r="%.1f" fill="#0b0c0e"/><circle r="%.1f" fill="#6c727d"/></g>' % (C30, K, px, py, 1.15 * self.s, .55 * self.s))

    def spot(self, x, y, z, tx_, ty_, r, color='#ffffff', op=.28):
        ax, ay = self.P(x, y, z)
        cx, cy = self.P(tx_, ty_, .1)
        rx, ry = r * self.s * EX, r * self.s * EY
        g1 = self.lin([(0, color, op), (1, color, 0)], 0, 0, 0, 1)
        g2 = self.rad([(0, color, op * 1.1), (1, color, 0)])
        d = 'M%.1f %.1f L%.1f %.1f A%.1f %.1f 0 0 0 %.1f %.1f Z' % (ax - 2, ay, cx - rx, cy, rx, ry, cx + rx, cy)
        self.ov.append('<path d="%s" fill="url(#%s)"/><ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="url(#%s)"/>' % (d, g1, cx, cy, rx, ry, g2))

    def render(self, aria='', extra=''):
        it = self.items
        n = len(it)

        def behind(a, b):
            return a[3] <= b[0] + 1e-6 or a[4] <= b[1] + 1e-6 or a[5] <= b[2] + 1e-6

        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                a, b = it[i][0], it[j][0]
                ab, ba = behind(a, b), behind(b, a)
                if ab and not ba:
                    adj[i].append(j)
                    indeg[j] += 1
                elif ba and not ab:
                    adj[j].append(i)
                    indeg[i] += 1
        key = lambda i: (it[i][0][0] + it[i][0][1] + it[i][0][3] + it[i][0][4], it[i][0][2], i)
        avail = [i for i in range(n) if indeg[i] == 0]
        order = []
        seen = set()
        while avail:
            avail.sort(key=key)
            i = avail.pop(0)
            order.append(i)
            seen.add(i)
            for j in adj[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    avail.append(j)
        order += [i for i in sorted(range(n), key=key) if i not in seen]
        body = ''.join(it[i][1] for i in order)
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="%s">'
                '<defs>%s</defs>%s%s%s%s</svg>' % (self.w, self.h, self.w, self.h, escape(aria), ''.join(self.defs), self.bg, body, ''.join(self.ov), extra))

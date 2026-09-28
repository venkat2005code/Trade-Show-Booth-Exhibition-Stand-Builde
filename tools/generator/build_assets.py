"""Writes every SVG in assets/images/. Run: python3 build_assets.py"""
import os, math
from xml.sax.saxutils import escape
from kit import Scene, shade
import scenes as S

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'images')) + '/'
OR = '#ff5a1f'
written = []


def save(name, svg):
    with open(OUT + name + '.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    written.append((name, len(svg)))


# ---------------------------------------------------------------- portfolio renders
for name, fn, dims, alt in S.PROJECT_SCENES:
    sc = Scene(800, 600, dims['W'], dims['D'], dims['H'], fit=.98 if dims["W"] < 25 else .94, cy=.6)
    fn(sc)
    save(name, sc.render(alt))

# ---------------------------------------------------------------- hero art
save('hero-booth', S.hero_scene(1200, 900).render('Isometric render of a custom island exhibition stand with hanging sign'))
cs = Scene(1600, 900, 40, 30, 15, fit=.62, cy=.64)
S.nova(cs)
save('case-study-hero', cs.render('NovaTech custom island booth at TechForward Expo'))

# ---------------------------------------------------------------- services, process, blog
for name, fn in S.SERVICE_SCENES:
    save(name, fn())
for name, fn in S.PROCESS_SCENES:
    save(name, fn())
for name, fn in S.BLOG_SCENES:
    save(name, fn())


# ---------------------------------------------------------------- booth-type floor plans
def t(x, y, s, size=11, fill='#fff', anchor='middle', w=700, op=1, ls=0):
    return '<text x="%.1f" y="%.1f" font-family="Arial,Helvetica,sans-serif" font-size="%s" font-weight="%d" fill="%s" fill-opacity="%s" text-anchor="%s" letter-spacing="%s">%s</text>' % (x, y, size, w, fill, op, anchor, ls, escape(s))


def plan_fragment(x0, y0, W, D, k, spec):
    """Draw one plan at pixel origin (x0,y0), scale k px per ft."""
    o = ''
    pw, ph = W * k, D * k
    open_ = spec.get('open', [])
    band = 22
    for side in open_:
        if side == 'n':
            o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="#fff" fill-opacity=".05"/>' % (x0, y0 - band, pw, band) + t(x0 + pw / 2, y0 - 8, 'AISLE', 8, '#fff', op=.45, ls=2)
        if side == 's':
            o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="#fff" fill-opacity=".05"/>' % (x0, y0 + ph, pw, band) + t(x0 + pw / 2, y0 + ph + 15, 'AISLE', 8, '#fff', op=.45, ls=2)
        if side == 'w':
            o += '<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="#fff" fill-opacity=".05"/>' % (x0 - band, y0, band, ph)
        if side == 'e':
            o += '<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="#fff" fill-opacity=".05"/>' % (x0 + pw, y0, band, ph)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#1a2230" stroke="#fff" stroke-opacity=".5" stroke-dasharray="5 4"/>' % (x0, y0, pw, ph)
    for it in spec.get('items', []):
        kind = it[0]
        if kind == 'r':
            _, x, y, w, h, fill = it[:6]
            op = it[6] if len(it) > 6 else 1
            o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity="%s" stroke="#fff" stroke-opacity=".35"/>' % (x0 + x * k, y0 + y * k, w * k, h * k, fill, op)
        elif kind == 'c':
            _, x, y, r, fill = it
            o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" fill-opacity=".9" stroke="#fff" stroke-opacity=".4"/>' % (x0 + x * k, y0 + y * k, r * k, fill)
        elif kind == 'l':
            _, xa, ya, xb, yb, col, sw = it
            o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="square"/>' % (x0 + xa * k, y0 + ya * k, x0 + xb * k, y0 + yb * k, col, sw)
        elif kind == 't':
            _, x, y, s, size = it
            o += t(x0 + x * k, y0 + y * k, s, size, '#fff', op=.75, ls=1)
        elif kind == 'h':  # hatch (storage)
            _, x, y, w, h = it
            o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#hatch)" stroke="#fff" stroke-opacity=".35"/>' % (x0 + x * k, y0 + y * k, w * k, h * k)
    for w_ in spec.get('walls', []):
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="4" stroke-linecap="square"/>' % (x0 + w_[0] * k, y0 + w_[1] * k, x0 + w_[2] * k, y0 + w_[3] * k)
    # entry arrows
    for side in open_:
        if side == 'n':
            cx, cy, d = x0 + pw / 2, y0 - 3, 'M-9 -6 L0 3 L9 -6'
            o += '<path d="%s" transform="translate(%.1f %.1f)" fill="none" stroke="%s" stroke-width="2.4"/>' % (d, cx, cy + 12, OR)
        if side == 's':
            o += '<path d="M-9 6 L0 -3 L9 6" transform="translate(%.1f %.1f)" fill="none" stroke="%s" stroke-width="2.4"/>' % (x0 + pw / 2, y0 + ph - 12 + 8, OR)
        if side == 'w':
            o += '<path d="M-6 -9 L3 0 L-6 9" transform="translate(%.1f %.1f)" fill="none" stroke="%s" stroke-width="2.4"/>' % (x0 + 12, y0 + ph / 2, OR)
        if side == 'e':
            o += '<path d="M6 -9 L-3 0 L6 9" transform="translate(%.1f %.1f)" fill="none" stroke="%s" stroke-width="2.4"/>' % (x0 + pw - 12, y0 + ph / 2, OR)
    # dimensions
    yb = y0 + ph + (36 if 's' in open_ else 18)
    o += '<g stroke="#fff" stroke-opacity=".55" stroke-width="1"><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/></g>' % (
        x0, yb, x0 + pw, yb, x0, yb - 5, x0, yb + 5, x0 + pw, yb - 5, x0 + pw, yb + 5)
    o += t(x0 + pw / 2, yb - 6, "%d ft" % W, 10, '#fff', op=.8)
    xr = x0 + pw + (38 if 'e' in open_ else 20)
    o += '<g stroke="#fff" stroke-opacity=".55"><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/></g>' % (
        xr, y0, xr, y0 + ph, xr - 5, y0, xr + 5, y0, xr - 5, y0 + ph, xr + 5, y0 + ph)
    o += '<text transform="translate(%.1f %.1f) rotate(-90)" font-family="Arial" font-size="10" fill="#fff" fill-opacity=".8" text-anchor="middle">%d ft</text>' % (xr - 7, y0 + ph / 2, D)
    return o


def plan(name, title, sub, W, D, spec, levels=None):
    w, h = 600, 450
    o = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="%s">' % (w, h, w, h, escape(title + ' floor plan')))
    o += ('<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#fff" stroke-opacity=".05"/></pattern>'
          '<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="#fff" stroke-opacity=".4" stroke-width="2"/></pattern></defs>')
    o += '<rect width="%d" height="%d" fill="#12161d"/><rect width="%d" height="%d" fill="url(#grid)"/>' % (w, h, w, h)
    if levels:
        k = min(210 / W, 230 / D)
        for i, (lbl, sp) in enumerate(levels):
            x0 = 40 + i * 290 + 20
            y0 = 130
            o += plan_fragment(x0, y0, W, D, k, sp) + t(x0 + W * k / 2, y0 - 30, lbl, 10, OR, w=800, ls=2)
    else:
        k = min(360 / W, 240 / D)
        x0, y0 = (w - W * k) / 2 - 10, 112 + (240 - D * k) / 2
        o += plan_fragment(x0, y0, W, D, k, spec)
    o += t(28, 38, title.upper(), 13, OR, 'start', 800, 1, 2.5) + t(28, 56, sub, 11, '#fff', 'start', 400, .65)
    # compass
    o += '<g transform="translate(548 46)"><circle r="16" fill="none" stroke="#fff" stroke-opacity=".4"/><path d="M0 -11 L4 4 L0 1 L-4 4Z" fill="%s"/>%s</g>' % (OR, t(0, -20, 'N', 8, '#fff', op=.6))
    o += '</svg>'
    save(name, o)


ORC, WH, GR = OR, '#f2f0ea', '#3a4150'
plan('plan-island', 'Island booth', 'Open on four sides - maximum visibility', 20, 20,
     dict(open=['n', 's', 'e', 'w'], items=[('r', 8, 8, 4, 4, ORC, .95), ('t', 10, 10.4, 'TOWER', 7), ('r', 3, 3, 5, 1.5, WH, .9), ('r', 12, 15.5, 5, 1.5, WH, .9),
                                           ('c', 4, 15, 1.6, GR), ('c', 16, 5, 1.6, GR), ('l', 2, 11, 6, 11, '#7be0ff', 3), ('l', 14, 9, 18, 9, '#7be0ff', 3)]))
plan('plan-peninsula', 'Peninsula booth', 'Three open sides, back wall on the neighbour line', 20, 20,
     dict(open=['n', 'e', 'w'], walls=[(0, 20, 20, 20)], items=[('h', 0, 14, 5, 6), ('t', 2.5, 17.3, 'STORE', 6), ('r', 7, 15, 6, 2, ORC, .95), ('r', 4, 5, 12, 1.4, WH, .9), ('r', 8, 9, 4, 2.2, GR, .9), ('c', 15, 12, 1.5, GR), ('l', 6, 19.6, 16, 19.6, '#7be0ff', 3)]))
plan('plan-inline', 'Inline booth', 'One open side, shared walls left, right and back', 20, 10,
     dict(open=['n'], walls=[(0, 0, 0, 10), (20, 0, 20, 10), (0, 10, 20, 10)], items=[('l', 3, 9.5, 17, 9.5, '#7be0ff', 3), ('r', 4, 2, 6, 1.6, ORC, .95), ('c', 15, 5, 1.4, GR), ('r', 12, 6.5, 4, 1.2, WH, .9), ('h', 0.4, 0.4, 3, 3)]))
plan('plan-corner', 'Corner booth', 'Two open sides on an end-of-row corner', 20, 10,
     dict(open=['n', 'e'], walls=[(0, 0, 0, 10), (0, 10, 20, 10)], items=[('r', 3, 3, 6, 1.6, ORC, .95), ('c', 14, 5, 1.5, GR), ('l', 3, 9.5, 14, 9.5, '#7be0ff', 3), ('r', 15, 1, 3, 3, WH, .85)]))
mods = []
for i in range(1, 4):
    mods.append(('l', i * 3.333, 0, i * 3.333, 10, '#7be0ff', 1))
plan('plan-modular', 'Modular booth', 'Re-configurable 3 ft panel system', 10, 10,
     dict(open=['n', 'e'], walls=[(0, 0, 0, 10), (0, 10, 10, 10)], items=mods + [('r', 1, 1, 3.3, 3.3, ORC, .9), ('r', 5, 5, 4, 1.4, WH, .9), ('c', 7.5, 2.5, 1.2, GR), ('t', 5, 8.2, '3 FT GRID', 5)]))
plan('plan-double-decker', 'Double-decker stand', 'Level 1 hosts the public; level 2 hosts meetings', 30, 20, {}, levels=[
    ('LEVEL 1 - GROUND', dict(open=['n', 's', 'e', 'w'], items=[('r', 2, 2, 6, 3, WH, .9), ('r', 22, 14, 6, 3, WH, .9), ('r', 12, 6, 6, 8, ORC, .9), ('t', 15, 10.3, 'STAIR', 6), ('c', 6, 14, 1.8, GR)])),
    ('LEVEL 2 - LOUNGE', dict(open=['n', 's', 'e', 'w'], items=[('r', 0, 0, 30, 20, '#ffffff', .06), ('r', 3, 3, 8, 4, GR, .95), ('r', 18, 3, 8, 4, GR, .95), ('c', 15, 13, 2.6, ORC), ('r', 12, 6, 6, 8, '#ffffff', .12), ('t', 15, 10.3, 'VOID', 6)]))])
plan('plan-pavilion', 'Custom pavilion', 'Shared identity across multiple exhibitors', 40, 30,
     dict(open=['n', 's', 'e', 'w'], items=[('r', 1, 1, 12, 9, GR, .9), ('r', 27, 1, 12, 9, GR, .9), ('r', 1, 20, 12, 9, GR, .9), ('r', 27, 20, 12, 9, GR, .9), ('c', 20, 15, 5, ORC), ('t', 20, 15.6, 'HUB', 8), ('t', 7, 5.6, 'A', 9), ('t', 33, 5.6, 'B', 9), ('t', 7, 24.6, 'C', 9), ('t', 33, 24.6, 'D', 9)]))
plan('plan-rental', 'Rental stand', 'Pre-engineered kit - reusable, fast to install', 20, 10,
     dict(open=['n'], walls=[(0, 0, 0, 10), (0, 10, 20, 10)], items=[('l', 5, 10, 5, 0, '#7be0ff', 1), ('l', 10, 10, 10, 0, '#7be0ff', 1), ('l', 15, 10, 15, 0, '#7be0ff', 1), ('r', 5, 3, 5, 1.4, ORC, .95), ('r', 12, 4, 3, 1.2, WH, .9), ('c', 17, 7, 1.3, GR), ('t', 10, 9, 'KIT OF PARTS', 5)]))


# ---------------------------------------------------------------- brand + decoration
def booth_mark(fill='#0e1013', accent=OR):
    """Isometric open-sided stand: floor, back wall, side wall and an accent header fascia."""
    return ('<path d="M16 27 4 21l12-6 12 6z" fill="%s" opacity=".28"/><path d="M4 21V9l12-6v12z" fill="%s"/>'
            '<path d="M16 15V3l12 6v12z" fill="%s" opacity=".62"/><path d="M4 9l12-6 12 6-2.4 1.2L16 5.4 6.4 10.2z" fill="%s"/>') % (fill, fill, fill, accent)


def mark(fill='#0e1013', accent=OR, size=64):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="%d" height="%d">%s</svg>' % (size, size, booth_mark(fill, accent))


save('logo-mark', mark())
lockup = lambda c: ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 40" width="220" height="40" role="img" aria-label="Standform"><g transform="translate(2 4)">%s</g>'
                    '<text x="44" y="28" font-family="Arial Black,Arial,Helvetica,sans-serif" font-weight="900" font-size="22" letter-spacing="2" fill="%s">STANDFORM</text></svg>' % (booth_mark(c, OR), c))
save('logo', lockup('#0e1013'))
save('logo-light', lockup('#ffffff'))
save('favicon', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32"><rect width="32" height="32" fill="#0e1013"/><g transform="translate(3.2 3.2) scale(.8)">%s</g></svg>' % booth_mark('#ffffff', OR))

og = Scene(1200, 630, 40, 30, 17, fit=.5, cy=.66)
og.hall('#181c24', '#090b0e')
S.hero_scene  # keep import used
hs = S.hero_scene(1200, 630, zoom=.72)
svg = hs.render('Standform exhibition stand studio')
svg = svg.replace('</defs>', '</defs><rect width="1200" height="630" fill="#0e1013"/>', 1)
svg = svg.replace('</svg>', '<g transform="translate(60 70)"><rect x="3" y="3" width="26" height="26" fill="none" stroke="#fff" stroke-width="3"/><rect x="11" y="11" width="10" height="10" fill="%s"/>'
                  '<text x="48" y="26" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="24" letter-spacing="3" fill="#fff">STANDFORM</text></g>'
                  '<text x="60" y="360" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="66" fill="#fff">Stand out</text>'
                  '<text x="60" y="435" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="66" fill="%s">before the show</text>'
                  '<text x="60" y="510" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="66" fill="#fff">even starts.</text></svg>' % (OR, OR))
save('og-cover', svg)

# blueprint tile and floorplan decoration
save('pattern-blueprint', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" width="96" height="96"><path d="M96 0H0V96" fill="none" stroke="#fff" stroke-opacity=".08"/><path d="M48 0V96M0 48H96" fill="none" stroke="#fff" stroke-opacity=".04"/><path d="M0 8v-8h8M96 88v8h-8" fill="none" stroke="#ff5a1f" stroke-opacity=".5"/></svg>')
fp = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="800" height="500"><g fill="none" stroke="#fff" stroke-opacity=".22" stroke-width="2">'
fp += '<rect x="40" y="40" width="720" height="420"/><rect x="120" y="120" width="200" height="140"/><rect x="380" y="90" width="120" height="120"/><circle cx="600" cy="300" r="90"/><path d="M40 330h240v130M520 40v120h240M280 330h120v-70h140"/>'
fp += '</g><g fill="none" stroke="#ff5a1f" stroke-opacity=".7" stroke-width="2"><rect x="420" y="130" width="40" height="40"/><path d="M40 250h60M700 460v-60"/></g></svg>'
save('pattern-floorplan', fp)

# stylised map
m = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="900" height="600" role="img" aria-label="Stylised map showing the Standform studio location"><rect width="900" height="600" fill="#12161d"/>'
m += '<g fill="#1b2230" stroke="#fff" stroke-opacity=".06">'
for i in range(9):
    for j in range(6):
        if (i * 7 + j * 3) % 5 != 0:
            m += '<rect x="%d" y="%d" width="%d" height="%d"/>' % (30 + i * 98, 26 + j * 96, 78 + (i * j) % 3 * 6, 70 + (i + j) % 3 * 6)
m += '</g><g stroke="#2a3346" stroke-width="16" fill="none" stroke-linecap="round"><path d="M0 300H900M450 0V600M0 120L900 480M120 600L780 0"/></g>'
m += '<g stroke="#3a4560" stroke-width="3" fill="none" stroke-dasharray="10 10"><path d="M0 300H900M450 0V600"/></g>'
m += '<path d="M0 470Q200 430 330 520T900 560V600H0Z" fill="#0e2233"/>'
m += '<g transform="translate(450 300)"><circle r="46" fill="%s" fill-opacity=".18"/><circle r="26" fill="%s" fill-opacity=".3"/><path d="M0 -30c-13 0-22 9-22 21 0 15 22 34 22 34s22-19 22-34c0-12-9-21-22-21z" fill="%s" stroke="#fff" stroke-width="3"/><circle cy="-9" r="7" fill="#fff"/></g>' % (OR, OR, OR)
m += '<text x="450" y="378" font-family="Arial" font-weight="800" font-size="20" fill="#fff" text-anchor="middle">STANDFORM STUDIO</text><text x="450" y="402" font-family="Arial" font-size="14" fill="#fff" fill-opacity=".7" text-anchor="middle">1200 Expo Drive, Chicago</text></svg>'
save('map', m)

print(len(written), 'files;', sum(s for _, s in written) // 1024, 'KB total')
for n, s in written:
    if s > 30000:
        print('large:', n, s)

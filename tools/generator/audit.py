import re, os, json, glob, sys
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')) + '/'
pages = sorted(glob.glob(ROOT + 'pages/*.html'))
problems = []


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []; self.ids = []; self.h1 = 0; self.imgs_noalt = []; self.ld = []; self._ld = False; self.heads = []
        self.title = ''; self._t = False; self.labels_for = set(); self.inputs = []; self.buttons_empty = []

    def handle_starttag(self, tag, a):
        a = dict(a)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag in ('link',) and 'href' in a: self.links.append(a['href'])
        if tag in ('script', 'img', 'source') and 'src' in a: self.links.append(a['src'])
        if tag == 'h1': self.h1 += 1
        if tag in ('h1', 'h2', 'h3', 'h4'): self.heads.append(int(tag[1]))
        if tag == 'img' and 'alt' not in a: self.imgs_noalt.append(a.get('src'))
        if tag == 'script' and a.get('type') == 'application/ld+json': self._ld = True; self.ld.append('')
        if tag == 'title': self._t = True
        if tag == 'label' and 'for' in a: self.labels_for.add(a['for'])
        if tag in ('input', 'select', 'textarea') and a.get('type') not in ('hidden', 'submit', 'button'):
            self.inputs.append(a)

    def handle_endtag(self, tag):
        if tag == 'script': self._ld = False
        if tag == 'title': self._t = False

    def handle_data(self, data):
        if self._ld: self.ld[-1] += data
        if self._t: self.title += data


all_ids = {}
for f in pages:
    name = os.path.basename(f)
    src = open(f, encoding='utf-8').read()
    p = P(); p.feed(src)
    all_ids[name] = set(p.ids)
    dup = {i for i in p.ids if p.ids.count(i) > 1}
    if dup: problems.append((name, 'duplicate ids', sorted(dup)))
    if p.h1 != 1: problems.append((name, 'h1 count', p.h1))
    if p.imgs_noalt: problems.append((name, 'img without alt', p.imgs_noalt))
    for j in p.ld:
        try: json.loads(j)
        except Exception as e: problems.append((name, 'bad JSON-LD', str(e)))
    # heading order
    last = 0
    for h in p.heads:
        if last and h > last + 1: problems.append((name, 'heading jump h%d -> h%d' % (last, h), ''))
        last = h
    for a in p.inputs:
        i = a.get('id')
        if i and i not in p.labels_for and not a.get('aria-label') and not a.get('aria-labelledby'):
            problems.append((name, 'input without label', i))
    if re.search(r'href="#"', src): problems.append((name, 'dead href="#"', ''))
    if re.search(r'lorem ipsum', src, re.I): problems.append((name, 'lorem ipsum', ''))
    if re.search(r'console\.log', src): problems.append((name, 'console.log', ''))
    if 'style="' in src: problems.append((name, 'inline style attr', len(re.findall(r'style="', src))))
    for l in p.links:
        if re.match(r'^(https?:|mailto:|tel:|data:|javascript:)', l): continue
        path, _, frag = l.partition('#')
        path = path.split('?')[0]
        if not path:
            continue
        target = os.path.normpath(os.path.join(os.path.dirname(f), path))
        if not os.path.exists(target): problems.append((name, 'missing file', l))

# anchors
for f in pages:
    name = os.path.basename(f)
    src = open(f, encoding='utf-8').read()
    for l in re.findall(r'href="([^"]+)"', src):
        if re.match(r'^(https?:|mailto:|tel:)', l): continue
        path, _, frag = l.partition('#')
        path = path.split('?')[0]
        if frag:
            tgt = os.path.basename(path) if path else name
            if tgt in all_ids and frag not in all_ids[tgt]:
                problems.append((name, 'missing anchor', l))

# CSS / JS files referenced exist
for k in ('assets/css/style.css', 'assets/css/dark-mode.css', 'assets/css/rtl.css', 'robots.txt', 'sitemap.xml'):
    if not os.path.exists(ROOT + k): problems.append(('root', 'missing', k))

# CSS class coverage: classes used in HTML but not defined in CSS
css = ''.join(open(ROOT + 'assets/css/' + n, encoding='utf-8').read() for n in ('style.css', 'dark-mode.css', 'rtl.css'))
defined = set(re.findall(r'\.([a-zA-Z_][\w-]*)', css))
used = set()
for f in pages:
    for m in re.findall(r'class="([^"]+)"', open(f, encoding='utf-8').read()):
        used.update(m.split())
missing = sorted(c for c in used if c not in defined)
print('pages:', len(pages))
print('classes used but not in CSS:', missing)
for p_ in problems: print(p_)
print('problems:', len(problems))

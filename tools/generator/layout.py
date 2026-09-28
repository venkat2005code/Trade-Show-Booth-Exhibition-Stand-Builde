# -*- coding: utf-8 -*-
"""Shared page shell (head, header, drawer, footer) and reusable HTML components."""
import json
from html import escape as esc
from data import *

BASE = SITE['url']
IMG = '../assets/images/'
WARN = []

ICONS = {
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'close': '<path d="M6 6l12 12M18 6L6 18"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    'moon': '<path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5z"/>',
    'arrow': '<path d="M4 12h15M13 6l6 6-6 6"/>',
    'arrow-up-right': '<path d="M7 17L17 7M8 7h9v9"/>',
    'arrow-up': '<path d="M12 20V5M6 11l6-6 6 6"/>',
    'chevron': '<path d="M6 9l6 6 6-6"/>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>',
    'minus': '<path d="M5 12h14"/>',
    'search': '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v3a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/>',
    'pin': '<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'upload': '<path d="M12 16V4M7 9l5-5 5 5M4 20h16"/>',
    'file': '<path d="M6 3h8l5 5v13H6z"/><path d="M14 3v5h5"/>',
    'share': '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.2 10.8l7.6-3.6M8.2 13.2l7.6 3.6"/>',
    'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3A4 4 0 0 0 13 5.3l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3A4 4 0 0 0 11 18.7l1-1"/>',
    'copy': '<rect x="8" y="8" width="12" height="12" rx="1"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
    'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    'eye-off': '<path d="M3 3l18 18M10.6 5.1A9.7 9.7 0 0 1 12 5c6.5 0 10 7 10 7a17 17 0 0 1-3.2 4M6.5 6.6A17 17 0 0 0 2 12s3.5 7 10 7a9.6 9.6 0 0 0 4-.9"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a7 7 0 0 1 4 6"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="1"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    'grid': '<rect x="4" y="4" width="7" height="7"/><rect x="13" y="4" width="7" height="7"/><rect x="4" y="13" width="7" height="7"/><rect x="13" y="13" width="7" height="7"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5M3 17.5l9 5 9-5" opacity=".6"/>',
    'ruler': '<path d="M3 17L17 3l4 4L7 21z"/><path d="M8 12l2 2M11 9l2 2M14 6l2 2"/>',
    'cube': '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
    'hammer': '<path d="M14 4l6 6-3 3-6-6zM12 9L4 17l3 3 8-8"/>',
    'truck': '<path d="M2 6h11v10H2zM13 10h5l4 3v3h-9z"/><circle cx="7" cy="17.5" r="2"/><circle cx="17" cy="17.5" r="2"/>',
    'bulb': '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    'printer': '<path d="M7 9V3h10v6M7 17H4v-7h16v7h-3"/><rect x="7" y="14" width="10" height="7"/>',
    'clipboard': '<rect x="5" y="4" width="14" height="17" rx="1"/><path d="M9 4V3h6v1M9 11h6M9 15h4"/>',
    'box': '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    'calendar': '<rect x="4" y="5" width="16" height="16" rx="1"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
    'download': '<path d="M12 4v12M7 11l5 5 5-5M4 20h16"/>',
    'trash': '<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
    'edit': '<path d="M4 20l1-4L16 5l3 3L8 19zM14 7l3 3"/>',
    'bell': '<path d="M6 17V11a6 6 0 0 1 12 0v6l2 2H4zM10 21h4"/>',
    'filter': '<path d="M3 5h18l-7 8v6l-4-2v-4z"/>',
    'settings': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
    'chart': '<path d="M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-3M20 16V6" />',
    'message': '<path d="M4 5h16v11H9l-5 4z"/>',
    'alert': '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>',
    'info': '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5h.01"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    'compass': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5L13 13l-4.5 2.5L11 11z"/>',
    'play': '<path d="M8 5l11 7-11 7z"/>',
    'home': '<path d="M3 11l9-8 9 8v9H3z"/><path d="M9 20v-6h6v6"/>',
    'inbox': '<path d="M3 13l3-8h12l3 8v6H3z"/><path d="M3 13h5l1 3h6l1-3h5"/>',
    'briefcase': '<rect x="3" y="7" width="18" height="13" rx="1"/><path d="M9 7V4h6v3M3 13h18"/>',
    'ruler2': '<path d="M4 20V4M4 20h16M4 8h4M4 12h6M4 16h4"/>',
}
SOCIAL = {
    'facebook': '<path d="M14 8V6.5c0-.8.4-1.5 1.5-1.5H17V2h-2.5C11.8 2 10 3.700 10 6.500V8H7.500v3.500H10V22h4V11.500h2.800L17.500 8z" transform="translate(0 0)"/>',
    'x': '<path d="M3 3h4.500l5 6.800L18 3h3l-7.300 8.300L21.500 21H17l-5.300-7.200L5.500 21h-3l7.700-8.800z"/>',
    'linkedin': '<path d="M4 9h4v12H4zM6 3.300a2.300 2.300 0 1 1 0 4.600 2.300 2.300 0 0 1 0-4.600zM10 9h3.800v1.700c.6-1 1.900-2 3.900-2 4 0 4.300 2.600 4.300 5.800V21h-4v-5.700c0-1.400 0-3.100-1.900-3.100s-2.100 1.500-2.100 3V21h-4z"/>',
    'instagram': '<path d="M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4zm0 2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm5 2.500a4.500 4.500 0 1 1 0 9 4.500 4.500 0 0 1 0-9zm0 2a2.500 2.500 0 1 0 0 5 2.500 2.500 0 0 0 0-5zM17.200 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>',
    'youtube': '<path d="M21.600 7.200a2.500 2.500 0 0 0-1.800-1.800C18.200 5 12 5 12 5s-6.200 0-7.800.4A2.500 2.500 0 0 0 2.400 7.200C2 8.800 2 12 2 12s0 3.200.4 4.800a2.500 2.500 0 0 0 1.800 1.800C5.800 19 12 19 12 19s6.200 0 7.800-.4a2.500 2.500 0 0 0 1.800-1.800c.4-1.600.4-4.800.4-4.800s0-3.200-.4-4.800zM10 15V9l5.200 3z"/>',
}


def sprite():
    s = '<svg class="sprite" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><defs>'
    for k, v in ICONS.items():
        s += '<symbol id="i-%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</symbol>' % (k, v)
    for k, v in SOCIAL.items():
        s += '<symbol id="i-%s" viewBox="0 0 24 24" fill="currentColor">%s</symbol>' % (k, v)
    s += ('<symbol id="i-mark" viewBox="0 0 32 32">'
          '<path d="M16 27 4 21l12-6 12 6z" fill="currentColor" opacity=".28"/>'
          '<path d="M4 21V9l12-6v12z" fill="currentColor"/>'
          '<path d="M16 15V3l12 6v12z" fill="currentColor" opacity=".62"/>'
          '<path d="M4 9l12-6 12 6-2.4 1.2L16 5.4 6.4 10.2z" fill="var(--color-accent)"/>'
          '</symbol>')
    return s + '</defs></svg>'


def ic(name, cls=''):
    if name in ('arrow', 'arrow-up-right'):
        cls = (cls + ' icon--flip').strip()
    return '<svg class="icon%s" aria-hidden="true" focusable="false"><use href="#i-%s"/></svg>' % (' ' + cls if cls else '', name)


# Photographs that replace the original SVG scenes (see documentation/credits.md). name -> (file in images/photos, alt)
PHOTO = {
    'hero-booth': ('sf-hero-stand', 'Custom exhibition stand with a lounge, bar and illuminated ceiling on a busy show floor'),
    'service-01': ('sf-svc-design', 'Designer pointing to stand drawings and floor plans'),
    'service-02': ('sf-svc-construction', 'Joiner cutting panels on a workshop saw'),
    'service-03': ('sf-svc-rental', 'Modular space-frame truss system overhead in a hall'),
    'service-04': ('sf-svc-installation', 'Crew member in a hard hat fixing panels during installation'),
    'service-05': ('sf-svc-dismantling', 'Packed crates wheeled out on a hand truck after the show'),
    'service-06': ('sf-svc-graphics', 'Large-format printer laying graphics onto an aluminium panel'),
    'service-07': ('sf-svc-lighting', 'Architectural LED strip lighting along a dark stairway'),
    'service-08': ('sf-svc-project-management', 'Project manager in hi-vis signing off site plans'),
    'process-01': ('sf-proc-discovery', 'Discovery workshop with the client team'),
    'process-02': ('sf-proc-concept', 'Team sketching layout ideas with sticky notes'),
    'process-03': ('sf-proc-3d-design', 'Designer drafting a stand plan on grid paper'),
    'process-04': ('sf-proc-approval', 'Client and designer shaking hands on the approved design'),
    'process-05': ('sf-proc-fabrication', 'Router shaping a timber component in the workshop'),
    'process-06': ('sf-proc-graphics', 'Band saw cutting a graphic panel to shape'),
    'process-07': ('sf-proc-logistics', 'Shipping containers stacked at a freight yard'),
    'process-08': ('sf-proc-installation', 'Site supervisor in hi-vis inspecting the build'),
    'process-09': ('sf-proc-event-support', 'Engaged audience during a live event session'),
    'process-10': ('sf-proc-dismantling', 'Wall of stacked storage crates ready for the next show'),
    'blog-01': ('sf-blog-high-impact', 'Designer reviewing bold layout options with the client'),
    'blog-02': ('sf-blog-custom-vs-rental', 'Drawings, tape measure and hammer on a workbench'),
    'blog-03': ('sf-blog-cost', 'Budget charts reviewed across a meeting table'),
    'blog-04': ('sf-blog-trends', 'Visitor exploring a design in a virtual reality headset'),
    'blog-05': ('sf-blog-checklist', 'Planner mapping a show timeline on a whiteboard'),
    'blog-06': ('sf-blog-lighting', 'Beams of stage light cutting through haze'),
    'blog-07': ('sf-blog-mistakes', 'Gloved hands marking timber before a cut'),
    'blog-08': ('sf-blog-small-spaces', 'Tape measure checking a tight dimension'),
}


def photo_src(name):
    """Relative path (from assets/images/) for an image name: WebP photo if one exists, else the SVG."""
    return 'photos/%s.webp' % PHOTO[name][0] if name in PHOTO else name + '.svg'


def img(name, alt, w, h, cls='', eager=False, sizes=None, ext='svg'):
    a = ' fetchpriority="high"' if eager else ' loading="lazy"'
    sz = ' sizes="%s"' % sizes if sizes else ''
    if name in PHOTO:
        src = photo_src(name)
        alt = PHOTO[name][1] if alt else ''
    else:
        src = '%s.%s' % (name, ext)
    return '<img src="%s%s" alt="%s" width="%d" height="%d"%s decoding="async"%s%s>' % (IMG, src, esc(alt, True), w, h, a, sz, ' class="%s"' % cls if cls else '')


def btn(text, href, cls='btn--accent', icon='arrow', extra=''):
    i = ic(icon) if icon else ''
    return '<a class="btn %s" href="%s"%s><span>%s</span>%s</a>' % (cls, href, (' ' + extra) if extra else '', text, i)


def eyebrow(text, num=None):
    n = '<span class="eyebrow__num">%s</span>' % num if num else ''
    return '<p class="eyebrow">%s<span>%s</span></p>' % (n, text)


def section_head(eb, title, lead=None, cta=None, num=None, tag='h2', center=False, cls=''):
    l = '<p class="lead">%s</p>' % lead if lead else ''
    c = '<div class="section-head__cta">%s</div>' % cta if cta else ''
    return ('<div class="section-head%s%s reveal"><div class="section-head__text">%s<%s class="section-title">%s</%s>%s</div>%s</div>'
            % (' section-head--center' if center else '', ' ' + cls if cls else '', eyebrow(eb, num), tag, title, tag, l, c))


def crumbs(items):
    """items: [(label, href|None)]"""
    o = '<nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
    o += '<li><a href="index.html">Home</a></li>'
    for i, (lab, href) in enumerate(items):
        if href:
            o += '<li><a href="%s">%s</a></li>' % (href, lab)
        else:
            o += '<li><span aria-current="page">%s</span></li>' % lab
    return o + '</ol></nav>'


def crumbs_ld(file, items):
    els = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': BASE + '/pages/index.html'}]
    for i, (lab, href) in enumerate(items):
        els.append({'@type': 'ListItem', 'position': i + 2, 'name': lab, 'item': BASE + '/pages/' + (href or file)})
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': els}


def ld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False, separators=(',', ':'))


ORG = {'@context': 'https://schema.org', '@type': 'Organization', 'name': SITE['legal'], 'url': BASE, 'logo': BASE + '/assets/images/logo.svg',
       'email': SITE['email'], 'telephone': SITE['phone'], 'sameAs': ['https://www.linkedin.com/', 'https://www.instagram.com/', 'https://www.youtube.com/']}
WEBSITE = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE['name'], 'url': BASE,
           'potentialAction': {'@type': 'SearchAction', 'target': BASE + '/pages/portfolio.html?q={search_term_string}', 'query-input': 'required name=search_term_string'}}
LOCAL = {'@context': 'https://schema.org', '@type': 'LocalBusiness', '@id': BASE + '/#studio', 'name': SITE['legal'], 'image': BASE + '/assets/images/og-cover.jpg', 'url': BASE,
         'telephone': SITE['phone'], 'email': SITE['email'], 'priceRange': '$$$',
         'address': {'@type': 'PostalAddress', 'streetAddress': '1200 Expo Drive, Suite 300', 'addressLocality': 'Chicago', 'addressRegion': 'IL', 'postalCode': '60607', 'addressCountry': 'US'},
         'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '08:00', 'closes': '18:00'}]}

NAV = [
    ('Home', 'index.html', ('index', 'home-2'), [('Home 1 — Studio layout', 'index.html'), ('Home 2 — Case-study layout', 'home-2.html')]),
    ('About', 'about.html', ('about',), None),
    ('Services', 'services.html', ('services', 'service-details', 'booth-types', 'pricing'),
     [('All services', 'services.html'), ('Service details', 'service-details.html'), ('Booth types', 'booth-types.html'), ('Pricing & estimator', 'pricing.html')]),
    ('Portfolio', 'portfolio.html', ('portfolio', 'portfolio-details'), None),
    ('Process', 'process.html', ('process',), None),
    ('Blog', 'blog.html', ('blog', 'blog-details'), None),
    ('Contact', 'contact.html', ('contact',), None),
]


def head(key, title, desc, extra_ld=(), preload=None, og_img='og-cover.jpg', noindex=False):
    if len(title) > 62:
        WARN.append('title too long (%d): %s' % (len(title), title))
    if not 140 <= len(desc) <= 165:
        WARN.append('desc length %d: %s' % (len(desc), key))
    url = '%s/pages/%s.html' % (BASE, key)
    o = ['<!DOCTYPE html>', '<html lang="en" dir="ltr">', '<head>', '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width, initial-scale=1">',
         '<title>%s</title>' % esc(title), '<meta name="description" content="%s">' % esc(desc, True),
         '<link rel="canonical" href="%s">' % url]
    if noindex:
        o.append('<meta name="robots" content="noindex, nofollow">')
    o += ['<meta name="theme-color" content="#0e1013">',
          '<meta property="og:type" content="website">', '<meta property="og:site_name" content="%s">' % SITE['name'],
          '<meta property="og:title" content="%s">' % esc(title, True), '<meta property="og:description" content="%s">' % esc(desc, True),
          '<meta property="og:url" content="%s">' % url, '<meta property="og:image" content="%s/assets/images/%s">' % (BASE, og_img),
          '<meta name="twitter:card" content="summary_large_image">', '<meta name="twitter:title" content="%s">' % esc(title, True),
          '<meta name="twitter:description" content="%s">' % esc(desc, True), '<meta name="twitter:image" content="%s/assets/images/%s">' % (BASE, og_img),
          '<link rel="icon" href="../assets/images/favicon.svg" type="image/svg+xml">',
          '<link rel="preconnect" href="https://fonts.googleapis.com">', '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
          '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&amp;family=Inter:wght@400;500;600;700&amp;display=swap">']
    if preload:
        o.append('<link rel="preload" as="image" href="%s%s" fetchpriority="high">' % (IMG, preload))
    o += ['<script>(function(){var d=document.documentElement;d.classList.add("js");try{var t=localStorage.getItem("sf-theme");if(!t){t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"}d.setAttribute("data-theme",t);var r=localStorage.getItem("sf-dir");var q=new URLSearchParams(location.search).get("dir");if(q==="rtl"||q==="ltr"){r=q}if(r==="rtl"){d.setAttribute("dir","rtl")}}catch(e){}})();</script>',
          '<link rel="stylesheet" href="../assets/css/style.css">', '<link rel="stylesheet" href="../assets/css/dark-mode.css">', '<link rel="stylesheet" href="../assets/css/rtl.css">']
    for j in extra_ld:
        o.append(ld(j))
    o.append('</head>')
    return '\n'.join(o)


DIR_SWITCH = ('<button type="button" class="dir-toggle" data-dir-toggle aria-pressed="false" aria-label="Switch to right-to-left layout" title="Switch text direction">LTR</button>')


def header(key, overlay=False):
    o = ['<a class="skip-link" href="#main">Skip to main content</a>', sprite()]
    o.append('<header class="site-header%s" data-header><div class="container site-header__inner">' % (' site-header--overlay' if overlay else ''))
    o.append('<a class="logo" href="index.html" aria-label="Standform, home">%s<span class="logo__word">STANDFORM</span></a>' % '<svg class="logo__mark" aria-hidden="true" focusable="false"><use href="#i-mark"/></svg>')
    o.append('<nav class="nav" aria-label="Primary"><ul class="nav__list">')
    for label, href, keys, sub in NAV:
        cur = ' aria-current="page"' if key == href[:-5] else ''
        active = ' is-active' if key in keys else ''
        if sub:
            o.append('<li class="nav__item has-sub"><a class="nav__link%s" href="%s"%s>%s</a>' % (active, href, cur, label))
            o.append('<button class="nav__sub-toggle" type="button" aria-expanded="false" aria-label="%s submenu" data-sub-toggle>%s</button><ul class="nav__sub">' % (label, ic('chevron')))
            for sl, sh in sub:
                o.append('<li><a href="%s"%s>%s</a></li>' % (sh, ' aria-current="page"' if sh.replace('.html', '') == key else '', sl))
            o.append('</ul></li>')
        else:
            o.append('<li class="nav__item"><a class="nav__link%s" href="%s"%s>%s</a></li>' % (active, href, cur, label))
    o.append('</ul></nav><div class="site-header__actions">')
    o.append(DIR_SWITCH)
    o.append('<button class="icon-btn" type="button" data-theme-toggle aria-label="Switch to dark mode" aria-pressed="false">%s%s</button>' % (ic('sun', 'theme-sun'), ic('moon', 'theme-moon')))
    o.append('<a class="btn btn--accent btn--sm header-cta" href="contact.html#enquiry"><span>Request a Project Quote</span></a>')
    o.append('<button class="icon-btn nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-drawer" aria-label="Open menu" data-nav-toggle>%s%s</button>' % (ic('menu', 'nav-toggle__open'), ic('close', 'nav-toggle__close')))
    o.append('</div></div></header>')
    # mobile drawer
    o.append('<div class="drawer" id="mobile-drawer" data-drawer><div class="drawer__inner container"><nav aria-label="Mobile primary"><ol class="drawer__list">')
    for i, (label, href, keys, sub) in enumerate(NAV):
        o.append('<li><a href="%s"%s><span class="drawer__num">%02d</span><span>%s</span></a></li>' % (href, ' aria-current="page"' if key in keys else '', i + 1, label))
    o.append('</ol></nav><ul class="drawer__more"><li><a href="home-2.html">Home 2</a></li><li><a href="booth-types.html">Booth types</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="service-details.html">Service details</a></li><li><a href="login.html">Client login</a></li></ul>')
    o.append('<a class="btn btn--accent btn--lg btn--block" href="contact.html#enquiry"><span>Request a Project Quote</span>%s</a>' % ic('arrow'))
    o.append('<div class="drawer__tools"><button class="btn btn--outline btn--sm" type="button" data-theme-toggle aria-pressed="false">%s<span data-theme-label>Dark mode</span></button>' % ic('moon'))
    o.append('<span class="drawer__dir"><span>Direction</span>%s</span>' % DIR_SWITCH)
    o.append('<a class="drawer__phone" href="tel:%s">%s%s</a></div></div></div>' % (SITE['phone_raw'], ic('phone'), SITE['phone']))
    return '\n'.join(o)


def newsletter(uid='nl'):
    return ('<form class="newsletter" data-validate data-demo novalidate aria-label="Newsletter signup"><div class="field newsletter__field">'
            '<label class="sr-only" for="%s-email">Email address</label><div class="newsletter__row">'
            '<input class="input" id="%s-email" name="email" type="email" required autocomplete="email" placeholder="you@company.com" data-msg-required="Enter your email address." data-msg-type="Enter a valid email address.">'
            '<button class="btn btn--accent" type="submit"><span>Subscribe</span></button></div></div>'
            '<p class="form-status" role="status" aria-live="polite" data-status></p></form>' % (uid, uid))


def footer(scripts=()):
    o = ['<footer class="site-footer on-dark"><div class="container"><div class="footer-top">',
         '<div class="footer-brand"><a class="logo" href="index.html" aria-label="Standform, home"><svg class="logo__mark" aria-hidden="true" focusable="false"><use href="#i-mark"/></svg><span class="logo__word">STANDFORM</span></a>',
         '<p>Custom trade show booths and exhibition stands, designed, built and installed by one accountable team since 2011.</p>',
         '<p class="footer-news-label" id="nl-label">Exhibition insights, once a month</p>', newsletter('ft'),
         '<ul class="social" aria-label="Social media">']
    for n, l in (('linkedin', 'LinkedIn'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('x', 'X'), ('facebook', 'Facebook')):
        o.append('<li><a href="https://www.%s.com/" target="_blank" rel="noopener noreferrer" aria-label="%s (opens in a new tab)">%s</a></li>' % (n if n != 'x' else 'x', l, ic(n)))
    o.append('</ul></div><div class="footer-cols">')
    o.append('<nav aria-label="Quick links"><h2 class="footer-h">Quick links</h2><ul><li><a href="index.html">Home</a></li><li><a href="home-2.html">Home (case-study layout)</a></li><li><a href="about.html">About</a></li><li><a href="portfolio.html">Portfolio</a></li><li><a href="process.html">Process</a></li><li><a href="booth-types.html">Booth types</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="contact.html">Contact</a></li></ul></nav>')
    o.append('<nav aria-label="Services"><h2 class="footer-h">Services</h2><ul>%s</ul></nav>' % ''.join('<li><a href="service-details.html?service=%s">%s</a></li>' % (s['slug'], s['title']) for s in SERVICES[:6]))
    o.append('<nav aria-label="Portfolio and resources"><h2 class="footer-h">Portfolio &amp; resources</h2><ul><li><a href="portfolio.html?category=island-booth">Island booths</a></li><li><a href="portfolio.html?category=rental">Rental stands</a></li><li><a href="portfolio.html?category=double-decker">Double-decker</a></li><li><a href="blog.html">Blog</a></li><li><a href="pricing.html#estimator">Cost estimator</a></li><li><a href="service-details.html#faq">FAQ</a></li><li><a href="login.html">Client login</a></li><li><a href="register.html">Create account</a></li></ul></nav>')
    o.append('<div><h2 class="footer-h">Contact</h2><address><p>%s %s</p><p>%s <a href="tel:%s">%s</a></p><p>%s <a href="mailto:%s">%s</a></p><p>%s %s</p></address></div>'
             % (ic('pin'), SITE['address'], ic('phone'), SITE['phone_raw'], SITE['phone'], ic('mail'), SITE['email'], SITE['email'], ic('clock'), SITE['hours']))
    o.append('</div></div><div class="footer-bottom"><p>&copy; 2026 %s. Demo template content.</p><ul class="footer-legal">'
             '<li><button class="link-btn" type="button" data-legal="privacy">Privacy Policy</button></li><li><button class="link-btn" type="button" data-legal="terms">Terms</button></li>'
             '<li><button class="link-btn" type="button" data-legal="accessibility">Accessibility</button></li>'
             '<li><button class="link-btn" type="button" data-dir-toggle aria-pressed="false">%s<span data-dir-label>Test RTL</span></button></li></ul></div></div></footer>' % (SITE['legal'], ic('globe')))
    o.append('<button class="to-top" type="button" data-to-top aria-label="Back to top">%s</button>' % ic('arrow-up'))
    o.append('<div class="toasts" role="region" aria-label="Notifications" aria-live="polite" data-toasts></div>')
    o.append('<script src="../assets/js/main.js" defer></script>')
    o.append('<script src="../assets/js/forms.js" defer></script>')
    for s in scripts:
        o.append('<script src="../assets/js/%s" defer></script>' % s)
    o.append('</body></html>')
    return '\n'.join(o)


def page(key, title, desc, body, ld_extra=(), scripts=(), overlay=False, preload=None, body_class='', crumb=None, noindex=False, og='og-cover.jpg'):
    lds = list(ld_extra)
    if crumb is not None:
        lds.append(crumbs_ld(key + '.html', crumb))
    h = head(key, title, desc, lds, preload, og, noindex)
    return '%s\n<body class="page-%s %s">\n%s\n<main id="main" tabindex="-1">\n%s\n</main>\n%s' % (h, key, body_class, header(key, overlay), body, footer(scripts))


# ------------------------------------------------------------------ components
def pcard(p, cls=''):
    search = ' '.join([p['title'], p['typeLabel'], p['industryLabel'], p['event'], p['location'], p['size']]).lower()
    href = 'portfolio-details.html?project=%s' % p['slug']
    return ('<article class="pcard%s reveal" data-project data-slug="%s" data-mode="%s" data-type="%s" data-industry="%s" data-search="%s">'
            '<a class="pcard__media" href="%s" tabindex="-1" aria-hidden="true">%s<span class="pcard__badges"><span class="badge badge--dark">%s</span><span class="badge badge--accent">%s</span></span></a>'
            '<div class="pcard__body"><p class="pcard__kicker">%s <span aria-hidden="true">/</span> %s</p><h3 class="pcard__title"><a href="%s">%s</a></h3>'
            '<dl class="pcard__meta"><div><dt>Size</dt><dd>%s</dd></div><div><dt>Event</dt><dd>%s</dd></div><div><dt>Location</dt><dd>%s</dd></div></dl>'
            '<p class="pcard__desc">%s</p><div class="pcard__foot"><a class="link-arrow" href="%s"><span>View Project</span>%s<span class="sr-only"> %s</span></a>'
            '<button class="link-btn pcard__quick" type="button" data-quick-view="%s">Quick view</button></div></div></article>'
            % (' ' + cls if cls else '', p['slug'], p['mode'], p['type'], p['industry'], esc(search, True), href,
               img(p['img'], p['title'] + ' booth render', 800, 600, sizes='(min-width:1024px) 33vw, (min-width:640px) 50vw, 100vw'),
               p['typeLabel'], 'Rental' if p['mode'] == 'rental' else 'Custom', p['industryLabel'], p['size'], href, esc(p['title']),
               p['size'], esc(p['event']), esc(p['location']), esc(p['desc']), href, ic('arrow'), esc(p['title']), p['slug']))


def svc_card(s, i=None):
    return ('<article class="svc reveal"><a class="svc__media" href="service-details.html?service=%s" tabindex="-1" aria-hidden="true">%s</a><div class="svc__body"><p class="svc__num">%02d</p><h3 class="svc__title">%s</h3><p>%s</p>'
            '<a class="link-arrow" href="service-details.html?service=%s"><span>View details</span>%s<span class="sr-only"> for %s</span></a></div></article>'
            % (s['slug'], img(s['img'], s['title'] + ' illustration', 640, 480, sizes='(min-width:1024px) 25vw, (min-width:640px) 50vw, 100vw'), s['n'], s['title'], esc(s['desc']), s['slug'], ic('arrow'), s['title']))


def plan_card(b):
    return ('<article class="plan reveal"><a class="plan__media" href="booth-types.html#%s" tabindex="-1" aria-hidden="true">%s</a><div class="plan__body"><p class="plan__open">%s</p><h3>%s</h3><p>%s</p>'
            '<a class="link-arrow" href="booth-types.html#%s"><span>Explore</span>%s<span class="sr-only"> %s</span></a></div></article>'
            % (b['slug'], img(b['plan'], b['name'] + ' floor plan', 600, 450, sizes='(min-width:1024px) 33vw, (min-width:640px) 50vw, 100vw'), b['open_'], b['name'], esc(b['ideal']), b['slug'], ic('arrow'), b['name']))


def fmt_date(d):
    y, m, dd = d.split('-')
    mn = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][int(m) - 1]
    return '%s %d, %s' % (mn, int(dd), y)


def post_card(p, cls=''):
    search = (p['title'] + ' ' + p['excerpt'] + ' ' + p['catLabel']).lower()
    return ('<article class="bcard%s reveal" data-post data-cat="%s" data-search="%s"><a class="bcard__media" href="blog-details.html?post=%s" tabindex="-1" aria-hidden="true">%s</a>'
            '<div class="bcard__body"><p class="bcard__meta"><span class="badge">%s</span><time datetime="%s">%s</time><span>%d min read</span></p>'
            '<h3 class="bcard__title"><a href="blog-details.html?post=%s">%s</a></h3><p>%s</p></div></article>'
            % (' ' + cls if cls else '', p['cat'], esc(search, True), p['slug'], img(p['img'], p['title'], 800, 500, sizes='(min-width:1024px) 33vw, (min-width:640px) 50vw, 100vw'),
               p['catLabel'], p['date'], fmt_date(p['date']), p['read'], p['slug'], esc(p['title']), esc(p['excerpt'])))


def testimonial(t, big=False):
    return ('<figure class="quote%s reveal"><div class="quote__mark" aria-hidden="true">&ldquo;</div><blockquote><p>%s</p></blockquote><figcaption><span class="avatar" aria-hidden="true">%s</span>'
            '<span><strong>%s</strong><br>%s, %s<br><span class="quote__ctx">%s &middot; %s</span></span></figcaption></figure>'
            % (' quote--big' if big else '', esc(t['q']), ''.join(w[0] for w in t['name'].replace('Dr. ', '').split()[:2]), t['name'], t['role'], t['company'], t['industry'], t['ctx']))


def cta_band(title, text, primary=('Start Your Project', 'contact.html#enquiry'), secondary=None, eb='Project enquiry'):
    sec = btn(secondary[0], secondary[1], 'btn--light', 'phone' if secondary[1].startswith('tel') else 'arrow') if secondary else ''
    return ('<section class="cta-band on-dark" aria-labelledby="cta-title"><div class="container cta-band__inner"><div class="reveal">%s<h2 id="cta-title" class="section-title">%s</h2><p class="lead">%s</p>'
            '<div class="btn-row">%s%s</div></div><div class="cta-band__art" aria-hidden="true">%s</div></div></section>'
            % (eyebrow(eb), title, text, btn(primary[0], primary[1]), sec, img('pattern-floorplan', '', 800, 500)))


def page_hero(crumb, eb, title, lead, art=None, ctas='', cls=''):
    a = '<div class="page-hero__art">%s</div>' % art if art else ''
    return ('<section class="page-hero on-dark blueprint %s"><div class="container page-hero__inner"><div class="page-hero__text">%s%s<h1 class="page-title">%s</h1><p class="lead">%s</p>%s</div>%s</div></section>'
            % (cls, crumbs(crumb), eyebrow(eb), title, lead, '<div class="btn-row">%s</div>' % ctas if ctas else '', a))


def field(id_, label, type_='text', req=True, ph='', ac=None, hint='', extra='', cls=''):
    r = ' required' if req else ''
    star = '<span class="req" aria-hidden="true"> *</span>' if req else '<span class="opt"> (optional)</span>'
    a = ' autocomplete="%s"' % ac if ac else ''
    h = '<p class="field__hint" id="%s-hint">%s</p>' % (id_, hint) if hint else ''
    return ('<div class="field%s"><label class="field__label" for="%s">%s%s</label><input class="input" id="%s" name="%s" type="%s"%s%s%s%s%s>%s</div>'
            % (' ' + cls if cls else '', id_, label, star, id_, id_, type_, r, a, ' placeholder="%s"' % esc(ph, True) if ph else '', ' aria-describedby="%s-hint"' % id_ if hint else '', ' ' + extra if extra else '', h))


def select(id_, label, options, req=True, cls='', extra=''):
    r = ' required' if req else ''
    star = '<span class="req" aria-hidden="true"> *</span>' if req else '<span class="opt"> (optional)</span>'
    opts = '<option value="">Select...</option>' + ''.join('<option value="%s">%s</option>' % (v, l) for v, l in options)
    return '<div class="field%s"><label class="field__label" for="%s">%s%s</label><select class="input select" id="%s" name="%s"%s%s>%s</select></div>' % (' ' + cls if cls else '', id_, label, star, id_, id_, r, ' ' + extra if extra else '', opts)


def textarea(id_, label, req=True, ph='', rows=5, cls='', hint=''):
    r = ' required' if req else ''
    star = '<span class="req" aria-hidden="true"> *</span>' if req else '<span class="opt"> (optional)</span>'
    h = '<p class="field__hint" id="%s-hint">%s</p>' % (id_, hint) if hint else ''
    return '<div class="field%s"><label class="field__label" for="%s">%s%s</label><textarea class="input" id="%s" name="%s" rows="%d"%s%s%s minlength="10" data-msg-minlength="Please write at least 10 characters.">%s</textarea>%s</div>' % (
        ' ' + cls if cls else '', id_, label, star, id_, id_, rows, r, ' placeholder="%s"' % esc(ph, True) if ph else '', ' aria-describedby="%s-hint"' % id_ if hint else '', '', h)

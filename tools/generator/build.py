# -*- coding: utf-8 -*-
"""Assemble every page, the JS data files, sitemap.xml and robots.txt."""
import json, os, re
import layout
from layout import *
import pages_a as A, pages_b as B, pages_c as C

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')) + '/'


def write(path, text):
    os.makedirs(os.path.dirname(ROOT + path), exist_ok=True)
    with open(ROOT + path, 'w', encoding='utf-8') as f:
        f.write(text)


def pg(key, title, desc, body, **kw):
    write('pages/%s.html' % key, page(key, title, desc, body, **kw))


pf_items = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Exhibition Stand Portfolio', 'url': BASE + '/pages/portfolio.html',
            'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': BASE + '/pages/portfolio-details.html?project=' + p['slug'], 'name': p['title']} for i, p in enumerate(PROJECTS)]}}
svc_ld = {'@context': 'https://schema.org', '@type': 'Service', 'name': 'Custom Booth Design', 'serviceType': 'Exhibition stand design', 'provider': {'@type': 'LocalBusiness', 'name': SITE['legal'], 'url': BASE},
          'areaServed': ['United States', 'Europe', 'Middle East'], 'description': SERVICES[0]['overview'],
          'offers': {'@type': 'Offer', 'priceCurrency': 'USD', 'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': '95', 'priceCurrency': 'USD', 'unitText': 'per sq ft', 'referenceQuantity': {'@type': 'QuantitativeValue', 'value': '1', 'unitCode': 'FTK'}}}}
p1 = PROJECTS[0]
img_ld = {'@context': 'https://schema.org', '@type': 'ImageObject', 'contentUrl': BASE + '/assets/images/project-01.svg', 'name': p1['title'], 'description': p1['desc'], 'creator': {'@type': 'Organization', 'name': SITE['legal']}, 'caption': p1['event'] + ', ' + p1['location']}
about_ld = {'@context': 'https://schema.org', '@type': 'AboutPage', 'name': 'About Standform', 'url': BASE + '/pages/about.html', 'about': {'@type': 'Organization', 'name': SITE['legal']}}
faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}

pg('index', 'Trade Show Booth & Exhibition Stand Builder | Standform',
   'Custom trade show booths and exhibition stands designed, built and installed by one team. Island, inline, peninsula and rental stands. Request a project quote.',
   A.home1(), ld_extra=[ORG, WEBSITE, LOCAL], overlay=True, preload=photo_src('hero-booth'), scripts=['plugins/projects-data.js', 'portfolio.js'])
pg('home-2', 'Exhibition Stand Case Studies & Booth Builder | Standform',
   'Explore a full exhibition stand case study, the industries we serve, booth types and design capabilities, then send your project enquiry to our studio.',
   A.home2(), ld_extra=[ORG, WEBSITE], overlay=True, body_class='has-rail')
pg('about', 'About Standform | Exhibition Stand Design & Build Studio',
   'Meet the designers, fabricators and installers behind Standform, a Chicago exhibition studio building custom trade show booths and stands for brands since 2011.',
   A.about(), ld_extra=[about_ld, ORG], crumb=[('About', None)])
pg('services', 'Exhibition Stand Services: Design to Install | Standform',
   'Eight exhibition stand services: custom booth design, construction, rental stands, installation, dismantling, graphics, lighting and project management.',
   A.services(), crumb=[('Services', None)])
pg('service-details', 'Custom Booth Design Service | Exhibition Stands | Standform',
   'Custom exhibition booth design from concept to build-ready drawings: 3D renders, floor plans, materials and compliance checks, with clear starting-from pricing.',
   A.service_details(), ld_extra=[svc_ld, faq_ld], crumb=[('Services', 'services.html'), ('Service details', None)], scripts=['plugins/services-data.js', 'plugins/service-details.js'])
pg('booth-types', 'Booth Types: Island, Peninsula, Inline & More | Standform',
   'Compare island, peninsula, inline, corner, modular, double-decker, pavilion and rental exhibition stands by open sides, size, benefits and customisation.',
   B.booth_types(), crumb=[('Booth types', None)])
pg('portfolio', 'Exhibition Stand Portfolio | Custom & Rental | Standform',
   'Browse custom island, inline, peninsula, double-decker, pavilion and rental exhibition stands. Filter by booth type or industry and view full case studies.',
   B.portfolio(), ld_extra=[pf_items], crumb=[('Portfolio', None)], scripts=['plugins/projects-data.js', 'portfolio.js'])
pg('portfolio-details', 'NovaTech Island Booth Case Study | Portfolio | Standform',
   'A case study of NovaTech\'s 40 x 30 ft custom island at TechForward Expo: the design challenge, solution, materials, lighting, installation and results.',
   B.portfolio_details(), ld_extra=[img_ld], crumb=[('Portfolio', 'portfolio.html'), ('Project details', None)], scripts=['plugins/projects-data.js', 'plugins/lightbox.js', 'portfolio.js'])
pg('process', 'Exhibition Stand Process: Design to Dismantle | Standform',
   'How Standform delivers a trade show booth in ten stages: discovery, concept, 3D design, approval, fabrication, graphics, logistics, install, support and strike.',
   B.process(), crumb=[('Process', None)])
pg('pricing', 'Exhibition Stand Pricing & Cost Estimator | Standform',
   'Project-based exhibition stand pricing: rental, custom, island and bespoke builds. See what moves the cost and use the interactive estimator for a range.',
   B.pricing(), crumb=[('Pricing', None)], scripts=['pricing.js'])
pg('blog', 'Exhibition Stand Blog: Design, Cost & Tips | Standform',
   'Practical exhibition advice: booth design, custom vs rental, stand costs, lighting, planning checklists and small-space tips from the Standform studio team.',
   C.blog(), crumb=[('Blog', None)], scripts=['plugins/posts-data.js', 'blog.js'])
bd_body, bd_ld = C.blog_details()
pg('blog-details', 'Exhibition Stand Costs: A 2026 Guide | Standform',
   'What an exhibition stand really costs: 2026 price ranges for rental and custom booths, the factors that drive cost, hidden fees and where you can save.',
   bd_body, ld_extra=[bd_ld], crumb=[('Blog', 'blog.html'), ('Article', None)], scripts=['plugins/posts-data.js', 'blog.js'])
pg('contact', 'Contact Standform | Request a Project Quote',
   'Send your exhibition project enquiry to Standform: event, booth size, budget and timeline. Call, email or visit our Chicago studio and workshop to meet us.',
   C.contact(), ld_extra=[LOCAL], crumb=[('Contact', None)], scripts=['upload.js'])
pg('login', 'Client Login | Standform', 'Log in to the Standform client portal (demo) to review 3D renders, approve drawings and track your exhibition project schedule from first sketch to final strike.',
   C.login(), ld_extra=[ORG], noindex=True, body_class='is-auth')
pg('register', 'Create an Account | Standform', 'Create a demo Standform client account to follow your exhibition stand project, review renders, sign off drawings and see your delivery schedule in one place.',
   C.register(), ld_extra=[ORG], noindex=True, body_class='is-auth')
pg('404', 'Page Not Found | Standform', 'This page missed the exhibition floor. Head back to the Standform home page, browse the portfolio or contact the studio about your next stand.',
   C.not_found(), ld_extra=[ORG], noindex=True)
write('pages/coming-soon.html', C.coming_soon_page())
write('pages/admin-dashboard.html', C.admin_dashboard())

# strip auth/coming-soon header-less pages: auth pages use the standard shell but hide header/footer via CSS class (.is-auth)

# ---------------------------------------------------------------- JS data
def js_obj(o):
    return json.dumps(o, ensure_ascii=False, indent=1)


proj_js = [dict(slug=p['slug'], title=p['title'], type=p['type'], typeLabel=p['typeLabel'], mode=p['mode'], industry=p['industry'], industryLabel=p['industryLabel'], size=p['size'], event=p['event'], location=p['location'], year=p['year'],
                desc=p['desc'], challenge=p['challenge'], solution=p['solution'], materials=p['materials'], lighting=p['lighting'], branding=p['branding'], construction=p['construction'], install=p['install'],
                results=[list(r) for r in p['results']], img=p['img']) for p in PROJECTS]
write('assets/js/plugins/projects-data.js', '/* Demo project data for portfolio-details.html and quick view. Generated from the template content; edit freely. */\nwindow.SF_PROJECTS = %s;\nwindow.SF_PLANS = %s;\n' % (js_obj(proj_js), js_obj(B.PLAN_FOR)))
posts_js = [dict(slug=p['slug'], title=p['title'], cat=p['cat'], catLabel=p['catLabel'], date=p['date'], dateLabel=fmt_date(p['date']), read=p['read'], author=p['author'], excerpt=p['excerpt'], img=photo_src(p['img']), imgAlt=PHOTO.get(p['img'], ('', p['title']))[1], sections=[list(s) for s in p['sections']]) for p in POSTS]
write('assets/js/plugins/posts-data.js', '/* Demo blog data used by blog-details.html. */\nwindow.SF_POSTS = %s;\n' % js_obj(posts_js))
svc_js = [dict(slug=s['slug'], n=s['n'], title=s['title'], tagline=s['tagline'], overview=s['overview'], includes=s['includes'], benefits=s['benefits'], deliverables=s['deliverables'], img=photo_src(s['img']), imgAlt=PHOTO.get(s['img'], ('', s['title']))[1],
               priceLabel=s['price'][0], priceNote=s['price'][1], priceRows=[list(r) for r in s['price'][2]]) for s in SERVICES]
write('assets/js/plugins/services-data.js', '/* Demo service data used by service-details.html. */\nwindow.SF_SERVICES = %s;\n' % js_obj(svc_js))

# ---------------------------------------------------------------- SEO files
keys = ['index', 'home-2', 'about', 'services', 'service-details', 'booth-types', 'portfolio', 'portfolio-details', 'process', 'pricing', 'blog', 'blog-details', 'contact', 'login', 'register', 'coming-soon']
pri = {'index': '1.0', 'portfolio': '0.9', 'services': '0.9', 'contact': '0.9', 'pricing': '0.8'}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for k in keys:
    sm += '  <url><loc>%s/pages/%s.html</loc><lastmod>2026-09-27</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>\n' % (BASE, k, pri.get(k, '0.6'))
for p in PROJECTS:
    sm += '  <url><loc>%s/pages/portfolio-details.html?project=%s</loc><lastmod>2026-09-27</lastmod><priority>0.7</priority></url>\n' % (BASE, p['slug'])
for p in POSTS:
    sm += '  <url><loc>%s/pages/blog-details.html?post=%s</loc><lastmod>%s</lastmod><priority>0.6</priority></url>\n' % (BASE, p['slug'], p['date'])
for s in SERVICES:
    sm += '  <url><loc>%s/pages/service-details.html?service=%s</loc><lastmod>2026-09-27</lastmod><priority>0.7</priority></url>\n' % (BASE, s['slug'])
write('sitemap.xml', sm + '</urlset>\n')
write('robots.txt', '# Replace the sitemap host with your production domain before launch.\nUser-agent: *\nAllow: /\nDisallow: /pages/admin-dashboard.html\nDisallow: /pages/login.html\nDisallow: /pages/register.html\nDisallow: /pages/404.html\n\nSitemap: %s/sitemap.xml\n' % BASE)

for w in layout.WARN:
    print('WARN', w)
print('built')

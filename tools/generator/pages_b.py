# -*- coding: utf-8 -*-
from layout import *
from pages_a import frame, P, PN

PLAN_FOR = {'island': 'plan-island', 'inline': 'plan-inline', 'peninsula': 'plan-peninsula', 'pavilion': 'plan-pavilion', 'double-decker': 'plan-double-decker'}


def booth_types():
    o = [page_hero([('Booth types', None)], 'Booth types', 'Find the footprint that fits your show.',
                   'Eight booth configurations, from a lean 10 × 10 inline to a two-level pavilion. Compare open sides, size ranges, strengths and customisation options.',
                   frame(img('plan-island', 'Island booth floor plan', 600, 450, eager=True)), btn('Request a Project Quote', 'contact.html#enquiry') + btn('View Pricing', 'pricing.html', 'btn--outline-light'))]
    o.append('<section class="section" aria-labelledby="bt-list"><div class="container"><h2 id="bt-list" class="sr-only">Booth types in detail</h2><ol class="bt-list">')
    for i, b in enumerate(BOOTH_TYPES):
        o.append('<li class="bt reveal" id="%s"><div class="bt__media">%s</div><div class="bt__body"><p class="bt__k"><span class="badge badge--accent">%s</span><span class="badge">%s</span></p><h3 class="bt__title">%s</h3>'
                 '<dl class="bt__facts"><div><dt>Ideal use</dt><dd>%s</dd></div><div><dt>Typical layout</dt><dd>%s</dd></div></dl>'
                 '<div class="bt__lists"><div><h4>Benefits</h4><ul class="checklist">%s</ul></div><div><h4>Customisation options</h4><ul class="checklist">%s</ul></div></div>'
                 '<div class="btn-row">%s%s</div></div></li>'
                 % (b['slug'], frame(img(b['plan'], b['name'] + ' floor plan', 600, 450)), b['open_'], b['size'], b['name'], esc(b['ideal']), esc(b['layout']),
                    ''.join('<li>%s<span>%s</span></li>' % (ic('check'), x) for x in b['benefits']), ''.join('<li>%s<span>%s</span></li>' % (ic('check'), x) for x in b['custom']),
                    btn('Quote this booth', 'contact.html?type=%s#enquiry' % b['slug'], 'btn--accent btn--sm'), btn('See projects', 'portfolio.html?category=%s' % b['filter'], 'btn--outline btn--sm')))
    o.append('</ol></div></section>')
    rows = [('Island', '4', '20 × 20 +', 'Highest', '$$$$', 'Launches, large demos'), ('Peninsula', '3', '20 × 20 +', 'High', '$$$', 'Balanced impact'), ('Inline', '1', '10 × 10 +', 'Standard', '$', 'First-time exhibitors'),
            ('Corner', '2', '10 × 10 +', 'Good', '$$', 'Step up from inline'), ('Modular', '1 - 4', '10 × 10 +', 'Flexible', '$$', 'Multi-show programmes'), ('Double-decker', '2 levels', '30 × 30 +', 'Landmark', '$$$$$', 'Hospitality and meetings'),
            ('Pavilion', 'Multiple', '40 × 30 +', 'High', '$$$$', 'Consortia, regions'), ('Rental', 'Any', '10 × 10 +', 'Varies', '$ - $$$', 'Single-show budgets')]
    hdr = ['Type', 'Open sides', 'Typical size (ft)', 'Visibility', 'Budget', 'Best for']
    o.append('<section class="section section--alt" aria-labelledby="cmp-title"><div class="container">%s<div class="table-wrap" tabindex="0" role="region" aria-label="Booth type comparison table"><table class="table table--stack"><caption class="sr-only">Comparison of booth types</caption><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></div></section>'
             % (section_head('Quick comparison', 'Booth types at a glance.', None, None).replace('<h2 class="section-title">', '<h2 class="section-title" id="cmp-title">'), ''.join('<th scope="col">%s</th>' % h for h in hdr),
                ''.join('<tr><th scope="row" data-label="Type">%s</th>%s</tr>' % (r[0], ''.join('<td data-label="%s">%s</td>' % (hdr[i + 1], c) for i, c in enumerate(r[1:]))) for r in rows)))
    o.append(cta_band('Not sure which booth type fits?', 'Tell us your hall, footprint and goals. We will recommend a configuration and show you why.', ('Request a Project Quote', 'contact.html#enquiry'), ('See the estimator', 'pricing.html#estimator')))
    return '\n'.join(o)


def portfolio():
    o = [page_hero([('Portfolio', None)], 'Portfolio', 'Twelve stands. Twelve different briefs.',
                   'Island booths, inline stands, double-deckers and pavilions built for technology, healthcare, automotive, manufacturing, retail, finance and food brands.',
                   frame(img('project-05', 'Vantage Motors double-decker render', 800, 600, eager=True)), btn('Request a Project Quote', 'contact.html#enquiry'))]
    o.append('<section class="section section--tight" aria-labelledby="pf-all"><div class="container" data-portfolio data-portfolio-page><h2 id="pf-all" class="sr-only">All projects</h2>')
    o.append('<div class="filterbar" data-filterbar><div class="chips" role="group" aria-label="Filter by booth category">%s</div>' % ''.join('<button class="chip" type="button" data-filter="%s" aria-pressed="%s">%s</button>' % (v, 'true' if v == 'all' else 'false', l) for v, l in CATEGORIES))
    o.append('<div class="filterbar__row"><div class="field field--inline"><label class="field__label" for="pf-industry">Industry</label><select class="input select" id="pf-industry" data-industry><option value="all">All industries</option>%s</select></div>'
             '<div class="field field--grow"><label class="field__label" for="pf-search">Search</label><div class="search">%s<input class="input" id="pf-search" type="search" placeholder="Name, event or city" autocomplete="off" data-search></div></div>'
             '<button class="btn btn--outline btn--sm" type="button" data-reset>Reset filters</button></div><p class="filterbar__count" role="status" aria-live="polite" data-result-count>Showing 12 projects</p></div>' % (''.join('<option value="%s">%s</option>' % (v, l) for v, l in INDUSTRIES), ic('search')))
    o.append('<div class="pgrid" data-grid>%s</div><div class="empty" data-empty hidden><h3>No projects match those filters.</h3><p>Try a different category or clear the search.</p><button class="btn btn--dark btn--sm" type="button" data-reset>Reset filters</button></div></div></section>' % ''.join(pcard(p) for p in PROJECTS))
    o.append(cta_band('Want your stand in this gallery?', 'Tell us about your next show and we will send a first layout idea within a week.', ('Start Your Project', 'contact.html#enquiry'), ('See booth types', 'booth-types.html')))
    return '\n'.join(o)


def portfolio_details():
    p = PROJECTS[0]
    o = []
    o.append('<section class="pd-hero on-dark" aria-labelledby="pd-title"><div class="container pd-hero__inner">%s<div class="pd-hero__text"><p class="pd-hero__badges"><span class="badge badge--accent" data-p="typeLabel">%s</span><span class="badge badge--dark" data-p="industryLabel">%s</span></p><h1 id="pd-title" class="page-title" data-p="title">%s</h1><p class="lead" data-p="desc">%s</p></div>%s</div></section>'
             % (crumbs([('Portfolio', 'portfolio.html'), ('<span data-p="title">%s</span>' % p['title'], None)]), p['typeLabel'], p['industryLabel'], p['title'], esc(p['desc']),
                frame('<img src="%s%s.svg" alt="%s" width="800" height="600" fetchpriority="high" decoding="async" data-p-img>' % (IMG, p['img'], p['title'] + ' booth render'), 'pd-hero__frame')))
    o.append('<section class="spec-strip-wrap"><div class="container"><dl class="spec-strip"><div><dt>Event</dt><dd data-p="event">%s</dd></div><div><dt>Location</dt><dd data-p="location">%s</dd></div><div><dt>Booth size</dt><dd data-p="size">%s</dd></div><div><dt>Industry</dt><dd data-p="industryLabel">%s</dd></div><div><dt>Project type</dt><dd data-p="typeLabel">%s</dd></div><div><dt>Year</dt><dd data-p="year">%s</dd></div></dl></div></section>'
             % (esc(p['event']), p['location'], p['size'], p['industryLabel'], p['typeLabel'], p['year']))
    o.append('<section class="section" aria-labelledby="cs-t"><div class="container"><h2 id="cs-t" class="sr-only">Case study</h2><div class="case"><article class="case__col reveal">%s<h3>The design challenge</h3><p data-p="challenge">%s</p></article><article class="case__col case__col--accent reveal">%s<h3>The design solution</h3><p data-p="solution">%s</p></article></div></div></section>'
             % (ic('target'), p['challenge'], ic('bulb'), p['solution']))
    o.append('<section class="section section--alt" aria-labelledby="sp-t"><div class="container">%s<div class="spec-grid"><article class="spec reveal"><h3>%s Materials</h3><ul class="checklist" data-p-list="materials">%s</ul></article><article class="spec reveal"><h3>%s Lighting</h3><p data-p="lighting">%s</p></article><article class="spec reveal"><h3>%s Branding</h3><p data-p="branding">%s</p></article><article class="spec reveal"><h3>%s Construction</h3><p data-p="construction">%s</p></article><article class="spec reveal"><h3>%s Installation</h3><p data-p="install">%s</p></article></div></div></section>'
             % (section_head('Specification', 'How it was made.', None, None).replace('<h2 class="section-title">', '<h2 class="section-title" id="sp-t">'), ic('layers'), ''.join('<li>%s<span>%s</span></li>' % (ic('check'), m) for m in p['materials']), ic('bulb'), p['lighting'], ic('printer'), p['branding'], ic('hammer'), p['construction'], ic('truck'), p['install']))
    o.append('<section class="section" aria-labelledby="ga-t"><div class="container">%s<ul class="gallery" data-gallery><li class="gallery__item gallery__item--wide"><button type="button" data-lightbox="0" aria-label="Open image: perspective render"><img src="%s%s.svg" alt="%s perspective render" width="800" height="600" loading="lazy" data-p-gallery="0"><span>Perspective</span></button></li>'
             '<li class="gallery__item"><button type="button" data-lightbox="1" aria-label="Open image: floor plan"><img src="%splan-island.svg" alt="Floor plan" width="600" height="450" loading="lazy" data-p-plan><span>Floor plan</span></button></li>'
             '<li class="gallery__item"><button type="button" data-lightbox="2" aria-label="Open image: detail crop, left side"><img class="crop crop--a" src="%s%s.svg" alt="Detail crop of the booth left side" width="800" height="600" loading="lazy" data-p-gallery="2"><span>Detail A</span></button></li>'
             '<li class="gallery__item"><button type="button" data-lightbox="3" aria-label="Open image: detail crop, right side"><img class="crop crop--b" src="%s%s.svg" alt="Detail crop of the booth right side" width="800" height="600" loading="lazy" data-p-gallery="3"><span>Detail B</span></button></li></ul></div></section>'
             % (section_head('Gallery', 'From every angle.', 'Select any image to enlarge it. Use the arrow keys to move between views.', None).replace('<h2 class="section-title">', '<h2 class="section-title" id="ga-t">'), IMG, p['img'], p['title'], IMG, IMG, p['img'], IMG, p['img']))
    o.append('<section class="section on-dark" aria-labelledby="rs-t"><div class="container">%s<ul class="results" data-p-results>%s</ul><p class="note">Results are client-reported demo content.</p></div></section>'
             % (section_head('Project outcome', 'What the stand delivered.', None, None).replace('<h2 class="section-title">', '<h2 class="section-title" id="rs-t">'), ''.join('<li class="result reveal"><strong>%s</strong><span>%s</span></li>' % r for r in p['results'])))
    rel = [PN[5], PN[6], PN[8]]
    o.append('<section class="section" aria-labelledby="rp-t"><div class="container">%s<div class="pgrid" data-related-projects>%s</div></div></section>'
             % (section_head('Related projects', 'More like this.', None, btn('All Projects', 'portfolio.html', 'btn--dark')).replace('<h2 class="section-title">', '<h2 class="section-title" id="rp-t">'), ''.join(pcard(x) for x in rel)))
    o.append(cta_band('Planning a stand like this?', 'Send us your show, footprint and goals. We will reply with ideas, a rough range and a schedule.', ('Request a Project Quote', 'contact.html#enquiry'), ('View Pricing', 'pricing.html')))
    return '\n'.join(o)


def process():
    o = [page_hero([('Process', None)], 'How we work', 'Ten stages from first call to final strike.',
                   'A transparent workflow with a named owner, a fixed deliverable and a clear decision point at every stage. No surprises on show day.',
                   frame(img('service-08', 'Project manager signing off stand plans on site', 400, 300, eager=True)), btn('Discuss Your Exhibition Project', 'contact.html#enquiry'))]
    o.append('<section class="section" aria-labelledby="tl-t"><div class="container"><h2 id="tl-t" class="sr-only">The ten stages</h2><ol class="tl">')
    for i, (t, d, bl, dur) in enumerate(PROCESS):
        extra = ''
        if i == 0:
            extra = '<p class="tl__ask">We will ask about: <strong>brand, event, booth size, goals, audience, budget and timeline.</strong></p>'
        o.append('<li class="tl__step reveal"><div class="tl__num" aria-hidden="true">%02d</div><div class="tl__card"><div class="tl__media">%s</div><div class="tl__body"><p class="tl__dur"><span class="badge badge--accent">%s</span></p><h3>%s</h3><p>%s</p>%s<ul class="checklist checklist--tight">%s</ul></div></div></li>'
                 % (i + 1, img('process-%02d' % (i + 1), t + ' illustration', 400, 300, sizes='(min-width:1024px) 30vw, 100vw'), dur, t, d, extra, ''.join('<li>%s<span>%s</span></li>' % (ic('check'), b) for b in bl)))
    o.append('</ol></div></section>')
    # gantt
    g = [('Discovery', 1, 1), ('Concept', 2, 2), ('3D design', 3, 3), ('Approval', 5, 1), ('Fabrication', 6, 6), ('Graphics', 8, 4), ('Logistics', 12, 2), ('Installation', 14, 1), ('Event', 15, 1), ('Dismantling', 16, 1)]
    o.append('<section class="section section--alt" aria-labelledby="gt-t"><div class="container">%s<div class="gantt-wrap" tabindex="0" role="region" aria-label="Sixteen week timeline, scrolls horizontally on small screens"><div class="gantt" role="table" aria-label="Typical 16-week project timeline"><div class="gantt__head" role="row"><span class="gantt__label" role="columnheader">Stage</span>%s</div>%s</div></div><p class="note">Typical timeline for a custom 20 × 20 island. Rental and inline stands compress this to 6 - 8 weeks.</p></div></section>'
             % (section_head('Typical timeline', '16 weeks, at a glance.', None, None).replace('<h2 class="section-title">', '<h2 class="section-title" id="gt-t">'), ''.join('<span role="columnheader">W%d</span>' % w for w in range(1, 17)),
                ''.join('<div class="gantt__row" role="row"><span class="gantt__label" role="rowheader">%s</span><span class="gantt__bar gc-%d gs-%d" role="cell" aria-label="Week %d to %d"></span></div>' % (n, s, l, s, s + l - 1) for n, s, l in g)))
    o.append('<section class="section" aria-labelledby="ch-t"><div class="container split"><div class="reveal">%s<h2 id="ch-t" class="section-title">What we need from you.</h2><p class="lead">You do not need a finished brief. Bring what you have and we will fill in the rest together.</p></div><ul class="checklist checklist--2 reveal">%s</ul></div></section>'
             % (eyebrow('Discovery checklist'), ''.join('<li>%s<span>%s</span></li>' % (ic('check'), x) for x in ('Brand guidelines and logo files', 'Show name, hall and stand number', 'Exhibitor manual or show-kit link', 'Booth size and open sides', 'Goals and audience', 'Budget range or ceiling', 'Key dates: show, install, dismantle', 'Any products or equipment to display'))))
    o.append(cta_band('Discuss Your Exhibition Project', 'Start with a 30-minute call. We will map your show against this process and give you a realistic schedule.', ('Book a Discovery Call', 'contact.html#enquiry'), ('See booth types', 'booth-types.html')))
    return '\n'.join(o)


FACTORS = [('i-cube', 'Booth size', 'Cost scales with floor area, but rarely in a straight line. Larger stands benefit from economies in design and installation.'), ('i-layers', 'Design complexity', 'Curves, double-height walls, and bespoke structures need more design hours and fabrication.'),
           ('i-hammer', 'Materials', 'Timber, aluminium, solid surface and glass each carry different costs and lifespans.'), ('i-printer', 'Graphics', 'Fabric, backlit and dimensional signage cost more than direct-print panels.'),
           ('i-bulb', 'Lighting', 'Feature lighting, LED walls and control add cost and power demand.'), ('i-users', 'Furniture', 'Rented furniture is cheap; bespoke seating and counters are custom pieces.'),
           ('i-settings', 'Technology', 'Screens, interactive demos and live product integration need hardware and programming.'), ('i-truck', 'Installation', 'Venue labour rules, number of days and access equipment drive installation cost.'),
           ('i-pin', 'Event location', 'Freight, local labour rates and hall regulations vary between cities and countries.'), ('i-calendar', 'Rental duration', 'Rental costs are based on days on floor; multi-show contracts reduce the per-show cost.')]


def pricing():
    o = [page_hero([('Pricing', None)], 'Pricing', 'Project-based pricing, explained honestly.',
                   'Exhibition stands are priced by footprint, complexity and show location, not in fixed packages. Here is what to expect, what drives the number and a quick estimator.',
                   frame(img('blog-03', 'Illustration of stand costs and budget', 800, 500, eager=True)), btn('Estimate My Project', '#estimator') + btn('Request a Quote', 'contact.html#enquiry', 'btn--outline-light'))]
    models = [('Rental Stand Pricing', 'From $42 / sq ft', 'Engineered kit with custom graphics. Priced per show.', ['10 × 10 inline from $4,200', '20 × 20 island from $22,000', 'Multi-show agreements up to 15% less'], 'Single shows, tight timelines'),
              ('Custom Booth Pricing', 'From $95 / sq ft', 'Fully bespoke inline, corner and peninsula stands.', ['10 × 20 inline from $19,000', '20 × 20 peninsula from $50,000', 'Design credited against the build'], 'Brand-led stands you will reuse'),
              ('Large Island Booths', 'From $145 / sq ft', 'Free-standing islands with hanging structures and hospitality.', ['30 × 30 island from $130,000', '40 × 40 island from $232,000', 'Structural drawings included'], 'Launches and flagship shows'),
              ('Custom Exhibition Projects', 'Quoted per project', 'Double-deckers, pavilions and multi-show programmes.', ['Double-decker from $150,000', 'Pavilions from $180,000', 'Multi-show planning and storage'], 'Complex, multi-level or multi-exhibitor builds')]
    o.append('<section class="section" aria-labelledby="pm-t"><div class="container">%s<div class="models">%s</div><p class="note">All prices are demonstration figures in US dollars and exclude hall-controlled services such as power, rigging and drayage.</p></div></section>'
             % (section_head('Pricing models', 'Choose the model that matches your show.', None, None, '01').replace('<h2 class="section-title">', '<h2 class="section-title" id="pm-t">'),
                ''.join('<article class="model reveal"><h3>%s</h3><p class="model__price">%s</p><p>%s</p><ul class="checklist">%s</ul><p class="model__for"><strong>Best for:</strong> %s</p>%s</article>' % (t, pr, d, ''.join('<li>%s<span>%s</span></li>' % (ic('check'), x) for x in l), f, btn('Request a Quote', 'contact.html#enquiry', 'btn--dark btn--sm btn--block')) for t, pr, d, l, f in models)))
    o.append('<section class="section section--alt" aria-labelledby="fc-t"><div class="container">%s<ul class="factors">%s</ul></div></section>'
             % (section_head('Cost factors', 'What moves the price.', 'Ten variables shape every quote. Understanding them helps you decide where to spend and where to save.', None, '02').replace('<h2 class="section-title">', '<h2 class="section-title" id="fc-t">'),
                ''.join('<li class="factor reveal">%s<h3>%s</h3><p>%s</p></li>' % (ic(i[2:]), t, d) for i, t, d in FACTORS)))
    o.append('''<section class="section" id="estimator" aria-labelledby="est-t"><div class="container">%s
<div class="calc" data-calc><form class="calc__form" aria-label="Project cost estimator" novalidate>
<fieldset class="calc__group"><legend>Booth</legend><div class="form-grid">
<div class="field"><label class="field__label" for="c-w">Width (ft)</label><input class="input" id="c-w" name="w" type="number" min="10" max="100" step="5" value="20" inputmode="numeric" data-calc-input></div>
<div class="field"><label class="field__label" for="c-d">Depth (ft)</label><input class="input" id="c-d" name="d" type="number" min="10" max="100" step="5" value="20" inputmode="numeric" data-calc-input></div>
<div class="field"><label class="field__label" for="c-type">Booth type</label><select class="input select" id="c-type" name="type" data-calc-input><option value="inline">Inline</option><option value="corner">Corner</option><option value="peninsula">Peninsula</option><option value="island" selected>Island</option><option value="modular">Modular</option><option value="double">Double-decker</option><option value="pavilion">Pavilion</option></select></div>
<div class="field"><label class="field__label" for="c-loc">Event location</label><select class="input select" id="c-loc" name="loc" data-calc-input><option value="local">Same region as our workshop</option><option value="domestic">Elsewhere in the same country</option><option value="intl">International</option></select></div></div>
<div class="segmented" role="radiogroup" aria-label="Build approach"><label><input type="radio" name="mode" value="custom" checked data-calc-input><span>Custom build</span></label><label><input type="radio" name="mode" value="rental" data-calc-input><span>Rental stand</span></label></div></fieldset>
<fieldset class="calc__group"><legend>Options</legend><div class="form-grid">
<div class="field"><label class="field__label" for="c-gfx">Graphics</label><select class="input select" id="c-gfx" name="gfx" data-calc-input><option value="0">Standard printed panels</option><option value="1" selected>Large-format fabric walls</option><option value="2">Full-wrap and dimensional signage</option></select></div>
<div class="field"><label class="field__label" for="c-lit">Lighting</label><select class="input select" id="c-lit" name="lit" data-calc-input><option value="0">Standard spots</option><option value="1" selected>Accent and feature lighting</option><option value="2">LED walls and truss lighting</option></select></div>
<div class="field"><label class="field__label" for="c-fur">Furniture</label><select class="input select" id="c-fur" name="fur" data-calc-input><option value="0">None</option><option value="1" selected>Basic counters and seating</option><option value="2">Lounge and meeting room</option></select></div>
<div class="field" data-rental-only><label class="field__label" for="c-days">Rental days on floor</label><input class="input" id="c-days" name="days" type="number" min="3" max="14" value="4" inputmode="numeric" data-calc-input></div></div>
<label class="check"><input type="checkbox" name="inst" checked data-calc-input><span>Include installation and dismantling</span></label></fieldset></form>
<div class="calc__result" role="region" aria-labelledby="calc-out-t"><h3 id="calc-out-t" class="calc__title">Estimated Project Range</h3><p class="calc__range" data-calc-range aria-live="polite">$0 - $0</p><p class="calc__sub" data-calc-sub></p><dl class="calc__break" data-calc-break></dl>
<a class="btn btn--accent btn--block" href="contact.html#enquiry" data-calc-cta><span>Request a Quote With These Details</span>%s</a><p class="calc__note">Estimated range only &mdash; final pricing depends on project requirements. This demo calculator does not create a binding quotation.</p></div></div></div></section>''' % (section_head('Project estimator', 'Get a ballpark in 30 seconds.', 'Adjust the inputs to see how footprint, build approach and options change the range.', None, '03').replace('<h2 class="section-title">', '<h2 class="section-title" id="est-t">'), ic('arrow')))
    rows = [('10 × 10 inline', '$4,200 - $7,200', '$9,500 - $15,000'), ('10 × 20 inline', '$8,400 - $14,400', '$19,000 - $30,000'), ('20 × 20 peninsula', '$20,000 - $30,500', '$50,000 - $76,000'), ('20 × 20 island', '$22,000 - $34,000', '$58,000 - $92,000'), ('30 × 30 island', '$49,500 - $76,500', '$130,500 - $207,000'), ('Double-decker (2,000 sq ft footprint)', 'On request', '$340,000 - $520,000')]
    o.append('<section class="section section--alt" aria-labelledby="rg-t"><div class="container">%s<div class="table-wrap" tabindex="0" role="region" aria-label="Indicative price ranges"><table class="table table--stack"><caption class="sr-only">Indicative price ranges by booth size</caption><thead><tr><th scope="col">Booth</th><th scope="col">Rental (per show)</th><th scope="col">Custom build</th></tr></thead><tbody>%s</tbody></table></div><p class="note">Demonstration ranges for structure and design only. Graphics, lighting, furniture and installation are added in the estimator above. Final pricing requires a quote.</p><p class="payment-note">Project deposits and stage payments can be paid by bank transfer, by card through Stripe or by PayPal.</p><!-- TODO: Stripe / PayPal checkout integration point: add your Stripe Payment Link or PayPal button here --></div></section>'
             % (section_head('Indicative ranges', 'Typical budgets by booth size.', None, None, '04').replace('<h2 class="section-title">', '<h2 class="section-title" id="rg-t">'), ''.join('<tr><th scope="row" data-label="Booth">%s</th><td data-label="Rental (per show)">%s</td><td data-label="Custom build">%s</td></tr>' % r for r in rows)))
    o.append(cta_band('Get a fixed-scope quote.', 'A designer will review your brief and reply with a range, a schedule and the questions that matter.', ('Request a Project Quote', 'contact.html#enquiry'), ('Read the cost guide', 'blog-details.html?post=how-much-does-an-exhibition-stand-cost')))
    return '\n'.join(o)

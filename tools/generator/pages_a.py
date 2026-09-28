# -*- coding: utf-8 -*-
from layout import *

P = {p['slug']: p for p in PROJECTS}
PN = {p['n']: p for p in PROJECTS}
SV = {s['slug']: s for s in SERVICES}


def frame(inner, cls=''):
    return '<div class="frame %s">%s<i class="frame__c frame__c--tl"></i><i class="frame__c frame__c--tr"></i><i class="frame__c frame__c--bl"></i><i class="frame__c frame__c--br"></i></div>' % (cls, inner)


WHY = [('i-ruler', 'Custom design', 'No catalogue stands. Every layout starts from your brand, your audience and your footprint.'),
       ('i-clipboard', 'End-to-end execution', 'Design, build, graphics, freight, install and strike under one contract and one schedule.'),
       ('i-users', 'Experienced installation team', 'Named supervisors and crews who have built in more than 60 venues.'),
       ('i-hammer', 'Quality fabrication', 'Our own 42,000 sq ft workshop, with a full dry-fit before anything ships.'),
       ('i-target', 'Brand-focused layouts', 'Sightlines, headlines and hero moments planned for how people actually walk a hall.'),
       ('i-clock', 'On-time set-up', 'A critical-path schedule, tracked weekly, with contingency built in.'),
       ('i-globe', 'Multi-location support', 'Partner crews in North America, Europe and the Middle East, supervised by us.'),
       ('i-briefcase', 'Professional project management', 'One accountable manager, one budget report, no last-minute surprises.')]


def home1():
    feat = [PN[i] for i in (1, 5, 3, 7, 2, 10)]
    chips = [('all', 'All'), ('custom-booth', 'Custom'), ('rental', 'Rental'), ('island-booth', 'Island'), ('double-decker', 'Double-Decker'), ('pavilion', 'Pavilions')]
    o = []
    o.append('''<section class="hero on-dark blueprint" aria-labelledby="hero-title"><div class="container hero__grid"><div class="hero__copy">
<p class="stand-tag"><span>HALL 4</span><span>STAND 4B-212</span><span>40 &times; 30 FT</span></p>
<h1 id="hero-title" class="display">Stand Out <span class="text-accent">Before the Show</span> Even Starts.</h1>
<p class="lead">Custom trade show booths and exhibition stands designed, built, and installed to make your brand impossible to overlook.</p>
<div class="btn-row">%s%s</div>
<ul class="hero__stats"><li><strong>600+</strong><span>Stands delivered</span></li><li><strong>24</strong><span>Countries built in</span></li><li><strong>96%%</strong><span>On-time installs</span></li><li><strong>15 yrs</strong><span>Exhibition experience</span></li></ul></div>
<div class="hero__visual">%s<ul class="spec-tags" aria-hidden="true"><li class="spec-tag spec-tag--1"><b>01</b>Illuminated ceiling canopy</li><li class="spec-tag spec-tag--2"><b>02</b>Lounge &amp; hospitality bar</li><li class="spec-tag spec-tag--3"><b>03</b>Open-sided island layout</li></ul></div></div>
<div class="ticker" aria-hidden="true"><div class="ticker__track"><span>Island booths</span><span>Peninsula booths</span><span>Inline stands</span><span>Modular systems</span><span>Double-deckers</span><span>Custom pavilions</span><span>Rental stands</span><span>Island booths</span><span>Peninsula booths</span><span>Inline stands</span><span>Modular systems</span><span>Double-deckers</span><span>Custom pavilions</span><span>Rental stands</span></div></div></section>'''
             % (btn('Request a Project Quote', 'contact.html#enquiry'), btn('View Our Portfolio', 'portfolio.html', 'btn--outline-light'),
                img('hero-booth', 'Isometric render of a custom island exhibition stand with a hanging sign, LED wall and product tower', 1200, 900, eager=True)))
    # portfolio
    o.append('<section class="section" id="portfolio" aria-labelledby="pf-title"><div class="container" data-portfolio>')
    o.append(section_head('Featured portfolio', 'Booths people remember.', 'Six recent builds from trade shows across North America and Europe.', btn('Full Portfolio', 'portfolio.html', 'btn--dark'), '01').replace('<h2 class="section-title">', '<h2 class="section-title" id="pf-title">'))
    o.append('<div class="chips" role="group" aria-label="Filter featured projects">%s</div>' % ''.join('<button class="chip" type="button" data-filter="%s" aria-pressed="%s">%s</button>' % (v, 'true' if v == 'all' else 'false', l) for v, l in chips))
    o.append('<p class="sr-only" role="status" aria-live="polite" data-result-count></p><div class="pgrid pgrid--feature" data-grid>')
    for i, p in enumerate(feat):
        o.append(pcard(p, 'pcard--feature' if i == 0 else ''))
    o.append('</div><p class="empty" data-empty hidden>No featured projects in this category. <a href="portfolio.html">Browse the full portfolio</a>.</p></div></section>')
    # services
    o.append('<section class="section section--alt" aria-labelledby="sv-title"><div class="container">%s<div class="svc-grid">%s</div></div></section>'
             % (section_head('What we offer', 'Everything from first sketch to final strike.', 'Eight services that work on their own or as one managed programme.', btn('All Services', 'services.html', 'btn--dark'), '02').replace('<h2 class="section-title">', '<h2 class="section-title" id="sv-title">'),
                ''.join(svc_card(s) for s in SERVICES)))
    # why
    o.append('<section class="section on-dark why" aria-labelledby="why-title"><div class="container why__grid"><div class="why__intro reveal">%s<h2 id="why-title" class="section-title">Why exhibitors choose Standform.</h2><p class="lead">We are a design and build studio, not a print shop with a sales team. That shows in the details clients notice on show day.</p>%s</div><ul class="why__list">' % (eyebrow('Why choose us', '03'), btn('Meet the Team', 'about.html', 'btn--outline-light')))
    for i, (icn, t, d) in enumerate(WHY):
        o.append('<li class="why__item reveal"><span class="why__num">%02d</span>%s<h3>%s</h3><p>%s</p></li>' % (i + 1, ic(icn[2:]), t, d))
    o.append('</ul></div></section>')
    # booth styles
    bt = [BOOTH_TYPES[i] for i in (0, 1, 2, 4, 5, 6)]
    o.append('<section class="section" aria-labelledby="bt-title"><div class="container">%s<div class="plan-grid">%s</div></div></section>'
             % (section_head('Booth design styles', 'Pick a footprint. We\'ll shape the story.', 'Six core configurations, each with its own sightlines, open sides and strengths.', btn('Compare All Types', 'booth-types.html', 'btn--dark'), '04').replace('<h2 class="section-title">', '<h2 class="section-title" id="bt-title">'),
                ''.join(plan_card(b) for b in bt)))
    # process preview
    steps = [('Discover', 'process-01', 'Goals, audience, hall and budget.'), ('Design', 'process-03', '3D renders and drawings you can approve.'), ('Build', 'process-05', 'Workshop fabrication and dry-fit.'),
             ('Install', 'process-08', 'Supervised set-up on the show floor.'), ('Deliver', 'process-09', 'Show support, strike and reuse.')]
    o.append('<section class="section section--alt" aria-labelledby="pr-title"><div class="container">%s<ol class="steps">%s</ol></div></section>'
             % (section_head('How we work', 'Five steps from brief to show floor.', 'A clear, predictable process with named owners at every stage.', btn('Explore Our Process', 'process.html', 'btn--dark'), '05').replace('<h2 class="section-title">', '<h2 class="section-title" id="pr-title">'),
                ''.join('<li class="step reveal"><span class="step__num">%02d</span>%s<h3>%s</h3><p>%s</p></li>' % (i + 1, img(im, n + ' stage illustration', 400, 300), n, d) for i, (n, im, d) in enumerate(steps))))
    # testimonials
    o.append('<section class="section" aria-labelledby="ts-title"><div class="container">%s<div class="quotes">%s%s%s</div><p class="note">Client quotes are demo content for this template.</p></div></section>'
             % (section_head('Trusted by exhibitors', 'What clients say after the show.', None, None, '06').replace('<h2 class="section-title">', '<h2 class="section-title" id="ts-title">'),
                testimonial(TESTIMONIALS[0], True), testimonial(TESTIMONIALS[1]), testimonial(TESTIMONIALS[2])))
    o.append(cta_band('Planning Your Next Exhibition?', 'Tell us your booth size, event, and vision. We\'ll turn it into a space your audience remembers.', ('Start Your Project', 'contact.html#enquiry'), ('Call ' + SITE['phone'], 'tel:' + SITE['phone_raw'])))
    return '\n'.join(o)


def home2():
    o = []
    rail = [('featured', 'Featured'), ('industries', 'Industries'), ('booth-types', 'Booth types'), ('capabilities', 'Capabilities'), ('selected-work', 'Selected work'), ('process', 'Process'), ('enquiry', 'Enquiry')]
    o.append('<aside class="rail" aria-label="Page sections" data-rail><ol>%s</ol><span class="rail__bar" aria-hidden="true"><i data-rail-progress></i></span></aside>'
             % ''.join('<li><a href="#%s"><span class="rail__n">%02d</span><span class="rail__l">%s</span></a></li>' % (h, i + 1, l) for i, (h, l) in enumerate(rail)))
    o.append('''<section class="cs-hero on-dark" aria-labelledby="cs-title">%s<div class="cs-hero__shade"></div><div class="container cs-hero__inner">
<p class="cs-hero__tag">Case study 01 <span>/</span> 12 &middot; NovaTech &middot; TechForward Expo 2025</p>
<div class="cs-hero__grid"><div><h1 id="cs-title" class="display">Your Brand. <span class="text-accent">Your Space.</span> Your Moment.</h1>
<div class="btn-row">%s%s</div></div>
<aside class="spec-sheet" aria-label="Project specifications"><h2 class="spec-sheet__title">Project sheet</h2><dl><div><dt>Client</dt><dd>NovaTech Systems</dd></div><div><dt>Booth</dt><dd>Custom island</dd></div><div><dt>Size</dt><dd>40 &times; 30 ft</dd></div><div><dt>Build</dt><dd>14 modules</dd></div><div><dt>Install</dt><dd>3 days</dd></div></dl><a class="link-arrow" href="portfolio-details.html?project=novatech-island-booth"><span>Read the case study</span>%s</a></aside></div></div></section>'''
             % (img('case-study-hero', 'NovaTech custom island booth render under a ring truss', 1600, 900, 'cs-hero__img', eager=True),
                btn('Request a Project Quote', 'contact.html#enquiry'), btn('View Our Portfolio', 'portfolio.html', 'btn--outline-light'), ic('arrow')))
    # story
    nv = P['novatech-island-booth']
    o.append('<section class="story" id="featured" aria-labelledby="story-title"><div class="container"><div class="story__head reveal">%s<h2 id="story-title" class="section-title">One island. Three zones. Six aisles of attention.</h2></div><div class="story__grid"><div class="story__stage" data-story-stage>' % eyebrow('Featured project', '01'))
    o.append(frame('%s%s%s' % (img('project-01', 'NovaTech booth render', 800, 600, 'is-on'), img('plan-island', 'NovaTech island floor plan', 600, 450), img('hero-booth', 'NovaTech booth detail', 1200, 900)), 'story__frame'))
    o.append('<p class="story__cap" aria-hidden="true"><span data-story-cap>Perspective render</span></p></div><ol class="story__steps">')
    for i, (t, d, m) in enumerate((('The brief', nv['challenge'], 'Client: NovaTech Systems'), ('The concept', nv['solution'], 'Footprint: 1,200 sq ft'),
                                   ('The build', nv['construction'] + ' ' + nv['install'], 'Crew: 6 &middot; 3 days'), ('The result', 'The stand delivered ' + nv['results'][0][0] + ' badge scans, ' + nv['results'][1][0] + ' booked meetings and a hall inspection with nothing to fix.', 'Results reported by client'))):
        o.append('<li class="story__step reveal" data-story-step data-img="%d" data-cap="%s"><p class="story__n">%02d</p><h3>%s</h3><p>%s</p><p class="story__meta">%s</p></li>' % (min(i, 2), ['Perspective render', 'Floor plan', 'Detail view'][min(i, 2)], i + 1, t, d, m))
    o.append('</ol></div></div></section>')
    # industries
    cnt = {}
    for p in PROJECTS:
        cnt[p['industry']] = cnt.get(p['industry'], 0) + 1
    o.append('<section class="section section--alt" id="industries" aria-labelledby="ind-title"><div class="container">%s<ul class="ind-list">%s</ul></div></section>'
             % (section_head('Industries we serve', 'Built for how your industry shows up.', 'Each sector has its own rules, audiences and hall culture. We know them.', None, '02').replace('<h2 class="section-title">', '<h2 class="section-title" id="ind-title">'),
                ''.join('<li class="reveal"><a class="ind-row" href="portfolio.html?industry=%s"><span class="ind-row__n">%02d</span><span class="ind-row__name">%s</span><span class="ind-row__count">%d project%s</span>%s</a></li>' % (v, i + 1, l, cnt.get(v, 0), '' if cnt.get(v, 0) == 1 else 's', ic('arrow-up-right')) for i, (v, l) in enumerate(INDUSTRIES))))
    # booth types strip
    o.append('<section class="section" id="booth-types" aria-labelledby="bty-title"><div class="container">%s</div><div class="hstrip" tabindex="0" role="region" aria-label="Booth types, scroll horizontally"><ul class="hstrip__track">%s</ul></div></section>'
             % (section_head('Booth types', 'Eight footprints. Endless compositions.', 'Scroll through the configurations we build most often.', btn('Compare in Detail', 'booth-types.html', 'btn--dark'), '03').replace('<h2 class="section-title">', '<h2 class="section-title" id="bty-title">'),
                ''.join('<li>%s</li>' % plan_card(b) for b in BOOTH_TYPES)))
    # capabilities
    caps = [('i-cube', '3D design & rendering', 'Photo-real models, walkthroughs and technical drawings in-house.', '2 render angles, standard'),
            ('i-ruler', 'Structural engineering', 'Certified drawings for decks, hanging signs and double-deckers.', 'Load-tested to hall rules'),
            ('i-hammer', 'CNC & carpentry', 'Joinery, curved forms and lacquer finishing in our own workshop.', '42,000 sq ft workshop'),
            ('i-layers', 'Metal fabrication', 'Aluminium and steel frames, trusses and feature structures.', 'Powder-coat on site'),
            ('i-printer', 'Large-format graphics', 'SEG fabric, backlit film and rigid substrates, colour-proofed.', 'Up to 5 m wide'),
            ('i-bulb', 'Lighting & AV', 'Lighting design, LED walls, control and certified power.', 'Hall-compliant plans')]
    o.append('<section class="section on-dark" id="capabilities" aria-labelledby="cap-title"><div class="container">%s<ul class="cap-grid">%s</ul></div></section>'
             % (section_head('Design capabilities', 'Everything under one roof, so nothing gets lost.', None, None, '04').replace('<h2 class="section-title">', '<h2 class="section-title" id="cap-title">'),
                ''.join('<li class="cap reveal">%s<h3>%s</h3><p>%s</p><p class="cap__spec">%s</p></li>' % (ic(i[2:]), t, d, s) for i, t, d, s in caps)))
    # selected work bento
    sel = [PN[i] for i in (6, 8, 11, 4, 12, 9)]
    o.append('<section class="section" id="selected-work" aria-labelledby="sw-title"><div class="container">%s<ul class="bento">' % section_head('Selected work', 'More from the show floor.', None, btn('Full Portfolio', 'portfolio.html', 'btn--dark'), '05').replace('<h2 class="section-title">', '<h2 class="section-title" id="sw-title">'))
    for i, p in enumerate(sel):
        o.append('<li class="bento__item bento__item--%d reveal"><a href="portfolio-details.html?project=%s">%s<span class="bento__cap"><span class="bento__t">%s</span><span class="bento__m">%s &middot; %s</span></span></a></li>' % (i + 1, p['slug'], img(p['img'], p['title'] + ' render', 800, 600), p['title'], p['typeLabel'], p['size']))
    o.append('</ul></div></section>')
    # process
    pr = [('Discover', 'We define the goals, audience, hall and budget together.'), ('Design', 'Concepts, 3D renders and drawings you approve before we build.'), ('Build', 'Fabrication, graphics and a full dry-fit in our workshop.'),
          ('Install', 'Supervised installation and hall sign-off on site.'), ('Deliver', 'Show support, strike, reuse and a post-show review.')]
    o.append('<section class="section section--alt" id="process" aria-labelledby="prc-title"><div class="container">%s<ol class="big-steps">%s</ol></div></section>'
             % (section_head('Our process', 'A calm route to a loud stand.', None, btn('Full Process', 'process.html', 'btn--dark'), '06').replace('<h2 class="section-title">', '<h2 class="section-title" id="prc-title">'),
                ''.join('<li class="big-step reveal"><span class="big-step__n">%02d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, t, d) for i, (t, d) in enumerate(pr))))
    # enquiry
    o.append('''<section class="section on-dark enquiry" id="enquiry" aria-labelledby="enq-title"><div class="container enquiry__grid"><div class="reveal">%s<h2 id="enq-title" class="section-title">Tell us about your next show.</h2><p class="lead">Share a few details and we will reply within one working day with questions, ideas and a next step.</p>
<ul class="contact-list"><li>%s<a href="tel:%s">%s</a></li><li>%s<a href="mailto:%s">%s</a></li><li>%s%s</li></ul>
<div class="enquiry__call"><p><strong>Prefer to talk first?</strong> Book a 30-minute discovery call and walk away with a first layout idea, a rough range and a schedule.</p>
<!-- TODO: calendar integration point: point data-booking-url (and the href) at your Calendly / Cal.com / Google appointment page -->
<a class="btn btn--light" href="contact.html#enquiry" data-booking-link data-booking-url="YOUR_BOOKING_URL">Book a Discovery Call</a></div></div>
<form class="card-form" data-validate data-demo novalidate aria-labelledby="enq-title"><div class="form-grid">%s%s%s%s</div><div class="form-alert" role="alert" data-error hidden></div><p class="form-status" role="status" aria-live="polite" data-status></p><button class="btn btn--accent btn--lg btn--block" type="submit"><span>Start Your Project</span>%s</button>
<p class="form-note">Demo form: nothing is sent until you connect an endpoint.</p></form></div></section>'''
             % (eyebrow('Project enquiry', '07'), ic('phone'), SITE['phone_raw'], SITE['phone'], ic('mail'), SITE['email'], SITE['email'], ic('pin'), SITE['address'],
                field('h2-name', 'Full name', ac='name', ph='Jane Cooper'), field('h2-email', 'Work email', 'email', ac='email', ph='jane@company.com'),
                field('h2-event', 'Event name', ph='e.g. TechForward Expo 2027'),
                select('h2-size', 'Booth size', [('10x10', '10 × 10 ft'), ('10x20', '10 × 20 ft'), ('20x20', '20 × 20 ft'), ('30x30', '30 × 30 ft'), ('40x40', '40 × 40 ft +')]), ic('arrow')))
    return '\n'.join(o)


def about():
    o = []
    o.append(page_hero([('About', None)], 'About Standform', 'We design and build the stands behind great shows.',
                       'Standform is a Chicago exhibition studio. Designers, fabricators and installers working as one team since 2011.',
                       frame(img('project-03', 'Meridian Health pavilion render', 800, 600, eager=True)), btn('Meet the Team', '#team', 'btn--accent') + btn('View Our Portfolio', 'portfolio.html', 'btn--outline-light')))
    o.append('<section class="section" aria-labelledby="intro-title"><div class="container split"><div class="split__text reveal">%s<h2 id="intro-title" class="section-title">A studio that builds what it draws.</h2><p class="lead">We started in a 2,000 sq ft workshop building stands for two clients. Today we run a 42,000 sq ft fabrication facility, an in-house graphics studio and crews that install in more than 60 venues.</p><p>Most exhibition companies are either designers who subcontract the build or builders who subcontract the design. We do both under one roof, which is why our stands look like the renders and go up on time.</p></div>'
             '<div class="stats reveal"><div><strong data-count="15">15</strong><span>Years in exhibitions</span></div><div><strong data-count="600" data-suffix="+">600+</strong><span>Stands delivered</span></div><div><strong data-count="42" data-suffix="k">42k</strong><span>Sq ft workshop</span></div><div><strong data-count="60" data-suffix="+">60+</strong><span>Venues installed in</span></div></div></div></section>' % eyebrow('Company introduction', '01'))
    o.append('<section class="section section--alt" aria-labelledby="mv-title"><div class="container"><h2 id="mv-title" class="sr-only">Mission and vision</h2><div class="mv"><article class="mv__card mv__card--dark reveal">%s<h3>Our mission</h3><p>To give every exhibitor, from a five-person start-up to a global brand, a stand that makes the business case for showing up.</p></article><article class="mv__card mv__card--accent reveal">%s<h3>Our vision</h3><p>A trade show floor where structures are reused instead of thrown away, and design quality does not depend on budget size.</p></article></div></div></section>' % (ic('target'), ic('compass')))
    tl = [('2011', 'Founded', 'Elena Marsh opens a two-bench workshop in Chicago and builds the first two stands.'), ('2014', 'First international island', 'Our first 40 × 40 ft island opens in Frankfurt.'), ('2017', 'New workshop', 'Move to a 42,000 sq ft facility with CNC and paint.'),
          ('2020', 'Rental system', 'We launch our engineered rental panel and frame range.'), ('2023', 'Circular build programme', 'Reuse tracking on every project; 80% average return to stock.'), ('2025', '600th stand', 'Milestone stand delivered for a healthcare client in Boston.')]
    o.append('<section class="section" aria-labelledby="hist-title"><div class="container">%s<ol class="timeline-h">%s</ol></div></section>' % (section_head('Our history', 'Fifteen years, six turning points.', None, None, '02').replace('<h2 class="section-title">', '<h2 class="section-title" id="hist-title">'),
                                                                                                                              ''.join('<li class="reveal"><span class="timeline-h__year">%s</span><h3>%s</h3><p>%s</p></li>' % t for t in tl)))
    ex = [('i-cube', 'Exhibition design'), ('i-hammer', 'Custom fabrication'), ('i-layers', 'Modular & rental systems'), ('i-printer', 'Large-format graphics'), ('i-bulb', 'Lighting & AV'), ('i-truck', 'Logistics & install')]
    o.append('<section class="section on-dark" aria-labelledby="ex-title"><div class="container">%s<ul class="cap-grid cap-grid--tight">%s</ul></div></section>' % (section_head('Expertise', 'Six disciplines, one accountable team.', None, None, '03').replace('<h2 class="section-title">', '<h2 class="section-title" id="ex-title">'),
                                                                                                                                                      ''.join('<li class="cap reveal">%s<h3>%s</h3></li>' % (ic(i[2:]), t) for i, t in ex)))
    ph = [('Design for the aisle', 'A stand is judged from 20 feet in three seconds. We design that view first.'), ('Build to be reused', 'Structures should outlive a single show. We specify systems that reconfigure.'),
          ('Light is a material', 'We budget for lighting like we budget for walls, because it does the same job.'), ('Plan the strike on day one', 'How a stand comes down decides how many shows it will go to.')]
    o.append('<section class="section" aria-labelledby="ph-title"><div class="container">%s<ol class="principles">%s</ol></div></section>' % (section_head('Design philosophy', 'Four principles we do not compromise on.', None, None, '04').replace('<h2 class="section-title">', '<h2 class="section-title" id="ph-title">'),
                                                                                                                                   ''.join('<li class="principle reveal"><span class="principle__n">%02d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i + 1, t, d) for i, (t, d) in enumerate(ph))))
    o.append('<section class="section section--alt" id="team" aria-labelledby="team-title"><div class="container">%s<ul class="team">%s</ul></div></section>' % (section_head('The team', 'The people you will actually work with.', None, None, '05').replace('<h2 class="section-title">', '<h2 class="section-title" id="team-title">'),
                                                                                                                                                              ''.join('<li class="member reveal"><span class="member__avatar" aria-hidden="true">%s</span><h3>%s</h3><p>%s</p></li>' % (i, n, r) for n, r, i in TEAM)))
    why = ['One team from concept to strike', 'Fixed-scope quotes with itemised hall costs', 'Weekly written status updates', 'A full dry-fit before shipping', 'Reusable structures and honest reuse tracking', 'A named supervisor on your show floor']
    o.append('<section class="section" aria-labelledby="wc-title"><div class="container split"><div class="reveal">%s<h2 id="wc-title" class="section-title">Why clients work with us.</h2><ul class="checklist">%s</ul></div><div class="quotes quotes--stack">%s%s</div></div></section>'
             % (eyebrow('Why Standform', '06'), ''.join('<li>%s<span>%s</span></li>' % (ic('check'), w) for w in why), testimonial(TESTIMONIALS[3]), testimonial(TESTIMONIALS[2])))
    o.append(cta_band('Let\'s build something worth walking toward.', 'Send us the show, the footprint and the goal. We\'ll send back a plan.', ('Discuss Your Project', 'contact.html#enquiry'), ('See Our Portfolio', 'portfolio.html')))
    return '\n'.join(o)


def services():
    o = [page_hero([('Services', None)], 'Services', 'Eight services. One accountable team.',
                   'Use us for a single discipline or hand over the whole exhibition programme. Every service is delivered by our own people, not a network of subcontractors.',
                   frame(img('process-05', 'Workshop router shaping a timber stand component', 640, 480, eager=True)), btn('Request a Project Quote', 'contact.html#enquiry') + btn('See Pricing', 'pricing.html', 'btn--outline-light'))]
    o.append('<section class="section" aria-labelledby="sl-title"><div class="container"><h2 id="sl-title" class="sr-only">All services</h2><ol class="svc-rows">')
    for s in SERVICES:
        o.append('<li class="svc-row reveal"><a class="svc-row__media" href="service-details.html?service=%s" tabindex="-1" aria-hidden="true">%s</a><div class="svc-row__body"><p class="svc-row__n">%02d</p><h3>%s</h3><p>%s</p><ul class="chips-list">%s</ul><a class="btn btn--dark btn--sm" href="service-details.html?service=%s"><span>View Details</span>%s<span class="sr-only"> for %s</span></a></div></li>'
                 % (s['slug'], img(s['img'], s['title'] + ' illustration', 640, 480, sizes='(min-width:1024px) 50vw, 100vw'), s['n'], s['title'], esc(s['desc']), ''.join('<li>%s</li>' % b for b in s['benefits']), s['slug'], ic('arrow'), s['title']))
    o.append('</ol></div></section>')
    o.append('<section class="section section--alt" aria-labelledby="ns-title"><div class="container next-steps"><div class="reveal">%s<h2 id="ns-title" class="section-title">Not sure where to start?</h2><p class="lead">Compare booth footprints, see what drives cost, or run a quick estimate. Then talk to a designer.</p></div><ul class="next-steps__list reveal"><li><a href="booth-types.html">%s<span>Compare booth types</span>%s</a></li><li><a href="pricing.html#estimator">%s<span>Estimate your project</span>%s</a></li><li><a href="process.html">%s<span>See how we work</span>%s</a></li></ul></div></section>'
             % (eyebrow('Next steps'), ic('grid'), ic('arrow'), ic('chart'), ic('arrow'), ic('clipboard'), ic('arrow')))
    o.append(cta_band('Have a show coming up?', 'Send us the date, the hall and the footprint. We\'ll tell you what is possible.', ('Request a Project Quote', 'contact.html#enquiry'), ('Ask a question', 'tel:' + SITE['phone_raw'])))
    return '\n'.join(o)


def service_details():
    s = SERVICES[0]
    o = []
    o.append('<section class="page-hero on-dark blueprint" aria-labelledby="svc-title"><div class="container page-hero__inner"><div class="page-hero__text">%s%s<h1 id="svc-title" class="page-title" data-svc="title">%s</h1><p class="lead" data-svc="tagline">%s</p><div class="btn-row">%s%s</div></div><div class="page-hero__art">%s</div></div></section>'
             % (crumbs([('Services', 'services.html'), ('Service details', None)]), eyebrow('Service <span data-svc="num">01</span> of 08'), s['title'], s['tagline'], btn('Request a Quote', 'contact.html#enquiry'), btn('All Services', 'services.html', 'btn--outline-light'), frame(img(s['img'], s['title'] + ' illustration', 640, 480, 'svc-hero-img', eager=True))))
    o.append('<section class="section"><div class="container detail"><div class="detail__main">')
    o.append('<section id="overview" class="block reveal" aria-labelledby="ov-t"><h2 id="ov-t">Overview</h2><p class="lead" data-svc="overview">%s</p></section>' % s['overview'])
    o.append('<section id="included" class="block reveal" aria-labelledby="in-t"><h2 id="in-t">What is included</h2><ul class="checklist checklist--2" data-svc-list="includes">%s</ul></section>' % ''.join('<li>%s<span>%s</span></li>' % (ic('check'), i) for i in s['includes']))
    o.append('<section id="benefits" class="block reveal" aria-labelledby="be-t"><h2 id="be-t">Benefits</h2><ul class="benefit-grid" data-svc-list="benefits">%s</ul></section>' % ''.join('<li>%s<h3>%s</h3></li>' % (ic('star'), b) for b in s['benefits']))
    o.append('<section id="deliverables" class="block reveal" aria-labelledby="de-t"><h2 id="de-t">Deliverables</h2><ul class="doc-list" data-svc-list="deliverables">%s</ul></section>' % ''.join('<li>%s<span>%s</span></li>' % (ic('file'), d) for d in s['deliverables']))
    o.append('<section id="approach" class="block reveal" aria-labelledby="ap-t"><h2 id="ap-t">Our design approach</h2><div class="tabs" data-tabs><div class="tabs__list" role="tablist" aria-label="Design approach"><button class="tabs__tab" role="tab" id="tab-1" aria-controls="panel-1" aria-selected="true" type="button">Listen</button><button class="tabs__tab" role="tab" id="tab-2" aria-controls="panel-2" aria-selected="false" tabindex="-1" type="button">Shape</button><button class="tabs__tab" role="tab" id="tab-3" aria-controls="panel-3" aria-selected="false" tabindex="-1" type="button">Test</button></div>'
             '<div class="tabs__panel" role="tabpanel" id="panel-1" aria-labelledby="tab-1"><p>We begin with your goals and your visitors: who should stop, what should they do, and what will they remember. We review hall rules, sightlines and traffic before anything is drawn.</p></div>'
             '<div class="tabs__panel" role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden><p>Two concept routes take shape as plans and quick 3D massing models. You compare them against your goals, not against taste alone.</p></div>'
             '<div class="tabs__panel" role="tabpanel" id="panel-3" aria-labelledby="tab-3" hidden><p>The chosen route is tested for visitor flow, sightlines, power, structure and budget, then locked into a fixed-scope drawing pack.</p></div></div></section>')
    o.append('<section id="process" class="block reveal" aria-labelledby="pc-t"><h2 id="pc-t">How it works</h2><ol class="mini-steps">%s</ol></section>' % ''.join('<li><span>%02d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i + 1, PROCESS[i][0], PROCESS[i][1]) for i in range(5)))
    pr = s['price']
    o.append('<section id="pricing" class="block reveal" aria-labelledby="pp-t"><h2 id="pp-t">Pricing &amp; quote information</h2><p data-svc="priceNote">%s</p><div class="table-wrap" tabindex="0" role="region" aria-label="Pricing table"><table class="table"><caption class="sr-only">Indicative pricing for this service</caption><thead><tr><th scope="col">Option</th><th scope="col">Indicative price</th></tr></thead><tbody data-svc-rows>%s</tbody></table></div><p class="note">Demonstration pricing only. Final quotes depend on show, footprint and scope. <a href="pricing.html#estimator">Try the estimator</a>.</p></section>'
             % (pr[1], ''.join('<tr><th scope="row">%s</th><td>%s</td></tr>' % r for r in pr[2])))
    o.append('<section id="faq" class="block reveal" aria-labelledby="fq-t"><h2 id="fq-t">Frequently asked questions</h2><div class="accordion" data-accordion>%s</div></section>' % ''.join(
        '<div class="accordion__item"><h3><button class="accordion__btn" type="button" aria-expanded="%s" aria-controls="faq-%d" id="faq-b%d"><span>%s</span>%s</button></h3><div class="accordion__panel" id="faq-%d" role="region" aria-labelledby="faq-b%d"%s><div><p>%s</p></div></div></div>'
        % ('true' if i == 0 else 'false', i, i, q, ic('plus'), i, i, '' if i == 0 else ' hidden', a) for i, (q, a) in enumerate(FAQ)))
    o.append('<section id="related" class="block" aria-labelledby="rl-t"><h2 id="rl-t">Related services</h2><div class="svc-grid svc-grid--3" data-related>%s</div></section>' % ''.join(svc_card(x) for x in (SERVICES[1], SERVICES[5], SERVICES[7])))
    o.append('</div><aside class="detail__side" aria-label="Quote and service navigation"><div class="side-card"><p class="side-card__k">Starting from</p><p class="side-card__price" data-svc="priceLabel">%s</p><p class="side-card__n">Indicative. Final quote follows a short discovery call.</p>%s<a class="side-card__phone" href="tel:%s">%s%s</a></div>'
             '<nav class="side-nav" aria-label="On this page"><h2>On this page</h2><ul><li><a href="#overview">Overview</a></li><li><a href="#included">What is included</a></li><li><a href="#benefits">Benefits</a></li><li><a href="#deliverables">Deliverables</a></li><li><a href="#approach">Design approach</a></li><li><a href="#pricing">Pricing</a></li><li><a href="#faq">FAQ</a></li></ul></nav></aside></div></section>'
             % (pr[0], btn('Request a Quote', 'contact.html#enquiry', 'btn--accent btn--block'), SITE['phone_raw'], ic('phone'), SITE['phone']))
    o.append(cta_band('Get a scoped range before you commit budget.', 'Send us your show and footprint. We\'ll come back with questions, options and a rough range.', ('Request a Project Quote', 'contact.html#enquiry'), ('View Pricing', 'pricing.html')))
    return '\n'.join(o)

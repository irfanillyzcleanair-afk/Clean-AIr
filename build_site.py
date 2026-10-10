import argparse
import html
import hashlib
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument('--base-url', required=True)
parser.add_argument('--mode', choices=['demo', 'production'], default='demo')
args = parser.parse_args()
BASE = args.base_url.rstrip('/')
DEMO = args.mode == 'demo'
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
ASSETS = '/assets/'
CSS_VERSION = hashlib.sha256((DIST / 'assets' / 'site.css').read_bytes()).hexdigest()[:12]
JS_VERSION = hashlib.sha256((DIST / 'assets' / 'site.js').read_bytes()).hexdigest()[:12]
PHONE = '+971504616073'
PHONE_SECONDARY = '+971501046233'
WHATSAPP = '971501169833'

def esc(value):
    return html.escape(str(value), quote=True)

def icon(name='arrow', size=24):
    paths = {
      'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
      'arrow-up': '<path d="M7 17 17 7M7 7h10v10"/>',
      'check': '<path d="m5 12 4 4L19 6"/>',
      'air': '<path d="M3 8h12a3 3 0 1 0-3-3M3 12h16a3 3 0 1 1-3 3M3 16h6"/>',
      'car': '<path d="m5 8 2-4h10l2 4M3 9h18v9H3zM6 18v2m12-2v2M6 13h2m8 0h2"/>',
      'home': '<path d="m3 10 9-7 9 7M5 9v12h14V9M9 21v-8h6v8"/>',
      'building': '<path d="M5 21V3h14v18M9 7h1m4 0h1M9 11h1m4 0h1M9 15h1m4 0h1M3 21h18"/>',
      'monitor': '<path d="M3 4h18v13H3zM8 21h8m-4-4v4M6 11h3l2-4 2 7 2-3h3"/>',
      'light': '<path d="M9 18h6m-5 3h4M8 14a6 6 0 1 1 8 0l-1 2H9z"/>',
      'layers': '<path d="m12 3 10 5-10 5L2 8zM2 12l10 5 10-5M2 16l10 5 10-5"/>',
      'chat': '<path d="M21 11a8 8 0 0 1-8 8H8l-5 3 1-6a8 8 0 1 1 17-5zM8 10h8m-8 4h5"/>',
      'mail': '<path d="M3 5h18v14H3zM3 5l9 8 9-8"/>',
      'pin': '<path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 0 1 14 0z"/><circle cx="12" cy="10" r="2"/>',
      'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    }
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths.get(name, paths["arrow"])}</svg>'

PRODUCTS = [
 dict(slug='ductfit-s', name='ductFIT S', category='Portable purification', tag='Cars & personal spaces', group='cars', image='ductfit-s.png',
      title='Car Air Purifier Dubai | ductFIT S | CleanAir',
      desc='Explore ductFIT S, a portable air purifier for cars and small personal spaces. Ask CleanAir in Dubai about compatibility and a quotation.',
      headline='Cleaner air, wherever you go.',
      intro='A compact ductFIT air purification device for cars and small personal spaces. Its portable format brings the range into your everyday journey.',
      bullets=['Portable format for cars and personal spaces', 'Built-in fan for air circulation', 'Photocatalytic oxidation technology'],
      applications=['Cars', 'Study spaces', 'Travel and hotel stays'],
      considerations=['Vehicle power connection and compatibility', 'Space suitability and placement', 'Model-specific care and maintenance']),
 dict(slug='ductfit-mobile', name='ductFIT Mobile', category='Standalone purification', tag='Homes & offices', group='rooms', image='ductfit-mobile.png',
      title='Standalone Air Purifier UAE | ductFIT Mobile | CleanAir',
      desc='Discover ductFIT Mobile, a standalone air purification unit for spaces without ductwork. Explore options for homes and offices in Dubai and the UAE.',
      headline='A standalone solution for your space.',
      intro='Bring ductFIT air purification into rooms without installing a unit inside HVAC ducts. A built-in fan circulates air through the standalone system.',
      bullets=['Standalone operation without duct installation', 'Built-in fan for air circulation', 'Suitable for discussing home and office applications'],
      applications=['Homes', 'Offices', 'Rooms without air ducts'],
      considerations=['Room size and ventilation', 'Placement and power availability', 'Applicable filtration stages and maintenance']),
 dict(slug='ductfit-vent', name='ductFIT Vent', category='HVAC purification', tag='Buildings & duct systems', group='buildings', image='ductfit-vent.png',
      title='HVAC Air Purification UAE | ductFIT Vent | CleanAir',
      desc='Explore ductFIT Vent for air treatment within HVAC ducts. Ask CleanAir about installation requirements and a quotation for your UAE building.',
      headline='Air treatment, integrated into your building.',
      intro='A duct-integrated solution for buildings with HVAC systems. ductFIT Vent is designed for installation inside ducts or plenums, using the system’s existing airflow.',
      bullets=['Designed for HVAC ducts and plenums', 'Integrated rather than a standalone room unit', 'Photocatalytic oxidation technology'],
      applications=['Commercial buildings', 'Offices and hospitality', 'Properties with HVAC duct systems'],
      considerations=['Duct layout and available installation space', 'HVAC airflow and operating conditions', 'Unit selection and maintenance access']),
 dict(slug='ductfit-kleansense-iaq-sensor', name='KleanSense IAQ Sensor', category='Air quality monitoring', tag='Measure your indoor air', group='monitoring', image='ductfit-kleansense-iaq-sensor.png',
      title='Indoor Air Quality Monitor UAE | KleanSense | CleanAir',
      desc='Explore KleanSense IAQ monitoring for PM2.5, TVOC, CO2 and other indoor readings. Ask CleanAir about sensor, software and connectivity options in the UAE.',
      headline='Understand the air in your room.',
      intro='Measure indoor air quality in real time with KleanSense. See environmental readings and trends to support more informed decisions about your space.',
      bullets=['Eight indoor environmental readings', 'Real-time monitoring and data reports', 'Wi-Fi connectivity; other options depend on configuration'],
      applications=['Offices', 'Homes and shared spaces', 'Building monitoring'],
      considerations=['Sensor placement and coverage of the monitoring plan', 'Connectivity and data access', 'Software subscription and reporting requirements']),
 dict(slug='ductfit-wall', name='ductFIT Wall', category='Wall-mounted purification', tag='Rooms without ductwork', group='rooms', image='ductfit-wall.png',
      title='Wall Mounted Air Purifier UAE | ductFIT Wall | CleanAir',
      desc='Explore ductFIT Wall, a wall-mounted purification option with a built-in fan for spaces without ductwork. Ask CleanAir about suitability and installation.',
      headline='A considered fit for your wall.',
      intro='A wall-mounted ductFIT unit for spaces without air ducts. Its built-in fan supports air circulation while keeping the unit away from floor space.',
      bullets=['Wall-mounted configuration', 'Independent of HVAC ductwork', 'Built-in fan for air circulation'],
      applications=['Homes', 'Offices', 'Rooms without ducts'],
      considerations=['Wall location and clearance', 'Room requirements and electrical access', 'Maintenance access and model configuration']),
 dict(slug='ductfit-ceiling', name='ductFIT Ceiling', category='Ceiling and wall purification', tag='Flexible installation', group='rooms', image='ductfit-ceiling.png',
      title='Ceiling Air Purification UAE | ductFIT Ceiling | CleanAir',
      desc='Explore ductFIT Ceiling for spaces without air ducts. Discuss ceiling or wall installation options and product suitability with CleanAir in the UAE.',
      headline='Purification above the everyday.',
      intro='A ductFIT option for spaces without air ducts, with ceiling or wall installation configurations. Our team can help assess the right arrangement for your space.',
      bullets=['Ceiling or wall installation options', 'Designed for spaces without ductwork', 'Configuration matched to the intended space'],
      applications=['Offices', 'Shared indoor spaces', 'Spaces without air ducts'],
      considerations=['Mounting arrangement and support', 'Air circulation and installation layout', 'Power, maintenance access and unit configuration']),
 dict(slug='ductfit-cloud', name='ductFIT Cloud', category='Ceiling-mounted purification', tag='Grid ceiling integration', group='rooms', image='ductfit-cloud.jpeg',
      title='Ceiling Grid Air Purifier UAE | ductFIT Cloud | CleanAir',
      desc='Discover ductFIT Cloud, a ceiling-mounted purification option designed for grid ceiling tiles. Ask CleanAir about installation and your room requirements.',
      headline='Designed to sit within your ceiling.',
      intro='A ceiling-mounted ductFIT system designed to fit into grid ceiling tiles. It operates independently of HVAC ducts and includes a built-in fan.',
      bullets=['Designed for grid ceiling tiles', 'Independent of HVAC duct systems', 'Built-in fan for air circulation'],
      applications=['Offices', 'Commercial rooms', 'Spaces with grid ceilings'],
      considerations=['Ceiling grid dimensions and support', 'Power and maintenance access', 'Room layout and circulation requirements']),
 dict(slug='ductfit-lampshade', name='ductFIT Lampshade', category='Interior-focused purification', tag='A discreet room option', group='rooms', image='ductfit-lampshade.png',
      title='Lampshade Air Purification UAE | ductFIT | CleanAir',
      desc='Explore the lampshade-style ductFIT purification unit for indoor spaces. Ask CleanAir about model suitability, mounting and care in Dubai and the UAE.',
      headline='An air solution that fits the interior.',
      intro='A lampshade-style ductFIT purification unit designed to blend into an indoor setting. Discuss its configuration and placement with our team before selecting a model.',
      bullets=['Lampshade-style format', 'Designed to blend into interiors', 'Part of the ductFIT purification range'],
      applications=['Hospitality interiors', 'Meeting and shared rooms', 'Interior-sensitive spaces'],
      considerations=['Installation and mounting arrangement', 'Placement within the room', 'Model specifications and maintenance']),
 dict(slug='ductfit-m', name='ductFIT M', category='Mobility and transport', tag='HVAC grille retrofit', group='buildings', image='ductfit-m.png',
      title='Transport Air Purification UAE | ductFIT M | CleanAir',
      desc='Explore ductFIT M for HVAC grille retrofit applications in trains, subways and buses. Discuss transport requirements and configuration with CleanAir.',
      headline='Designed for shared journeys.',
      intro='A semi-custom ductFIT purification option developed for mobility environments such as trains, subways and buses. It is intended for retrofit into existing HVAC grille systems.',
      bullets=['Transport and mobility applications', 'Retrofit into HVAC grille systems', 'Semi-custom configuration'],
      applications=['Trains', 'Subways', 'Buses'],
      considerations=['Existing HVAC grille and airflow', 'Vehicle-specific installation constraints', 'Configuration, power and maintenance access']),
]
P = {x['slug']: x for x in PRODUCTS}
P['ductfit-kleansense-iaq-sensor'].update(
    intro='See eight indoor environmental readings with KleanSense. Wi-Fi connectivity brings live data and historical trends into a centralised dashboard, helping you review conditions across your space.',
    bullets=['Eight environmental readings, including PM2.5, TVOC and CO₂', 'Centralised dashboard with live data and historical trends', 'Wi-Fi connectivity for a connected monitoring plan'],
    considerations=['Sensor placement and monitoring locations', 'Wi-Fi, dashboard access and integration requirements', 'Software access, calibration and support terms'],
    reference_intro='A compact connected monitor for viewing indoor conditions and reviewing trends.',
    reference_note='Confirm the sensor variant, dashboard access and calibration plan with your quotation.',
    reference_specs=[('Dimensions','135 × 135 × 40 mm'),('Connectivity','Wi-Fi'),('Dashboard','Live data and historical trends'),('Readings','Eight indoor environmental parameters')])
P['ductfit-vent'].update(
    reference_intro='The details below describe ductFIT Vent 100 in the product brochure. Other Vent models use different configurations.',
    reference_note='Our team confirms the selected model’s data sheet, HVAC suitability and installation requirements.',
    reference_specs=[('Reference model','ductFIT Vent 100'),('Dimensions','29 × 18 × 31 cm (L × W × D)'),('Length inside duct','24 cm'),('Power consumption','Maximum 30 W'),('Status indication','UV bulb monitoring indicator')])
READINGS = [('PM2.5','Fine particles'),('TVOC','Combined organic compounds'),('CO₂','Carbon dioxide'),('CO','Carbon monoxide'),('O₃','Ozone'),('HCHO','Formaldehyde'),('Temperature','Room conditions'),('Humidity','Moisture in the air')]

def image(product, cls='', eager=False):
    width, height = (640,640) if 'kleansense' in product['slug'] else (763,810) if product['slug']=='ductfit-cloud' else (500,500)
    return f'<img class="{cls}" src="{ASSETS}{product["image"]}" alt="{esc(product["name"])} {esc(product["category"].lower())} device" width="{width}" height="{height}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def button(text, href, kind='primary', extra=''):
    return f'<a class="button button-{kind}" href="{href}" {extra}>{text}{icon("arrow",18)}</a>'

def product_card(product):
    path='/products/'+product['slug']+'/'
    return f'<article class="product-card" data-category="{product["group"]}"><a class="product-art" href="{path}" aria-label="Explore {esc(product["name"])}">{image(product)}<span class="art-arrow">{icon("arrow-up",20)}</span></a><div class="product-card-copy"><p class="eyebrow">{product["category"]}</p><h3><a href="{path}">{product["name"]}</a></h3><p>{product["tag"]}</p><a class="text-link" href="{path}">Explore the product {icon("arrow",16)}</a></div></article>'

def breadcrumbs(items):
    labels=[('<a href="/">Home</a>')]
    for name, url in items[:-1]:
        labels.append(f'<a href="{url}">{esc(name)}</a>')
    labels.append(f'<span aria-current="page">{esc(items[-1][0])}</span>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">'+'<span aria-hidden="true">/</span>'.join(labels)+'</nav>'

def faqs(items):
    return '<div class="faq-list">'+''.join(f'<details><summary>{esc(q)}<span class="plus" aria-hidden="true"></span></summary><p>{esc(a)}</p></details>' for q,a in items)+'</div>'

def process():
    items=[('01','Analyze your environment','Understand the space, occupancy and existing HVAC conditions. Use monitoring or third-party IAQ testing when a project needs baseline data.'),('02','Create your IAQ plan','Compare appropriate purification formats, monitoring locations and any ventilation or humidity support required by the space.'),('03','Execute and review','Install and configure the selected equipment, set up data access, and review indoor conditions after installation.')]
    return '<div class="process-grid">'+''.join(f'<article><span class="step-number">{n}</span><h3>{title}</h3><p>{body}</p></article>' for n,title,body in items)+'</div>'

def tech_steps():
    steps=[('air','01','Air brings oxygen and moisture','A built-in fan or the building’s HVAC airflow moves air containing oxygen and water vapour through the system.'),('light','02','UV light activates the catalyst','Inside the unit, UV energy activates the catalyst surface. This light-driven reaction is called photocatalytic oxidation.'),('layers','03','Reactive molecules support treatment','ductFIT describes generating low levels of hydrogen peroxide molecules that act on selected contaminants while the unit operates.')]
    return '<div class="technology-steps">'+''.join(f'<article><div class="step-icon">{icon(ico,28)}</div><span class="eyebrow">Step {n}</span><h3>{title}</h3><p>{body}</p></article>' for ico,n,title,body in steps)+'</div>'

def pco_diagram():
    stages=[
      ('O₂ + H₂O','Airflow','Air brings the ingredients','Air contains oxygen and water vapour. A fan or HVAC airflow brings it through the unit.'),
      ('UV + catalyst','Activation','Light powers a reaction','The UV lamp activates the catalyst surface inside the system: photocatalytic oxidation.'),
      ('H₂O₂','Formation','Reactive molecules form','ductFIT describes using oxygen and moisture to generate low levels of hydrogen peroxide molecules.'),
      ('Oxidation','Treatment','The process continues','The manufacturer describes treatment of selected contaminants in air and on surfaces. Hydrogen peroxide can decompose into water and oxygen.')]
    return '<figure class="pco-diagram"><figcaption>A simple view of the ductFIT process</figcaption><ol class="pco-flow">'+''.join('<li><span class="pco-stage">'+f'{number:02} · '+esc(label)+'</span><span class="pco-chem">'+esc(chem)+'</span><h3>'+esc(title)+'</h3><p>'+esc(copy)+'</p></li>' for number,(chem,label,title,copy) in enumerate(stages,1))+'</ol><p class="pco-note">A simplified view of the manufacturer’s process. Ask for the selected model’s operating requirements and relevant performance reports.</p></figure>'

def product_reference(product):
    if not product.get('reference_specs'):
        return ''
    rows=''.join('<div><dt>'+esc(label)+'</dt><dd>'+esc(value)+'</dd></div>' for label,value in product['reference_specs'])
    return '<section class="section technical-section"><div class="container technical-layout"><div><p class="eyebrow">Technical reference</p><h2>Details for your<br>next conversation.</h2><p>'+esc(product['reference_intro'])+'</p><p class="small">'+esc(product['reference_note'])+'</p></div><dl class="technical-specs">'+rows+'</dl></div></section>'

def project_services():
    items=[
      ('monitor','Connected monitoring','View live readings and historical trends in a centralised dashboard. Discuss sensor locations, reporting, alerts and BMS integration options for your project.'),
      ('layers','Installation and setup','Plan the equipment layout, installation and connectivity. Include Wi-Fi configuration, access to readings and handover requirements in the project scope.'),
      ('air','Before-and-after assessment','Discuss third-party IAQ testing before and after installation. A site-specific sampling plan can include particles, gases, and bacterial or fungal counts.')]
    return '<section class="section container"><div class="section-heading"><div><p class="eyebrow">Support around the equipment</p><h2>From first readings<br>to a working plan.</h2></div><p>Bring monitoring, purification and the practical details of your building into one conversation.</p></div><div class="project-services">'+''.join('<article><span class="service-icon">'+icon(ico,25)+'</span><h3>'+esc(title)+'</h3><p>'+esc(copy)+'</p></article>' for ico,title,copy in items)+'</div></section>'

def cta():
    return '<section class="closing"><div class="container closing-inner"><div><p class="eyebrow">Your space. Your starting point.</p><h2>Let’s find the right<br>air solution.</h2><p>Tell us what you need. We’ll help you compare the options.</p></div>'+button('Talk to CleanAir','/contact/','light')+'</div></section>'

def header(path):
    nav=[('Products','/products/'),('How it works','/technology/'),('Spaces','/spaces/'),('About','/about/')]
    links=''.join('<a href="'+url+'"'+(' aria-current="page"' if path.startswith(url) else '')+'>'+name+'</a>' for name,url in nav)
    notice='<div class="demo-bar"><div class="container"><span>Website proposal</span><span>A new direction for CleanAir <a href="/about/#proposal">About this preview '+icon('arrow-up',12)+'</a></span></div></div>' if DEMO else ''
    return notice+'<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="container header-inner"><a class="brand" href="/" aria-label="CleanAir home"><img src="/assets/cleanair-logo.png" alt="Clean Air" width="640" height="281" loading="eager"></a><button class="menu-toggle" aria-label="Open navigation" aria-controls="site-nav" aria-expanded="false">'+icon('menu')+'</button><nav id="site-nav" class="site-nav" aria-label="Main navigation">'+links+'<a class="button button-small button-primary" href="/contact/">Request a quote '+icon('arrow',16)+'</a></nav></div></header>'

def footer():
    return '<footer class="site-footer"><div class="container footer-grid"><div class="footer-brand"><a class="brand" href="/" aria-label="CleanAir home"><img src="/assets/cleanair-logo.png" alt="Clean Air" width="640" height="281" loading="lazy"></a><p>Cleaner air. Healthier spaces.</p><p class="small">Air purification and indoor air quality<br>monitoring in Dubai and the UAE.</p></div><div><h3>Explore</h3><a href="/products/">Products</a><a href="/technology/">Our technology</a><a href="/spaces/">Solutions by space</a><a href="/insights/">Air quality guides</a></div><div><h3>CleanAir</h3><a href="/about/">About us</a><a href="/contact/">Contact our team</a><a href="/privacy/">Privacy</a></div><div><h3>Let’s talk</h3><a href="tel:'+PHONE+'" data-track="phone_click">+971 50 461 6073</a><a href="tel:'+PHONE_SECONDARY+'" data-track="phone_click">+971 50 104 6233</a><a href="mailto:info@cleanairme.com" data-track="email_click">info@cleanairme.com</a><a href="https://wa.me/'+WHATSAPP+'" target="_blank" rel="noopener" data-track="whatsapp_click">Chat on WhatsApp '+icon('arrow-up',14)+'</a><span>Dubai, United Arab Emirates</span></div></div><div class="container footer-bottom"><span>© '+str(date.today().year)+' Clean Air Wellness &amp; Hygiene.</span><span>Thoughtfully chosen for your space.</span></div></footer>'

PAGES=[]
def write_page(path,title,description,body,crumbs=None, schema_extra=None):
    url=BASE+path
    graph=[{'@type':'Organization','@id':BASE+'/#organization','name':'Clean Air Wellness & Hygiene','url':BASE+'/', 'logo':BASE+'/assets/cleanair-logo.png','email':'info@cleanairme.com','telephone':PHONE,'contactPoint':[{'@type':'ContactPoint','telephone':number,'contactType':'customer service'} for number in [PHONE,PHONE_SECONDARY]],'address':{'@type':'PostalAddress','addressLocality':'Dubai','addressCountry':'AE'},'areaServed':{'@type':'Country','name':'United Arab Emirates'}},
           {'@type':'WebSite','@id':BASE+'/#website','url':BASE+'/','name':'CleanAir','publisher':{'@id':BASE+'/#organization'},'inLanguage':'en'},
           {'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'isPartOf':{'@id':BASE+'/#website'},'inLanguage':'en'}]
    if crumbs:
        entries=[('Home','/')]+crumbs
        graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':BASE+u} for i,(n,u) in enumerate(entries)]})
    if schema_extra:
        graph.extend(schema_extra)
    ld=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('</','<'+chr(92)+'/')
    body_html=header(path)+'<main id="main">'+body+'</main>'+footer()
    content=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="robots" content="{"noindex,follow" if DEMO else "index,follow,max-image-preview:large"}"><link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/cleanair-logo.png"><meta property="og:site_name" content="CleanAir"><meta name="twitter:card" content="summary"><meta name="theme-color" content="#00538a"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css?v={CSS_VERSION}"><script type="application/ld+json">{ld}</script><script src="/assets/site.js?v={JS_VERSION}" defer></script></head><body>{body_html}</body></html>'
    out=DIST/'index.html' if path=='/' else DIST/path.strip('/')/'index.html'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(content)
    PAGES.append({'path':path,'title':title,'description':description,'canonical':url})

home_faq=[
 ('Which product should I start with?','Start with how you will use it: a car, a room without ductwork, a building with HVAC ducts, or air quality monitoring. Our product finder suggests a starting point; the team confirms suitability.'),
 ('Is KleanSense an air purifier?','KleanSense is an indoor air quality monitor. It measures environmental readings. Choose a purification product separately if your space needs air treatment.'),
 ('Can an air purifier replace ventilation?','Air cleaning supports an overall air quality plan. Ventilation, control of pollutant sources and appropriate maintenance still matter. The right approach depends on the space and the concern.'),
 ('How do I get a price or quotation?','Tell us the product or space you are considering using the enquiry page. It prepares a WhatsApp message for you to send, or an email draft if you prefer.'),
]
finder='<section id="finder" class="section finder-section"><div class="container finder-layout"><div class="section-intro"><p class="eyebrow">A little guidance</p><h2>Find your<br>starting point.</h2><p>Choose the kind of space you’re working with. We’ll show you a sensible place to begin.</p><span class="small">Our team confirms sizing and compatibility.</span></div><div class="finder-card"><fieldset><legend>Where do you need a solution?</legend><div class="finder-options">'+''.join(f'<label><input type="radio" name="use-case" value="{value}" {"checked" if value=="home" else ""}><span>{icon(ico,23)}{label}</span></label>' for value,ico,label in [('car','car','My car'),('home','home','My home'),('office','building','A commercial space'),('monitor','monitor','Air quality monitoring')])+'</div></fieldset><label class="field-label" for="ducts">Does your space have HVAC air ducts?</label><select id="ducts"><option value="unknown">I’m not sure</option value="no">No ductwork</option value="yes">Yes, it has ducts</option></select><div class="finder-result" id="finder-result" aria-live="polite"></div></div></div></section>'
home='<section class="hero"><div class="container hero-grid"><div class="hero-copy"><p class="eyebrow"><span class="tiny-rule"></span>CleanAir · Dubai &amp; UAE</p><h1>Cleaner air.<br><span>A better space.</span></h1><p class="hero-lead">Air purification and indoor air quality monitoring, thoughtfully matched to the spaces you live, work and travel in.</p><div class="button-row">'+button('Explore the products','/products/')+button('Find my solution','#finder','ghost')+'</div><div class="hero-note">'+icon('pin',17)+'Based in Dubai. Solutions for the UAE.</div></div><div class="hero-visual"><span class="hero-visual-label">A fresh perspective on indoor air</span><div class="hero-product">'+image(P['ductfit-mobile'],'hero-device',True)+'</div><div class="hero-product-label"><span class="eyebrow">Standalone purification</span><strong>ductFIT Mobile</strong><a href="/products/ductfit-mobile/" aria-label="Explore ductFIT Mobile">'+icon('arrow-up',22)+'</a></div><a class="floating-monitor" href="/products/ductfit-kleansense-iaq-sensor/"><span class="monitor-icon">'+icon('monitor',22)+'</span><span><strong>Know your indoor air</strong><small>PM2.5 · TVOC · CO₂ &amp; more</small></span>'+icon('arrow-up',16)+'</a></div></div></section>'
home+='<section class="quick-paths"><div class="container"><a href="/products/?filter=cars">'+icon('car',22)+'<span>For your car</span>'+icon('arrow',18)+'</a><a href="/products/?filter=rooms">'+icon('home',22)+'<span>For homes &amp; offices</span>'+icon('arrow',18)+'</a><a href="/products/?filter=buildings">'+icon('building',22)+'<span>For buildings &amp; HVAC</span>'+icon('arrow',18)+'</a><a href="/products/?filter=monitoring">'+icon('monitor',22)+'<span>For air quality monitoring</span>'+icon('arrow',18)+'</a></div></section>'
home+='<section class="section"><div class="container"><div class="section-heading"><div><p class="eyebrow">The CleanAir range</p><h2>Different spaces.<br>Considered solutions.</h2></div><div><p>Portable devices, standalone systems, HVAC integration and monitoring. Explore an option that fits your needs.</p><a class="text-link" href="/products/">View the complete range '+icon('arrow',17)+'</a></div></div><div class="products-grid">'+''.join(product_card(P[x]) for x in ['ductfit-s','ductfit-mobile','ductfit-vent','ductfit-kleansense-iaq-sensor'])+'</div></div></section>'
home+=finder
home+='<section class="section technology-section"><div class="container"><div class="section-heading"><div><p class="eyebrow">Understand the technology</p><h2>A clearer way<br>to explain clean air.</h2></div><div><p>UV energy, a catalyst, oxygen and moisture power ductFIT’s described photocatalytic oxidation process. Follow the stages in plain language.</p><a class="text-link" href="/technology/">See how it works '+icon('arrow',17)+'</a></div></div>'+tech_steps()+'</div></section>'
home+='<section class="section"><div class="container monitoring-layout"><div class="monitoring-art">'+image(P['ductfit-kleansense-iaq-sensor'])+'<span>Actual KleanSense IAQ Sensor</span></div><div><p class="eyebrow">Measure before you guess</p><h2>Make the invisible<br>easier to understand.</h2><p>See eight environmental readings, live data and historical trends through KleanSense monitoring. Use the dashboard to understand indoor conditions and decide what your space needs next.</p><div class="reading-grid">'+''.join(f'<span><strong>{a}</strong><small>{b}</small></span>' for a,b in READINGS)+'</div>'+button('Explore air quality monitoring','/products/ductfit-kleansense-iaq-sensor/','ghost')+'</div></div></section>'
home+='<section class="section approach-section"><div class="container"><div class="section-heading"><div><p class="eyebrow">A practical approach</p><h2>Your needs come first.</h2></div><p>Analyze, create and execute: a practical plan for monitoring, purification and the building conditions behind your concerns.</p></div>'+process()+'</div></section>'
home+='<section class="section"><div class="container faq-layout"><div><p class="eyebrow">Good questions</p><h2>Let’s make<br>the next step simple.</h2><p>Get answers before choosing a product.</p><a class="text-link" href="/contact/">Ask our team '+icon('arrow',17)+'</a></div>'+faqs(home_faq)+'</div></section>'+cta()
write_page('/','Air Purification Dubai and UAE | CleanAir','Explore ductFIT air purification for cars, homes and commercial spaces, plus KleanSense IAQ monitoring in Dubai and the UAE. Find your solution.',home)

filters=[('all','All products'),('cars','Cars & personal'),('rooms','Rooms & interiors'),('buildings','HVAC & transport'),('monitoring','Monitoring')]
catalog='<section class="page-intro container">'+breadcrumbs([('Products','/products/')])+'<p class="eyebrow">Explore the range</p><h1>An air solution<br>for your space.</h1><p class="intro-lead">Choose from the ductFIT purification range and KleanSense monitoring. Start with the setting, then confirm the details with our team.</p></section><section class="section section-top-small"><div class="container"><div class="catalog-toolbar"><div class="filter-tabs" role="group" aria-label="Filter products">'+''.join(f'<button type="button" data-filter="{value}" aria-pressed="{"true" if value=="all" else "false"}">{label}</button>' for value,label in filters)+'</div><p class="small" id="product-count" aria-live="polite">9 products</p></div><div class="products-grid catalog-grid">'+''.join(product_card(x) for x in PRODUCTS)+'</div><div class="catalog-help"><div><h2>Need a little guidance?</h2><p>Our product finder is a useful starting point. Our team confirms the final choice.</p></div>'+button('Help me choose','/#finder','ghost')+'</div></div></section>'+cta()
write_page('/products/','Air Purifiers and IAQ Monitors UAE | CleanAir','Browse ductFIT car, standalone, wall, ceiling and HVAC purification options, plus KleanSense indoor air quality monitoring in Dubai and the UAE.',catalog,[('Products','/products/')],[{'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':BASE+'/products/'+x['slug']+'/','name':x['name']} for i,x in enumerate(PRODUCTS)]}])

for product in PRODUCTS:
    path='/products/'+product['slug']+'/'
    body='<div class="container">'+breadcrumbs([('Products','/products/'),(product['name'],path)])+'</div><section class="product-hero container"><div class="product-detail-art">'+image(product,'',True)+'<span>'+product['category']+'</span></div><div class="product-detail-copy"><p class="eyebrow">'+product['tag']+'</p><h1>'+product['name']+'</h1><h2 class="product-headline">'+product['headline']+'</h2><p class="intro-lead">'+product['intro']+'</p><ul class="feature-list">'+''.join('<li>'+icon('check',18)+esc(b)+'</li>' for b in product['bullets'])+'</ul><div class="button-row">'+button('Ask about this product','/contact/?product='+product['slug'])+'</div><p class="small">Our team can confirm suitability, configuration and a quotation.</p></div></section>'
    body+='<section class="section product-details-section"><div class="container detail-grid"><div><p class="eyebrow">Where it fits</p><h2>Applications to discuss.</h2><div class="application-tags">'+''.join('<span>'+esc(x)+'</span>' for x in product['applications'])+'</div></div><div><p class="eyebrow">Choose with clarity</p><h2>Before you decide.</h2><ul class="plain-list">'+''.join('<li>'+icon('check',18)+esc(x)+'</li>' for x in product['considerations'])+'</ul><p>We’ll help you compare the relevant model information and installation requirements for your intended use.</p></div></div></section>'
    body+=product_reference(product)
    if product['group']=='monitoring':
        body+='<section class="section container"><p class="eyebrow">Eight environmental readings</p><h2>A more informed view of your room.</h2><div class="reading-grid wide-readings">'+''.join(f'<span><strong>{a}</strong><small>{b}</small></span>' for a,b in READINGS)+'</div><p class="reading-note">KleanSense monitors conditions. It does not perform air purification or replace a ventilation system.</p><a class="text-link" href="/insights/understanding-air-quality-readings/">Understand the readings '+icon('arrow',17)+'</a></section>'
    else:
        body+='<section class="section technology-section"><div class="container"><p class="eyebrow">The process</p><h2>The idea behind ductFIT.</h2>'+tech_steps()+'<a class="text-link technology-link" href="/technology/">Explore the technology '+icon('arrow',17)+'</a></div></section>'
    related=[x for x in PRODUCTS if x['slug']!=product['slug'] and (x['group']==product['group'] or x['group']=='monitoring')][:3]
    if len(related)<3:
        related += [x for x in PRODUCTS if x not in related and x['slug']!=product['slug']][:3-len(related)]
    body+='<section class="section container"><div class="section-heading"><div><p class="eyebrow">Compare your options</p><h2>Also in the range.</h2></div><a class="text-link" href="/products/">All products '+icon('arrow',17)+'</a></div><div class="products-grid three-columns">'+''.join(product_card(x) for x in related)+'</div></section>'+cta()
    # Product identity is useful structured content; omit unverified offers, ratings and numerical performance claims.
    schema=[{'@type':'Product','name':product['name'],'description':product['intro'],'image':BASE+'/assets/'+product['image'],'url':BASE+path,'brand':{'@type':'Brand','name':'KleanSense' if product['group']=='monitoring' else 'ductFIT'},'category':product['category']}]
    write_page(path,product['title'],product['desc'],body,[('Products','/products/'),(product['name'],path)],schema)

tech_faq=[
 ('How does the nature analogy relate to ductFIT?','Oxidation is the shared concept. The indoor system uses a powered UV source and a catalyst, with oxygen and moisture in the air, rather than relying on sunlight.'),
 ('How do the different units move air?','Standalone models use their own airflow arrangement. ductFIT Vent is installed in a suitable HVAC duct or plenum and uses the building’s airflow. Installation requirements depend on the model.'),
 ('What does KleanSense add?','KleanSense provides eight environmental readings, live data and historical trends. Its dashboard helps you understand conditions and review changes over time.'),
 ('How should CO₂ and humidity be addressed?','Assess fresh-air exchange and room conditions. A project may need ventilation adjustments or dedicated dehumidification alongside purification and monitoring.'),
 ('What information should I request for my project?','Ask for the selected model’s data sheet, installation and care requirements, relevant test reports, and the monitoring or assessment scope included in your quotation.')]
technology=(
 '<section class="page-intro container">'+breadcrumbs([('How it works','/technology/')])+'<p class="eyebrow">Photocatalytic oxidation · PCO</p><h1>Understanding<br>ductFIT technology.</h1><p class="intro-lead">UV energy, a catalyst, oxygen and moisture are the inputs in ductFIT’s described purification process. Connected IAQ monitoring adds a separate view of the conditions in your space.</p></section>'
 +'<section class="section technology-section"><div class="container"><p class="eyebrow">From airflow to oxidation</p><h2>Four stages.<br>One continuous process.</h2>'+pco_diagram()
 +'<div class="technology-copy-grid"><article><h3>Inspired by oxidation in nature</h3><p>Oxidation is part of natural atmospheric chemistry. ductFIT’s indoor approach uses controlled UV energy at a catalyst surface, with oxygen and water vapour present in the airflow.</p></article><article><h3>What the process aims to address</h3><p>The manufacturer describes action on selected odour-causing compounds and biological contaminants in air and on surfaces. Model-specific reports explain the results under their tested conditions.</p></article></div></div></section>'
 +'<section class="section container"><div class="section-heading"><div><p class="eyebrow">An overall air quality plan</p><h2>Look at the whole space.</h2></div><p>Bring purification, monitoring, ventilation and room conditions into the same plan.</p></div><div class="process-grid"><article><span class="step-number">01</span><h3>Understand the sources</h3><p>Review activities, occupancy and the building. Use an appropriate assessment or sampling plan to understand the concern.</p></article><article><span class="step-number">02</span><h3>Match the equipment</h3><p>Compare a standalone room unit with HVAC integration. Confirm placement, airflow, power and maintenance access for the selected model.</p></article><article><span class="step-number">03</span><h3>Monitor and review</h3><p>Use live readings and historical trends to review conditions. Discuss follow-up IAQ testing where independent measurement is part of the project.</p></article></div><div class="source-note">Further reading: <a href="https://cleanairme.com/blog/how-ductfit-photocatalysis-works" target="_blank" rel="noopener">CleanAir’s technology explanation '+icon('arrow-up',12)+'</a> · <a href="https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home" target="_blank" rel="noopener">US EPA guide to air cleaners '+icon('arrow-up',12)+'</a></div></section>'
 +'<section class="section technology-section"><div class="container faq-layout"><div><p class="eyebrow">Questions worth asking</p><h2>Know how it fits<br>your space.</h2><p>Compare the process, installation and supporting information before selecting a model.</p>'+button('Discuss the technology','/contact/','ghost')+'</div>'+faqs(tech_faq)+'</div></section>'+cta()
)

write_page('/technology/','ductFIT Air Purification Technology | CleanAir UAE','Learn how ductFIT uses UV light, a catalyst, oxygen and moisture in photocatalytic oxidation. Explore purification and IAQ monitoring for your UAE space.',technology,[('How it works','/technology/')])

spaces_data=[('Homes and villas','home','A solution that fits your everyday surroundings.','Consider room layout, ventilation and a suitable placement for a standalone or installed unit.','rooms'),('Offices and retail','building','A clearer plan for shared indoor spaces.','Discuss occupancy, the HVAC arrangement, operating hours and whether monitoring would help the team.','rooms'),('Hotels and hospitality','home','Options for rooms and shared areas.','Compare installation formats and ongoing care to suit a hospitality setting.','rooms'),('Schools and education','building','Understand conditions in occupied rooms.','Consider the layout, ventilation and a plan for monitoring and appropriate equipment selection.','buildings'),('Healthcare settings','building','Product selection for a considered facility plan.','Discuss facility requirements and supporting technical documentation. Purification supports the wider air quality strategy.','buildings'),('Transport and mobility','car','Air solutions for personal and shared journeys.','Explore portable car options or a transport-specific HVAC retrofit, depending on the vehicle and application.','cars')]
spaces='<section class="page-intro container">'+breadcrumbs([('Spaces','/spaces/')])+'<p class="eyebrow">Solutions by setting</p><h1>Your space shapes<br>the right solution.</h1><p class="intro-lead">Start with the environment and the concern. We’ll help you compare the formats and information that matter for your project.</p></section><section class="section section-top-small container"><div class="spaces-grid">'+''.join('<article class="space-card"><span class="space-icon">'+icon(ico,26)+'</span><h2>'+title+'</h2><strong>'+lead+'</strong><p>'+desc+'</p><a class="text-link" href="/contact/?space='+esc(title)+'">Discuss this space '+icon('arrow',17)+'</a></article>' for title,ico,lead,desc,group in spaces_data)+'</div></section><section class="section approach-section"><div class="container"><p class="eyebrow">From requirements to a quotation</p><h2>A practical next step.</h2>'+process()+'</div></section>'+cta()
write_page('/spaces/','Indoor Air Solutions for Homes and Businesses | CleanAir UAE','Explore air purification and monitoring options for homes, offices, schools, hotels and transport. Discuss your Dubai or UAE space with CleanAir.',spaces,[('Spaces','/spaces/')])

proposal='<section id="proposal" class="section proposal-section"><div class="container"><p class="eyebrow">For the proposal review</p><h2>A clearer website for CleanAir.</h2><div class="proposal-grid"><article><h3>Accurate and focused</h3><p>Authentic product images, relevant company copy and no unrelated landscaping reviews. Product pages explain model distinctions and clearly label model-specific technical references.</p></article><article><h3>A useful enquiry journey</h3><p>A product finder and prefilled enquiries give visitors a clear starting point. WhatsApp messages stay drafts until the visitor presses Send.</p></article><article><h3>Prepared for a public launch</h3><p>Separate HTML pages, unique metadata, canonical URLs, structured data and a sitemap. This proposal is private and excluded from indexing; production configuration enables indexing.</p></article></div></div></section>' if DEMO else ''
about='<section class="page-intro container">'+breadcrumbs([('About CleanAir','/about/')])+'<p class="eyebrow">CleanAir · Dubai, UAE</p><h1>Better information.<br>Better air decisions.</h1><p class="intro-lead">CleanAir provides ductFIT air purification products and KleanSense indoor air quality monitoring for Dubai and the UAE.</p></section><section class="section section-top-small container about-layout"><div class="about-art">'+image(P['ductfit-wall'],'',True)+'</div><div><h2>Chosen around how<br>you use your space.</h2><p>Our range brings together portable devices, standalone systems, wall and ceiling installation options, and HVAC-integrated units. KleanSense adds environmental monitoring to help you understand indoor conditions.</p><p>Our analyze, create and execute approach starts with indoor conditions, then brings together appropriate equipment, monitoring and installation. Discuss baseline assessment, dashboard setup and a review after installation as part of your project.</p>'+button('Meet your solution','/products/','ghost')+'</div></section><section class="section approach-section"><div class="container"><p class="eyebrow">How we approach a project</p><h2>Clear choices from the start.</h2>'+process()+'</div></section>'+project_services()+proposal+cta()
write_page('/about/','About CleanAir Dubai | Air Purification and IAQ','Explore CleanAir’s ductFIT purification, KleanSense monitoring, installation and IAQ assessment support for homes and businesses in Dubai and the UAE.',about,[('About CleanAir','/about/')])

contact='<section class="page-intro container">'+breadcrumbs([('Contact','/contact/')])+'<p class="eyebrow">Let’s talk about your space</p><h1>Your next step<br>to clearer air.</h1><p class="intro-lead">Tell us what you’re considering. We’ll help you compare suitable products and the details for a quotation.</p></section><section class="section section-top-small container contact-layout"><aside class="contact-details"><h2>Talk to CleanAir.</h2><a href="https://wa.me/'+WHATSAPP+'" target="_blank" rel="noopener" data-track="whatsapp_click"><span>'+icon('chat',22)+'</span><div><strong>WhatsApp</strong><small>+971 50 116 9833</small></div>'+icon('arrow-up',18)+'</a><a href="tel:'+PHONE+'" data-track="phone_click"><span>'+icon('chat',22)+'</span><div><strong>Call our team</strong><small>+971 50 461 6073</small></div>'+icon('arrow-up',18)+'</a><a href="tel:'+PHONE_SECONDARY+'" data-track="phone_click"><span>'+icon('chat',22)+'</span><div><strong>Call our team</strong><small>+971 50 104 6233</small></div>'+icon('arrow-up',18)+'</a><a href="mailto:info@cleanairme.com" data-track="email_click"><span>'+icon('mail',22)+'</span><div><strong>Email us</strong><small>info@cleanairme.com</small></div>'+icon('arrow-up',18)+'</a><div class="location-note">'+icon('pin',20)+'<span>Based in Dubai<br>United Arab Emirates</span></div><p>Not sure which product to choose? Describe the space and what you want to address. It’s a useful place to begin.</p></aside><div class="enquiry-card"><h2>Prepare your enquiry.</h2><p class="small">Complete a few details, then choose WhatsApp or an email draft.</p><form id="enquiry-form"><div class="form-grid"><div><label for="name">Your name <span aria-hidden="true">*</span></label><input id="name" name="name" autocomplete="name" required maxlength="100" placeholder="Your full name"></div><div><label for="contact">Phone number or email <span aria-hidden="true">*</span></label><input id="contact" name="contact" autocomplete="off" required maxlength="120" placeholder="How can our team reach you?"></div><div><label for="space">Type of space</label><select id="space" name="space"><option value="">Choose a space</option>'+''.join('<option>'+x+'</option>' for x in ['Car','Home or villa','Office or retail','Hotel or hospitality','School or education','Healthcare setting','Transport','Other'])+'</select></div><div><label for="product">Product of interest</label><select id="product" name="product"><option value="">Help me choose</option>'+''.join(f'<option value="{x["slug"]}">{x["name"]}</option>' for x in PRODUCTS)+'</select></div><div><label for="location">Location</label><input id="location" name="location" maxlength="120" placeholder="Dubai, Abu Dhabi, Sharjah…"></div><div><label for="size">Approximate room area <span class="optional">(optional)</span></label><input id="size" name="size" maxlength="60" placeholder="For example, 60 m²; leave blank for a car"></div><div class="full"><label for="message">What would you like help with?</label><textarea id="message" name="message" rows="3" maxlength="2000" placeholder="Tell us about your space or the concern you want to address."></textarea></div></div><button class="button button-primary" id="prepare-enquiry" type="button" disabled>Prepare my enquiry '+icon('arrow',18)+'</button><p class="form-help">Nothing is sent automatically. You choose when to send your message.</p><noscript><p>Please use the WhatsApp, phone or email links to contact our team.</p></noscript></form><section id="enquiry-result" class="enquiry-result" hidden tabindex="-1" aria-live="polite"><h3>Your enquiry draft is ready.</h3><p>Review it below. Press Send in WhatsApp, or send the email draft, to deliver it to CleanAir.</p><textarea id="message-preview" readonly aria-label="Your enquiry message" rows="7"></textarea><div class="button-row"><a id="whatsapp-draft" class="button button-primary" target="_blank" rel="noopener" data-track="whatsapp_click" href="https://wa.me/'+WHATSAPP+'">Continue on WhatsApp '+icon('arrow-up',16)+'</a><a id="email-draft" class="button button-ghost" data-track="email_click" href="mailto:info@cleanairme.com">Open email draft</a><button class="text-link" id="copy-enquiry" type="button">Copy message</button></div><p class="small" id="copy-status" aria-live="polite"></p></section></div></section>'
write_page('/contact/','Contact CleanAir Dubai | Air Purification Quote','Contact CleanAir in Dubai for ductFIT purification or KleanSense monitoring. Prepare a product enquiry, ask about your space, or request a quotation.',contact,[('Contact','/contact/')])

guides=[
 ('choosing-an-air-purifier-in-dubai','Choosing an air purifier in Dubai','Start with the space and the concern, then compare an appropriate type of device.','Choosing an Air Purifier in Dubai | CleanAir Guide'),
 ('understanding-air-quality-readings','Understand your air quality readings','What PM2.5, TVOC and CO₂ can tell you, and why the readings describe different conditions.','PM2.5 TVOC and CO2 Readings Explained | CleanAir UAE'),
]
insights='<section class="page-intro container">'+breadcrumbs([('Air quality guides','/insights/')])+'<p class="eyebrow">Make informed choices</p><h1>A little clarity<br>goes a long way.</h1><p class="intro-lead">Straightforward guides to choosing an air solution and understanding indoor environmental readings.</p></section><section class="section section-top-small container"><div class="guides-grid">'+''.join('<article class="guide-card"><div class="guide-art">'+image(P['ductfit-mobile'] if i==0 else P['ductfit-kleansense-iaq-sensor'])+'</div><p class="eyebrow">'+('Product selection' if i==0 else 'Air quality monitoring')+'</p><h2><a href="/insights/'+slug+'/">'+title+'</a></h2><p>'+desc+'</p><a class="text-link" href="/insights/'+slug+'/">Read the guide '+icon('arrow',17)+'</a></article>' for i,(slug,title,desc,seo_title) in enumerate(guides))+'</div></section>'+cta()
write_page('/insights/','Indoor Air Quality Guides Dubai and UAE | CleanAir','Read clear guides to choosing an air purifier and understanding PM2.5, TVOC and CO2 readings. Make more informed indoor air decisions with CleanAir.',insights,[('Air quality guides','/insights/')])

guide1='<h2>Start with where you will use it</h2><p>A car, one room and an HVAC system call for different formats. A portable device and a duct-integrated unit are not interchangeable. Check the product’s intended application before considering installation or size.</p><h2>Describe the concern</h2><p>Dust, odours, ventilation and dampness call for different questions. Identify likely sources and building conditions rather than assuming one device addresses every issue. Air cleaning supplements source control and ventilation.</p><h2>Compare the information that matters</h2><ul><li>Intended use and model suitability</li><li>Room requirements or HVAC installation conditions</li><li>Power connection, placement and maintenance</li><li>Applicable performance documentation and care costs</li></ul><h2>Decide whether monitoring would help</h2><p>Environmental monitoring can help you understand conditions and observe trends. KleanSense provides readings; a purification product performs a separate task. Discuss which measurements are useful for the concern in your space.</p><h2>Prepare a useful enquiry</h2><p>Tell the team your location, type of space, approximate room area and the issue you want to address. If you have an HVAC plan or a model in mind, include it in the conversation.</p>'
guide2='<h2>PM2.5 describes fine particles</h2><p>PM2.5 refers to airborne particles with a diameter of 2.5 micrometres or smaller. Particle levels can vary with activities and conditions, so look at patterns rather than a single reading.</p><h2>TVOC combines multiple compounds</h2><p>Total volatile organic compounds is a combined measurement. It does not identify every individual substance or its risk. Changes may help you investigate activities, products or ventilation in a room.</p><h2>CO₂ is a different kind of signal</h2><p>Carbon dioxide can rise in occupied rooms with limited fresh air exchange. It is a useful part of a ventilation discussion. A purification device does not replace fresh air exchange, and CO₂ alone does not describe every air quality concern.</p><h2>Temperature and humidity add context</h2><p>These readings describe environmental conditions. Consider them alongside activities, occupancy and the sensor’s placement when reviewing room trends.</p><h2>Use live readings and historical trends together</h2><p>A connected dashboard helps you compare the current reading with earlier conditions. Note occupancy, operating hours and activities when reviewing changes. Discuss reporting, alerts and any BMS integration requirements with the team.</p><h2>Read the pattern, then ask the right question</h2><p>Compare readings over time and note what was happening in the space. A monitor provides information; it does not identify every pollutant or replace an appropriate assessment. Ask the team about sensor configuration, placement and data access.</p>'
for i,(slug,title,desc,seo_title) in enumerate(guides):
    path='/insights/'+slug+'/'
    body='<section class="page-intro container">'+breadcrumbs([('Air quality guides','/insights/'),(title,path)])+'<p class="eyebrow">CleanAir guide</p><h1>'+title+'</h1><p class="intro-lead">'+desc+'</p></section><article class="article-body container">'+(guide1 if i==0 else guide2)+'<div class="source-note">Further reading: <a href="https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home" target="_blank" rel="noopener">US EPA guide to air cleaners</a> · <a href="https://cleanairme.com/products/ductfit-kleansense-iaq-sensor" target="_blank" rel="noopener">KleanSense product information</a></div>'+button('Discuss my space','/contact/','ghost')+'</article>'+cta()
    write_page(path,seo_title,desc+' Explore practical indoor air guidance for Dubai and the UAE.',body,[('Air quality guides','/insights/'),(title,path)])

privacy='<section class="page-intro container">'+breadcrumbs([('Privacy','/privacy/')])+'<p class="eyebrow">Your enquiry details</p><h1>A clear note<br>about your information.</h1></section><article class="article-body container"><h2>Enquiry drafts</h2><p>The enquiry form prepares a message in your browser. It does not automatically send your details to a server. If you choose WhatsApp or email, the details are transferred into a draft in that service, which you decide whether to send.</p><h2>Services you choose to open</h2><p>WhatsApp and your email provider process information under their own policies when you use them. You can call or email CleanAir directly instead of completing the form.</p><h2>Website analytics</h2><p>This preview has no external analytics service configured. A public launch should include an updated privacy notice reflecting any forms, analytics and other services enabled on the production website.</p><h2>Questions</h2><p>Contact <a href="mailto:info@cleanairme.com">info@cleanairme.com</a> with questions about a CleanAir enquiry.</p></article>'
write_page('/privacy/','Enquiry Privacy | CleanAir Website Preview','Understand how enquiry drafts work on this CleanAir preview and what happens when you choose WhatsApp or email.',privacy,[('Privacy','/privacy/')])

notfound='<section class="page-intro container not-found"><p class="eyebrow">Page not found</p><h1>Let’s find your<br>way back.</h1><p class="intro-lead">Explore the product range or ask our team about your space.</p>'+button('Explore products','/products/')+'</section>'
write_page('/404/','Page Not Found | CleanAir','Explore CleanAir air purification and monitoring products, or contact our team about your Dubai or UAE space.',notfound)
(DIST/'404.html').write_text((DIST/'404'/'index.html').read_text())

urls=[x['canonical'] for x in PAGES if x['path']!='/404/']
sitemap='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(u)+'</loc></url>' for u in urls)+'</urlset>'
(DIST/'sitemap.xml').write_text(sitemap)
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n')
(DIST/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n/assets/*\n  Cache-Control: public, max-age=86400\n')
(DIST/'assets'/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#00538a"/><path d="M14 25h26c9 0 9-12 1-12M14 33h35c10 0 10 13 1 13M14 41h16" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/></svg>')
(ROOT/'page_manifest.json').write_text(json.dumps(PAGES,indent=2))
print(json.dumps({'pages':len(PAGES),'base_url':BASE,'mode':args.mode,'output':str(DIST)}))

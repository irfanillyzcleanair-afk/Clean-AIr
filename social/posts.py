"""30-day Instagram content plan for CleanAir (Clean Air Wellness & Hygiene, Dubai).

Each post has: the on-image copy, the layout to render, the caption, hashtags and
the audience it targets. Copy follows the claim rules in content_sources.json:
no universal health guarantees, no efficacy percentages for the products and
no certification claims. General indoor-air facts name their source.
"""

WEBSITE = "www.cleanairme.com"
WHATSAPP = "+971 50 116 9833"
WHATSAPP_LINK = "https://wa.me/971501169833"
EMAIL = "info@cleanairme.com"

CTA_LINE = (
    f"\n\n📩 DM us, WhatsApp {WHATSAPP} or email {EMAIL}"
    f"\n🌐 {WEBSITE}"
)

TAGS_CORE = "#CleanAirUAE #IndoorAirQuality #AirPurification #Dubai #UAE"
TAGS_OFFICE = "#DubaiOffices #FacilityManagement #WorkplaceWellbeing #HealthyBuildings #DubaiBusiness"
TAGS_VILLA = "#DubaiVillas #LuxuryHomesDubai #DubaiHomes #VillaLife #InteriorDubai"
TAGS_GOV = "#SmartDubai #PublicSector #UAEGovernment #SustainableUAE #FacilityManagementUAE"
TAGS_EDU = "#IAQ #PM25 #AirQualityMatters #HealthyHome #KnowYourAir"
TAGS_PRODUCT = "#ductFIT #KleanSense #PhotocatalyticOxidation #AirPurifierDubai #CleanAirSolutions"

# layout keys are implemented in render.py
POSTS = [
    dict(day=1, layout="hero", audience="All", pillar="Brand",
         eyebrow="Introducing Clean Air", title="Cleaner air.<br>Healthier spaces.",
         body="Air purification and indoor air quality monitoring for offices, villas and public buildings across the UAE.",
         products=["ductfit-vent", "ductfit-mobile", "ductfit-kleansense-iaq-sensor"],
         caption="The air inside your building is the air your team, your family and your visitors breathe all day.\n\n"
                 "Clean Air Wellness & Hygiene brings the ductFIT air purification range and KleanSense indoor air quality monitoring to Dubai and the UAE, from HVAC-integrated units for large buildings to discreet room units for villas.\n\n"
                 "Over the next 30 days we'll show you what's in indoor air, how to measure it, and how to choose the right solution for your space. Follow along 👇",
         tags=[TAGS_CORE, TAGS_PRODUCT]),
    dict(day=2, layout="fact", audience="All", pillar="Education",
         eyebrow="Did you know?", big="~90%", title="of our time is spent indoors.",
         body="So the air inside your office, home or service centre matters more than you think.",
         source="Source: US Environmental Protection Agency (EPA)",
         caption="Most of us spend around 90% of our time indoors, according to the US EPA. In the UAE, with long summers and AC running around the clock, that number can feel even higher.\n\n"
                 "That makes indoor air one of the biggest parts of your daily environment, and one of the least visible.\n\n"
                 "Question for you: when did you last check the air quality in your office or home? Tell us in the comments 👇",
         tags=[TAGS_CORE, TAGS_EDU]),
    dict(day=3, layout="audience", audience="Offices", pillar="Audience",
         eyebrow="For offices", title="Your best people deserve your best air.",
         points=["Ceiling and grid-ceiling units for open-plan floors", "HVAC-integrated purification for the whole building", "Live air quality dashboards for facility teams"],
         products=["ductfit-cloud"],
         caption="Talent, focus and first impressions all happen indoors.\n\n"
                 "For offices, we combine:\n✅ ductFIT Cloud: fits into standard grid ceiling tiles\n✅ ductFIT Vent: purification installed inside your HVAC ducts\n✅ KleanSense: live readings so your facility team can see the air, not guess it\n\n"
                 "HR and facility managers: book a site consultation and we'll walk your floor with you.",
         tags=[TAGS_CORE, TAGS_OFFICE]),
    dict(day=4, layout="steps", audience="All", pillar="Technology",
         eyebrow="How ductFIT works", title="Photocatalytic oxidation, explained in 3 steps.",
         steps=[("01", "Air flows in", "A built-in fan or your HVAC airflow brings air, oxygen and moisture through the unit."),
                ("02", "UV meets catalyst", "UV light activates a catalyst surface, a light-driven reaction called photocatalytic oxidation."),
                ("03", "Treatment in action", "Low levels of reactive molecules act on selected contaminants while the unit operates.")],
         caption="How does ductFIT treat air? With a process inspired by nature: photocatalytic oxidation (PCO).\n\n"
                 "1️⃣ Air carrying oxygen and water vapour moves through the unit\n2️⃣ UV light activates a catalyst surface\n3️⃣ The reaction produces low levels of reactive molecules that act on selected contaminants while the unit runs\n\n"
                 "Same technology across the range, from in-duct units to standalone room units. Save this post to explain it to your team 🔖",
         tags=[TAGS_CORE, TAGS_PRODUCT]),
    dict(day=5, layout="product", audience="Offices · Government", pillar="Product",
         eyebrow="ductFIT Vent", title="Air treatment, integrated into your building.",
         specs=[("Installs", "Inside HVAC ducts or plenums"), ("Vent 100 size", "29 × 18 × 31 cm"), ("Vent 100 power", "Max 30 W"), ("Indicator", "UV bulb monitoring")],
         products=["ductfit-vent"],
         caption="No extra units on the floor. No change to your interiors.\n\n"
                 "ductFIT Vent is installed inside your HVAC ducts or plenums and uses your building's existing airflow, which makes it a strong fit for office towers, government buildings, hotels and malls.\n\n"
                 "Reference model Vent 100: 29 × 18 × 31 cm, max 30 W, with a UV bulb monitoring indicator.\n\n"
                 "Facility & MEP teams: send us your duct layout and we'll recommend the right model.",
         tags=[TAGS_CORE, TAGS_PRODUCT, "#HVAC #MEP"]),
    dict(day=6, layout="audience", audience="Villas", pillar="Audience",
         eyebrow="For villas", title="Your villa is beautifully designed. Is the air?",
         points=["Discreet wall, ceiling and lampshade-style units", "Standalone purifiers with no installation", "Monitor every room from your phone"],
         products=["ductfit-lampshade"],
         caption="You chose every finish, fabric and fixture. The air deserves the same care.\n\n"
                 "For villas we offer purification that fits the interior:\n✨ ductFIT Lampshade: designed to blend in\n✨ ductFIT Wall & Ceiling: for rooms without ducts\n✨ ductFIT Mobile: plug in and go\n✨ KleanSense: see your home's air quality live\n\n"
                 "Book a home visit and we'll recommend a plan room by room.",
         tags=[TAGS_CORE, TAGS_VILLA]),
    dict(day=7, layout="audience", audience="Government", pillar="Audience",
         eyebrow="For government & public buildings", title="Shared spaces. Shared air. Shared responsibility.",
         points=["HVAC-integrated purification for large buildings", "Centralised IAQ monitoring and data reports", "Assessment, installation and review support"],
         products=["ductfit-vent", "ductfit-kleansense-iaq-sensor"],
         caption="Service centres, ministries, municipalities and authorities welcome thousands of people through their doors every week.\n\n"
                 "We support facility and procurement teams with a full approach:\n🔹 Analyse: understand the building, occupancy and HVAC\n🔹 Create: an IAQ plan with the right purification and monitoring\n🔹 Execute: installation, data access and post-installation review\n\n"
                 "Contact us for a technical presentation for your facilities team.",
         tags=[TAGS_CORE, TAGS_GOV]),
    dict(day=8, layout="readings", audience="All", pillar="Product",
         eyebrow="KleanSense IAQ Sensor", title="You can't manage what you don't measure.",
         products=["ductfit-kleansense-iaq-sensor"],
         caption="Eight readings. One dashboard. Real-time clarity.\n\n"
                 "KleanSense measures PM2.5, TVOC, CO₂, CO, O₃, HCHO (formaldehyde), temperature and humidity, then sends live data and historical trends to a central dashboard over Wi-Fi.\n\n"
                 "For offices and public buildings, that means data for wellbeing and sustainability reporting. For villas, it means peace of mind.\n\n"
                 "Compact: 135 × 135 × 40 mm.",
         tags=[TAGS_CORE, TAGS_PRODUCT, "#SmartBuilding"]),
    dict(day=9, layout="explainer", audience="All", pillar="Education",
         eyebrow="Air quality 101", title="What is PM2.5?",
         body="Fine particles 2.5 microns or smaller, about 30× thinner than a human hair. Too small to see, which is why measuring matters.",
         points=["Sources: outdoor dust, traffic, cooking, incense (bakhoor)", "In the UAE: dust and sand events can raise outdoor levels", "Track it indoors with a monitor like KleanSense"],
         caption="PM2.5 = particulate matter 2.5 micrometres or smaller. For scale, a human hair is roughly 50–70 micrometres wide.\n\n"
                 "Common sources indoors and out:\n• Dust and sand events\n• Traffic and construction\n• Cooking and frying\n• Bakhoor and candles\n\n"
                 "You can't see it, so the only way to know your levels is to measure. Save this for later 🔖",
         tags=[TAGS_CORE, TAGS_EDU]),
    dict(day=10, layout="product", audience="Offices", pillar="Product",
         eyebrow="ductFIT Cloud", title="Designed to sit within your ceiling.",
         specs=[("Fits", "Standard grid ceiling tiles"), ("Works", "Independently of HVAC ducts"), ("Airflow", "Built-in fan"), ("Ideal for", "Offices & commercial rooms")],
         products=["ductfit-cloud"],
         caption="Most offices in Dubai have grid ceilings. ductFIT Cloud is designed to drop straight into one.\n\n"
                 "It works independently of your HVAC ducts, has a built-in fan for circulation, and keeps your floor space and desks completely clear.\n\n"
                 "Perfect for open-plan floors, meeting rooms and reception areas. Ask us how many units your floor plan needs.",
         tags=[TAGS_CORE, TAGS_PRODUCT, TAGS_OFFICE]),
    dict(day=11, layout="poll", audience="All", pillar="Engagement",
         eyebrow="Quick question", title="Which room needs cleaner air first?",
         options=["A  Meeting rooms", "B  Reception & waiting areas", "C  Bedrooms", "D  The majlis"],
         caption="Tell us in the comments: A, B, C or D? 👇\n\n"
                 "Every building has one space where air quality matters most, whether it's a packed meeting room, a busy customer service hall or the bedroom where your family sleeps.\n\n"
                 "We'll share tips for the most-voted room later this month.",
         tags=[TAGS_CORE, "#DubaiLife #UAELife"]),
    dict(day=12, layout="steps", audience="Offices · Government", pillar="Trust",
         eyebrow="Our approach", title="Analyse. Create. Execute.",
         steps=[("01", "Analyse your environment", "Space, occupancy and HVAC conditions, with monitoring or third-party IAQ testing for baseline data."),
                ("02", "Create your IAQ plan", "The right purification formats, monitoring locations, and ventilation or humidity support."),
                ("03", "Execute and review", "Installation, configuration, data access and a review of conditions after installation.")],
         caption="We don't just sell a box. We follow a process:\n\n"
                 "🔍 Analyse: understand your space, people and HVAC, with baseline monitoring or third-party IAQ testing if needed\n📐 Create: a tailored indoor air quality plan\n🛠 Execute: installation, configuration and post-installation review\n\n"
                 "Ideal for corporate offices, government buildings and multi-villa projects. Let's start with a site visit.",
         tags=[TAGS_CORE, TAGS_OFFICE, TAGS_GOV]),
    dict(day=13, layout="question", audience="Offices", pillar="Education",
         eyebrow="Workplace air", title="Feeling sleepy in the 3 pm meeting?",
         body="Full rooms and closed doors let CO₂ build up from people breathing. A CO₂ reading tells you when a room needs more fresh air.",
         caption="It's not always the lunch 😅\n\n"
                 "When a meeting room is full and the door is closed, carbon dioxide from breathing builds up. CO₂ is a useful indicator of how well a room is ventilated for the number of people in it.\n\n"
                 "KleanSense shows CO₂ live, so facility teams can spot rooms that need more fresh air and act on data, not complaints.\n\n"
                 "Tag your colleague who always books the smallest meeting room 👇",
         tags=[TAGS_CORE, TAGS_OFFICE, TAGS_EDU]),
    dict(day=14, layout="product", audience="Villas · Offices", pillar="Product",
         eyebrow="ductFIT Mobile", title="A standalone solution. No installation needed.",
         specs=[("Setup", "Standalone, no ducts needed"), ("Airflow", "Built-in fan"), ("Ideal for", "Homes, offices, any room"), ("Technology", "Photocatalytic oxidation")],
         products=["ductfit-mobile"],
         caption="Need cleaner air in a room today, with no contractor and no ceiling work?\n\n"
                 "ductFIT Mobile is a standalone unit with a built-in fan that brings ductFIT purification to any room: a private office, a bedroom, a clinic room or a villa guest suite.\n\n"
                 "Move it where you need it. DM us for availability.",
         tags=[TAGS_CORE, TAGS_PRODUCT, "#AirPurifier"]),
    dict(day=15, layout="quote", audience="Villas", pillar="Audience",
         eyebrow="For the majlis", title="Guests notice the air before they notice the décor.",
         products=["ductfit-lampshade"],
         caption="Hospitality is in our culture. The majlis is where it shows.\n\n"
                 "Between bakhoor, cooking and full gatherings, majlis air works hard. The ductFIT Lampshade-style unit is designed to blend into the interior while it works, so nothing distracts from your space.\n\n"
                 "Ask us about the right setup for your majlis.",
         tags=[TAGS_CORE, TAGS_VILLA, "#Majlis #EmiratiHospitality"]),
    dict(day=16, layout="fact", audience="All", pillar="Education",
         eyebrow="Living in the UAE", big="24/7", title="AC running. Windows closed.",
         body="Our climate keeps us indoors and our air recirculating. That's exactly why indoor air needs attention here.",
         source="Clean Air Wellness & Hygiene · Dubai",
         caption="Hot summers, dust events, sealed buildings and AC that rarely stops. Life in the UAE is lived indoors for much of the year.\n\n"
                 "Recirculated air is efficient for cooling, but it means indoor air quality depends on what's in your building and how it's treated.\n\n"
                 "The good news: you can measure it and improve it. Start with a conversation with our team.",
         tags=[TAGS_CORE, TAGS_EDU, "#UAESummer"]),
    dict(day=17, layout="checklist", audience="Offices · Government", pillar="Education",
         eyebrow="For facility managers", title="5 questions to ask about your building's air",
         points=["Do we know our PM2.5, CO₂ and TVOC levels?", "Which rooms have the most people for the longest time?", "Is our HVAC treating air or just cooling it?", "Do we have data for our wellbeing / ESG reports?", "When were readings last reviewed after a fit-out?"],
         caption="Facility managers, save this checklist 🔖\n\n"
                 "1. Do we actually know our PM2.5, CO₂ and TVOC levels?\n2. Which rooms have the highest occupancy for the longest time?\n3. Is our HVAC treating the air, or only cooling it?\n4. Do we have IAQ data for wellbeing and ESG reporting?\n5. When did we last review readings after a fit-out or renovation?\n\n"
                 "If you answered 'not sure' to two or more, let's talk. We can start with monitoring.",
         tags=[TAGS_CORE, TAGS_OFFICE, TAGS_GOV]),
    dict(day=18, layout="product", audience="Villas · Offices", pillar="Product",
         eyebrow="ductFIT Wall", title="A considered fit for your wall.",
         specs=[("Mounting", "Wall-mounted"), ("Works", "Independently of HVAC ducts"), ("Airflow", "Built-in fan"), ("Benefit", "Keeps floor space clear")],
         products=["ductfit-wall"],
         caption="No ducts? No floor space? No problem.\n\n"
                 "ductFIT Wall mounts neatly on the wall, works independently of HVAC ductwork and uses a built-in fan to circulate air, keeping your floor clear.\n\n"
                 "Great for bedrooms, home offices, clinic rooms and private offices.",
         tags=[TAGS_CORE, TAGS_PRODUCT]),
    dict(day=19, layout="explainer", audience="All", pillar="Education",
         eyebrow="Air quality 101", title="What is TVOC?",
         body="Total Volatile Organic Compounds: gases released by many everyday products. You may smell some; many you won't.",
         points=["New furniture, carpets and paint", "Cleaning products and air fresheners", "Printers, adhesives and fit-out materials"],
         caption="TVOC stands for Total Volatile Organic Compounds, a combined reading of gases released from everyday materials and products.\n\n"
                 "Common indoor sources:\n• New furniture, carpets and paint\n• Cleaning sprays and fresheners\n• Printers and adhesives\n\n"
                 "That 'new office smell' after a fit-out? A TVOC reading tells you more. KleanSense measures it live.",
         tags=[TAGS_CORE, TAGS_EDU]),
    dict(day=20, layout="audience", audience="Government", pillar="Audience",
         eyebrow="Customer service centres", title="Hundreds of visitors a day. One shared air.",
         points=["Ceiling units for halls and waiting areas", "Live occupancy-driven CO₂ insight", "Reports for facility and sustainability teams"],
         products=["ductfit-ceiling", "ductfit-kleansense-iaq-sensor"],
         caption="Government service centres, hospitals' waiting areas, licensing offices and courts all have one thing in common: lots of people sharing the same air for long periods.\n\n"
                 "ductFIT Ceiling units treat air where people wait, and KleanSense gives teams live data on CO₂, particles and more, supporting smart, data-led facility decisions.\n\n"
                 "We welcome enquiries from public-sector facility and procurement teams.",
         tags=[TAGS_CORE, TAGS_GOV]),
    dict(day=21, layout="myth", audience="All", pillar="Education",
         eyebrow="Myth vs fact", myth="If the air looks clean, it is clean.",
         fact="PM2.5, CO₂, TVOC and formaldehyde are invisible. The only way to know is to measure.",
         caption="❌ MYTH: If the air looks and smells fine, it's fine.\n✅ FACT: Many indoor pollutants, including fine particles, CO₂, VOCs and formaldehyde, are invisible and often odourless.\n\n"
                 "That's why we always start with measurement. Share this with someone who needs to hear it 🔁",
         tags=[TAGS_CORE, TAGS_EDU]),
    dict(day=22, layout="product", audience="Offices · Government", pillar="Product",
         eyebrow="ductFIT Ceiling", title="Purification above the everyday.",
         specs=[("Mounting", "Ceiling or wall"), ("Designed for", "Spaces without ducts"), ("Setup", "Matched to your space"), ("Ideal for", "Offices & shared spaces")],
         products=["ductfit-ceiling"],
         caption="Out of sight, always working.\n\n"
                 "ductFIT Ceiling is built for spaces without air ducts, with ceiling or wall installation options. Our team assesses your room and recommends the right arrangement.\n\n"
                 "Ideal for offices, waiting areas, classrooms and shared spaces.",
         tags=[TAGS_CORE, TAGS_PRODUCT]),
    dict(day=23, layout="quote", audience="Villas", pillar="Audience",
         eyebrow="For your family", title="The room where your family spends 8 hours every night.",
         products=["ductfit-mobile"],
         caption="We spend about a third of our lives asleep, mostly in a closed bedroom with the AC on.\n\n"
                 "Make that room a priority: measure it with KleanSense and add a ductFIT Mobile or Wall unit for purification.\n\n"
                 "Book a villa air check with our team.",
         tags=[TAGS_CORE, TAGS_VILLA, "#HealthyHome"]),
    dict(day=24, layout="finder", audience="All", pillar="Product",
         eyebrow="Product finder", title="Which ductFIT fits your space?",
         finder=[("Building with HVAC ducts", "ductFIT Vent", "ductfit-vent"),
                 ("Office with grid ceiling", "ductFIT Cloud", "ductfit-cloud"),
                 ("Room without ducts", "Wall · Ceiling · Mobile", "ductfit-wall"),
                 ("Car or personal space", "ductFIT S", "ductfit-s")],
         caption="One technology, many formats. Here's a quick guide:\n\n"
                 "🏢 Building with HVAC ducts → ductFIT Vent\n🧩 Office with grid ceiling → ductFIT Cloud\n🏠 Room without ducts → ductFIT Wall, Ceiling or Mobile\n🚗 Car or personal space → ductFIT S\n🚌 Buses, metro, trains → ductFIT M\n📊 Measure everything → KleanSense\n\n"
                 "Still unsure? Send us a photo of your space and we'll recommend one.",
         tags=[TAGS_CORE, TAGS_PRODUCT]),
    dict(day=25, layout="question", audience="Offices", pillar="Education",
         eyebrow="Moving into a new office?", title="Just finished a fit&#8209;out?", bubble="HCHO",
         body="New furniture, paint and adhesives can release formaldehyde (HCHO) and VOCs. Measure before your team moves in.",
         caption="New office, new furniture, new carpets: congratulations! 🎉\n\n"
                 "Fresh fit-outs can release formaldehyde (HCHO) and other VOCs from materials and adhesives. Before your team moves in, check the readings.\n\n"
                 "KleanSense measures HCHO and TVOC, and our team can recommend purification for the move-in period.\n\n"
                 "Fit-out contractors and interior designers: let's partner.",
         tags=[TAGS_CORE, TAGS_OFFICE, "#FitOut #InteriorDesignDubai"]),
    dict(day=26, layout="hero", audience="Offices · Government", pillar="Audience",
         eyebrow="Wellbeing & ESG", title="Healthy buildings<br>are built on data.",
         body="KleanSense dashboards give you live and historical IAQ data for wellbeing, sustainability and tenant reporting.",
         products=["ductfit-kleansense-iaq-sensor"],
         caption="Wellbeing and sustainability reports are only as good as the data behind them.\n\n"
                 "With KleanSense, your team gets live and historical readings for PM2.5, CO₂, TVOC, HCHO and more in one dashboard, ready for wellbeing programmes, ESG reporting and tenant communication.\n\n"
                 "Pair it with ductFIT purification and you can show what changed after installation.",
         tags=[TAGS_CORE, TAGS_OFFICE, "#ESG #Sustainability #WELLBuilding"]),
    dict(day=27, layout="product", audience="Executives · Fleets", pillar="Product",
         eyebrow="ductFIT S", title="Cleaner air, wherever you go.",
         specs=[("Format", "Portable"), ("For", "Cars & personal spaces"), ("Airflow", "Built-in fan"), ("Technology", "Photocatalytic oxidation")],
         products=["ductfit-s"],
         caption="Dubai commutes can be long. Make the drive better.\n\n"
                 "ductFIT S is a compact, portable purifier for cars and small personal spaces, ideal for executives, chauffeur fleets, VIP transport and hotel cars.\n\n"
                 "A thoughtful corporate gift too 🎁 Ask us about bulk orders.",
         tags=[TAGS_CORE, TAGS_PRODUCT, "#CarAccessories #DubaiDrive"]),
    dict(day=28, layout="product", audience="Government · Transport", pillar="Product",
         eyebrow="ductFIT M", title="Designed for shared journeys.",
         specs=[("Fits", "Existing HVAC grilles"), ("For", "Buses, metro & trains"), ("Build", "Semi-custom configuration"), ("Install", "Retrofit")],
         products=["ductfit-m"],
         caption="Public transport moves the UAE. ductFIT M helps treat the air on the way.\n\n"
                 "A semi-custom unit designed to retrofit into existing HVAC grille systems on buses, metro and trains.\n\n"
                 "Transport authorities and fleet operators: contact us to discuss your vehicle specifications.",
         tags=[TAGS_CORE, TAGS_GOV, "#PublicTransport #Mobility"]),
    dict(day=29, layout="cta", audience="All", pillar="Conversion",
         eyebrow="Book your consultation", title="Let's look at the air in your building.",
         points=["Site visit by our team", "Recommendation for your space", "Monitoring plan & quotation"],
         caption="Ready to take the next step?\n\n"
                 "Book a consultation with Clean Air and we'll:\n✔ Visit your office, villa or facility\n✔ Recommend the right ductFIT units and KleanSense monitoring\n✔ Prepare a clear quotation\n\n"
                 "Comment AIR or send us a DM and our team will reach out.",
         tags=[TAGS_CORE, TAGS_OFFICE, TAGS_VILLA]),
    dict(day=30, layout="range", audience="All", pillar="Brand",
         eyebrow="The complete range", title="Measure. Purify. Review.",
         products=["ductfit-vent", "ductfit-cloud", "ductfit-wall", "ductfit-mobile", "ductfit-lampshade", "ductfit-kleansense-iaq-sensor"],
         caption="From a single villa bedroom to an entire government building, one partner for indoor air.\n\n"
                 "📊 Measure with KleanSense\n🌀 Purify with the ductFIT range: Vent, Cloud, Ceiling, Wall, Mobile, Lampshade, S and M\n🔁 Review results with your team\n\n"
                 "Thank you for following our 30-day series. Which post was most useful? Tell us below 👇",
         tags=[TAGS_CORE, TAGS_PRODUCT]),
]

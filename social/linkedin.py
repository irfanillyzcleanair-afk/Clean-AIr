"""LinkedIn versions of the 30 posts, written for decision makers in offices,
facility management, real estate and government. Use the same image as the
Instagram post of the same day. Post from the company page and reshare from
the founder's / sales lead's personal profile with one line of their own.
"""

LI_FOOTER = "\n\nClean Air Wellness & Hygiene · Dubai\nWhatsApp +971 50 116 9833 · info@cleanairme.com · www.cleanairme.com"

LI = {
1: ("Most organisations measure energy, occupancy and cost per square metre. Very few measure the air their people breathe for eight hours a day.\n\n"
    "Clean Air Wellness & Hygiene supplies ductFIT air purification and KleanSense indoor air quality monitoring across the UAE, from HVAC-integrated units for office towers and public buildings to discreet room units for villas.\n\n"
    "For the next 30 days we'll share practical indoor air guidance for facility managers, HR leaders and property owners. Follow the page to get it in your feed.",
    "#IndoorAirQuality #FacilityManagement #Dubai #UAE #HealthyBuildings"),
2: ("The US EPA estimates that people spend around 90% of their time indoors.\n\n"
    "In the UAE, with long summers, sealed buildings and air conditioning running most of the year, indoor air is the environment we live and work in.\n\n"
    "Yet most buildings have no data on it. A quick question for facility and HR leaders: do you know your office's PM2.5, CO₂ or TVOC levels today?",
    "#IndoorAirQuality #WorkplaceWellbeing #UAE #ESG"),
3: ("Companies compete hard for talent, then put that talent in rooms nobody has measured.\n\n"
    "For offices we combine three things:\n• ductFIT Cloud, which fits standard grid ceiling tiles\n• ductFIT Vent, installed inside the HVAC ducts\n• KleanSense monitors with a live dashboard for the facility team\n\n"
    "No disruption to floor space or interiors. If you manage an office in Dubai or Abu Dhabi, we're happy to walk the floor with you.",
    "#OfficeDesign #EmployeeExperience #FacilityManagement #Dubai"),
4: ("How does ductFIT treat air? Photocatalytic oxidation, in three steps:\n\n"
    "1. Air carrying oxygen and water vapour moves through the unit, using a built-in fan or the building's HVAC airflow.\n"
    "2. UV light activates a catalyst surface.\n"
    "3. The reaction produces low levels of reactive molecules that act on selected contaminants while the unit operates.\n\n"
    "The same principle runs across the range, from in-duct units to standalone room units.",
    "#PCO #AirPurification #HVAC #BuildingTechnology"),
5: ("For buildings with central HVAC, the most discreet place to treat air is inside the ductwork.\n\n"
    "ductFIT Vent installs in ducts or plenums and uses the system's existing airflow. Reference model Vent 100: 29 × 18 × 31 cm, 24 cm inside the duct, max 30 W, with a UV bulb monitoring indicator.\n\n"
    "MEP consultants and facility engineers: send us a duct layout and we'll recommend the right model and quantity.",
    "#HVAC #MEP #FacilityManagement #CommercialRealEstate"),
6: ("Interior designers specify every finish in a villa. Air is rarely on the list.\n\n"
    "Our villa range is built to sit inside the design: a lampshade-style ductFIT unit, wall and ceiling units for rooms without ducts, the standalone ductFIT Mobile, and KleanSense monitoring on the owner's phone.\n\n"
    "We're building partnerships with interior design and fit-out studios in Dubai. If that's you, let's talk about adding indoor air to your specification.",
    "#InteriorDesign #LuxuryRealEstate #DubaiVillas #FitOut"),
7: ("Public buildings carry a particular responsibility: thousands of visitors share the same air every week.\n\n"
    "Our approach for government and public-sector facilities:\n"
    "• Analyse the building, occupancy and HVAC, with baseline monitoring where needed\n"
    "• Create an IAQ plan covering purification and monitoring locations\n"
    "• Execute installation, data access and a post-installation review\n\n"
    "We welcome the chance to give a technical presentation to facility, engineering and sustainability teams.",
    "#PublicSector #SmartCity #UAEGovernment #Sustainability"),
8: ("You can't manage what you don't measure.\n\n"
    "KleanSense tracks eight indoor parameters: PM2.5, TVOC, CO₂, CO, O₃, formaldehyde, temperature and humidity. Readings stream over Wi-Fi to a central dashboard with live data and historical trends.\n\n"
    "For facility teams that means evidence for decisions. For sustainability teams it means data for reporting.",
    "#IAQ #SmartBuildings #ESGReporting #PropTech"),
9: ("PM2.5 in one minute:\n\n"
    "• Particles 2.5 micrometres or smaller, roughly 30 times thinner than a human hair\n"
    "• Common sources: dust and sand events, traffic, construction, cooking, incense\n"
    "• Invisible, so the only way to know indoor levels is to measure them\n\n"
    "If your building reports on wellbeing, PM2.5 is usually the first number people ask about.",
    "#AirQuality #PM25 #HealthyBuildings #UAE"),
10: ("Most Dubai offices have grid ceilings. ductFIT Cloud is designed to drop into one.\n\n"
     "It works independently of the HVAC ducts, has a built-in fan, and keeps desks and floor space clear. That makes it a practical retrofit for open-plan floors, meeting rooms and receptions, with no change to the ductwork.",
     "#OfficeFitOut #Retrofit #FacilityManagement #Dubai"),
11: ("Quick poll for facility managers and building owners: which space would you improve first?\n\n"
     "A) Meeting rooms\nB) Reception and waiting areas\nC) Open-plan floors\nD) Executive offices\n\n"
     "Reply with a letter and your reason. We'll share practical guidance for the most-voted space.",
     "#FacilityManagement #WorkplaceStrategy #Poll"),
12: ("We don't start with a product. We start with the building.\n\n"
     "1. Analyse: space, people, HVAC and, where useful, baseline monitoring or third-party IAQ testing\n"
     "2. Create: a tailored indoor air quality plan\n"
     "3. Execute: installation, configuration and a review of conditions afterwards\n\n"
     "This is how we work with corporate offices, government facilities and multi-villa projects.",
     "#IndoorAirQuality #ProjectDelivery #FacilityManagement"),
13: ("Afternoon meetings feel heavy for a reason that is easy to measure.\n\n"
     "In a full room with the door closed, CO₂ from breathing builds up. CO₂ is a useful indicator of whether a room is ventilated well enough for the number of people in it.\n\n"
     "KleanSense shows CO₂ live, so facility teams can find the rooms that need more fresh air and act on data rather than complaints.",
     "#WorkplaceWellbeing #CO2 #MeetingRooms #FacilityManagement"),
14: ("Not every space can wait for a fit-out.\n\n"
     "ductFIT Mobile is a standalone unit with a built-in fan. No ducts, no ceiling work, no contractor. It suits private offices, clinic rooms, temporary project offices and any room that needs a solution this week.",
     "#AirPurifier #Offices #Clinics #Dubai"),
15: ("Hospitality is central to life in the UAE, and the majlis is where it shows.\n\n"
     "Between bakhoor, food and full gatherings, majlis air works hard. Our lampshade-style ductFIT unit is designed to blend into the interior while it operates.\n\n"
     "Hospitality operators and villa owners: we're happy to recommend a setup for your space.",
     "#Hospitality #Majlis #LuxuryHomes #UAE"),
16: ("Life in the UAE is lived indoors for much of the year: AC running, windows closed, air recirculating.\n\n"
     "Recirculation is efficient for cooling. It also means indoor air quality depends on what's inside the building and how the air is treated.\n\n"
     "The useful part: indoor air can be measured, and it can be improved.",
     "#UAE #BuildingPerformance #IndoorAirQuality"),
17: ("Five questions every facility manager can ask this week:\n\n"
     "1. Do we know our PM2.5, CO₂ and TVOC levels?\n"
     "2. Which rooms have the highest occupancy for the longest time?\n"
     "3. Is our HVAC treating the air, or only cooling it?\n"
     "4. Do we have IAQ data for wellbeing and ESG reporting?\n"
     "5. When did we last review readings after a fit-out?\n\n"
     "Two or more \"not sure\" answers is a good reason to start with monitoring.",
     "#FacilityManagement #ESG #Checklist #HealthyBuildings"),
18: ("For rooms without ducts or spare floor space, ductFIT Wall mounts on the wall, runs independently of the HVAC and circulates air with a built-in fan.\n\n"
     "It is a common choice for private offices, clinic rooms and home offices.",
     "#AirPurification #Clinics #Offices #UAE"),
19: ("TVOC (total volatile organic compounds) is the reading that explains the \"new office smell\".\n\n"
     "Common sources: new furniture, carpets and paint, cleaning products and fresheners, printers and adhesives.\n\n"
     "If you've just completed a fit-out, a TVOC reading before the team moves in is a sensible step.",
     "#FitOut #TVOC #IndoorAirQuality #Dubai"),
20: ("Customer service centres, licensing offices and waiting halls share one thing: many people, shared air, long waits.\n\n"
     "ductFIT Ceiling units treat air where people wait. KleanSense gives teams live data on CO₂, particles and more, supporting data-led facility decisions.\n\n"
     "We welcome enquiries from public-sector facility and procurement teams.",
     "#PublicSector #CustomerHappiness #SmartGovernment #UAE"),
21: ("Myth: if the air looks clean, it is clean.\n\n"
     "Fact: fine particles, CO₂, VOCs and formaldehyde are invisible and often odourless.\n\n"
     "That's why every project we take on starts with measurement.",
     "#IndoorAirQuality #MythVsFact #HealthyBuildings"),
22: ("ductFIT Ceiling is built for spaces without air ducts, with ceiling or wall installation options.\n\n"
     "Our team assesses the room and recommends the arrangement. Typical uses: offices, waiting areas, classrooms and shared spaces.",
     "#AirPurification #Education #Offices #UAE"),
23: ("Bedrooms are the rooms we spend the most continuous hours in, usually closed with the AC on.\n\n"
     "For villa owners and residential developers, the bedroom is the simplest place to start: measure it with KleanSense, then add a ductFIT Mobile or Wall unit if the readings call for it.",
     "#ResidentialRealEstate #DubaiVillas #HealthyHomes"),
24: ("Choosing the right format is simpler than it looks:\n\n"
     "• Building with HVAC ducts → ductFIT Vent\n"
     "• Office with grid ceiling → ductFIT Cloud\n"
     "• Room without ducts → ductFIT Wall, Ceiling or Mobile\n"
     "• Car or personal space → ductFIT S\n"
     "• Buses, metro, trains → ductFIT M\n"
     "• Measuring all of it → KleanSense\n\n"
     "Send us a photo or floor plan and we'll recommend one.",
     "#AirPurification #ProductGuide #FacilityManagement"),
25: ("Moving into a newly fitted-out office?\n\n"
     "New furniture, paint and adhesives can release formaldehyde (HCHO) and other VOCs. Measuring before move-in gives you a clear picture.\n\n"
     "Fit-out contractors and interior designers: we'd like to partner on handover IAQ checks for your clients.",
     "#FitOut #InteriorDesign #Partnership #Dubai"),
26: ("Wellbeing and sustainability reports are only as good as the data behind them.\n\n"
     "KleanSense gives live and historical readings for PM2.5, CO₂, TVOC, HCHO and more in one dashboard, ready for wellbeing programmes, ESG reporting and tenant communication. Paired with ductFIT purification, you can show what changed after installation.",
     "#ESG #Sustainability #WELL #HealthyBuildings"),
27: ("Long commutes are part of working in the UAE.\n\n"
     "ductFIT S is a compact, portable purifier for cars and small personal spaces. It suits executive cars, chauffeur fleets, VIP transport and hotel cars, and it makes a considered corporate gift. Ask us about volume orders.",
     "#CorporateGifts #Fleet #Hospitality #Dubai"),
28: ("Public transport moves the UAE every day.\n\n"
     "ductFIT M is a semi-custom unit designed to retrofit into existing HVAC grille systems on buses, metro and trains.\n\n"
     "Transport authorities and fleet operators: we'd welcome a conversation about your vehicle specifications.",
     "#PublicTransport #Mobility #SmartCity #UAE"),
29: ("If indoor air is on your agenda for 2027, the first step is simple.\n\n"
     "Book a consultation and we will:\n• Visit your office, villa or facility\n• Recommend the right ductFIT units and KleanSense monitoring\n• Prepare a clear quotation\n\n"
     "Message us here on LinkedIn or on WhatsApp.",
     "#IndoorAirQuality #FacilityManagement #Dubai #AbuDhabi"),
30: ("Measure. Purify. Review.\n\n"
     "From a single villa bedroom to an entire government building: KleanSense to measure, the ductFIT range (Vent, Cloud, Ceiling, Wall, Mobile, Lampshade, S and M) to purify, and a review with your team to confirm results.\n\n"
     "Thank you for following our 30-day series. Which topic should we cover in more depth next?",
     "#IndoorAirQuality #HealthyBuildings #UAE"),
}

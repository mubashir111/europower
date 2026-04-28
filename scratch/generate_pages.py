import os
import re

topics = {
    "IT SOLUTIONS": """Europower delivers cutting-edge IT Solutions designed to accelerate Digital Transformation across the Middle East and beyond. Our ERP implementation and IT Consulting services streamline complex business processes for maximum efficiency. We specialize in bespoke App Development and scalable Software Solutions tailored to your industry needs. With rising digital threats, our Cyber Security protocols ensure your data remains protected against global vulnerabilities. Our Website Development team focuses on high-performance interfaces, integrated with advanced SEO and AEO (Answer Engine Optimization) to ensure your brand tops search results. We also offer cloud-based SaaS (Software as a Service) models to provide flexibility and cost-effectiveness. From startups in Dubai to enterprises in Riyadh, we empower businesses with future-ready technology. Our goal is to bridge the gap between innovation and practical application. We ensure your digital infrastructure is robust, secure, and highly scalable. Partner with us for reliable tech support and strategic digital growth. We turn complex technical challenges into seamless user experiences. Enhance your online visibility and operational intelligence with Europower IT.""",

    "INDUSTRIAL SOLUTIONS": """As a leading provider of Industrial Solutions, Europower supports the heavy industries of the Middle East with premium MRO Consumables. We offer high-performance Truck Hydraulics and Industrial Hydraulics designed to withstand the harsh environmental conditions of the region. Our inventory includes world-class Industrial Pumps & Motors that ensure continuous operational uptime. We specialize in Automation Control Systems to optimize production lines and reduce manual overhead. Our selection of specialized Lubricants and Chemicals meets the highest international safety and performance standards. We cater to the Oil & Gas, Construction, and Manufacturing sectors with precision-engineered components. Europower understands the urgency of industrial maintenance, providing rapid delivery of critical parts. We focus on durability to minimize downtime in demanding desert climates. Our technical experts provide guidance on system integration and efficiency upgrades. From hydraulic repairs to full-scale plant automation, we are your trusted partner. We source only from reputed global manufacturers to guarantee quality. Strengthen your industrial operations with our comprehensive product range. Reliability and power are the hallmarks of Europower Industrial.""",

    "MARINE SOLUTIONS": """Europower is a premier supplier of Marine Solutions, serving the bustling maritime hubs from the Arabian Gulf to the Far East. We provide certified Marine Handling Gear and Offshore Lifting Equipment built for extreme sea conditions. Our range of Cargo Handling Gear ensures safe and efficient port operations and logistics. We supply high-quality Ship Parts and Ship Deck Machinery to keep your fleet in peak condition. From heavy-duty Winches to complex anchoring systems, our equipment meets stringent IMO standards. We support the offshore energy sector with specialized rigging and lifting tools. Our team understands the critical nature of maritime schedules, offering 24/7 supply support. We provide technical solutions for vessel maintenance, repair, and overhaul (MRO). Whether you are managing a tanker fleet or offshore platforms, we provide the hardware you need. Our marine products are corrosion-resistant and tested for high-load endurance. We bridge the gap between global manufacturers and local maritime operators. Trust Europower for seamless logistics and high-performance marine engineering. We keep the maritime industry moving with safety and precision.""",

    "HARDWARE SOLUTIONS": """Our Hardware Solutions division provides the essential backbone for construction, oilfields, and heavy engineering projects. We offer a comprehensive range of Rigging Hardware, including shackles, hooks, and turnbuckles for heavy lifting. Europower prioritizes worker safety with high-grade Industrial Oilfield PPE, designed for the rigorous Middle Eastern heat. Our Welding Equipment selection features the latest technology for structural integrity and precision. We are experts in Lifting Equipment, providing slings, chains, and hoists that comply with international safety certifications. Our products are sourced to withstand the high-salinity and high-temperature environments of the Gulf. We serve contractors, fabricators, and site managers who demand reliability and durability. Every piece of hardware undergoes strict quality control to ensure site safety. We offer bulk supply and customized kits for large-scale infrastructure projects. Our inventory is stocked to meet the immediate demands of the energy and mining sectors. Protect your workforce and empower your projects with Europower hardware. We deliver the strength you need to build the future. Quality hardware is not an option; it is a necessity for success.""",

    "HR TRAINING PROGRAMS": """Europower offers comprehensive HR Training Programs designed to elevate the professional standards of the modern workforce. We focus on Human Capital Development to meet the evolving demands of the Middle East’s diverse economy. Our training modules cover essential areas such as Leadership Development, Corporate Governance, and Organizational Behavior. We provide specialized workshops on Soft Skills, communication, and conflict resolution to foster a productive work environment. Our programs are tailored to help companies meet Localization requirements (such as Saudization and Emiratization) by upskilling local talent. We offer both on-site and virtual training sessions to accommodate global teams across Africa and Asia. Our curriculum includes Digital Literacy and the adoption of AI in HR processes for future-ready operations. We provide certified training in Occupational Health and Safety to ensure compliance with international labor standards. Europower’s trainers are industry veterans who bring real-world insights to every classroom. We assist in Performance Management training to help managers conduct effective appraisals and feedback. Our goal is to bridge the skills gap through continuous learning and professional certification. We customize our content to align with your specific corporate culture and strategic objectives. From entry-level onboarding to executive coaching, we cover the full spectrum of professional growth. Our training solutions result in higher employee retention and increased operational efficiency. We empower your staff with the tools needed to navigate a competitive global market. Partner with us to transform your workforce into a strategic asset. Europower is your gateway to excellence in corporate education and skill mastery.""",

    "HUMAN RESOURCE RECRUITMENT": """As a premier Human Resource Recruitment agency, Europower connects world-class talent with leading industries across the globe. We specialize in Talent Acquisition for sectors ranging from Oil & Gas to IT and Construction. Our recruitment network spans Europe, India, and the Far East, providing a truly Global Manpower Solution. We utilize advanced Headhunting techniques to identify executive-level professionals and specialized technical experts. Our team manages the entire Recruitment Life Cycle, from initial sourcing and screening to final placement. We understand the nuances of the Middle Eastern labor market, ensuring full compliance with Visa and Labor Regulations. Europower offers RPO (Recruitment Process Outsourcing) services to streamline your internal hiring departments. We focus on quality over quantity, delivering candidates who match both the skill set and the company culture. Our database includes thousands of pre-vetted professionals ready for deployment in the Middle East and Africa. We provide Contract Staffing and Permanent Placement options to suit your project needs. Our rigorous interview process includes technical assessments and background verification for maximum reliability. We help businesses scale quickly by providing rapid staffing solutions for large-scale infrastructure projects. Our expertise reduces the Time-to-Hire and lowers recruitment costs for our clients. We act as a strategic partner, advising on market salary benchmarks and benefits packages. Trust Europower to build the backbone of your organization with elite human resources. We find the right people to drive your business success in an ever-changing landscape.""",

    "ENGINEERING CONSULTING": """Europower serves as a leading Engineering Consultant, providing high-level technical expertise for complex global projects. Our consultancy services cover the full project lifecycle, from Pre-feasibility Studies to final implementation. We specialize in Mechanical, Electrical, and Structural Engineering designs tailored for harsh environments. Our team provides Technical Audits and risk assessments to ensure your assets are performing at peak efficiency. We assist in Project Management to keep large-scale industrial developments on schedule and within budget. In the Middle East, we focus on Sustainable Engineering and energy-efficient designs to meet regional Green Building standards. Our consultants provide expert advice on System Integration and the modernization of legacy industrial plants. We utilize the latest BIM (Building Information Modeling) and CAD technologies for precision engineering. Europower ensures that all designs comply with Aramco, ADNOC, QP, PDO and International ISO standards. We offer specialized consultancy for the maritime, oilfield, and manufacturing sectors. Our goal is to provide innovative solutions to complex engineering challenges, reducing operational waste. We conduct Value Engineering to optimize costs without compromising on quality or safety. Our global footprint allows us to bring international best practices to local regional projects. We support clients through the Regulatory Approval process with local authorities and municipalities. Whether you need a structural analysis or a complete industrial master plan, we are your trusted advisors. Partner with Europower for engineering excellence that combines global innovation with local expertise. We turn your ambitious engineering concepts into functional, high-performance realities.""",

    "SUPPLY CHAIN OF MRO PRODUCTS": """Europower provides a robust Supply Chain of MRO Products specifically designed to support the continuous operations of Middle Eastern industries. We specialize in the rapid delivery of MRO Consumables to minimize downtime in high-stakes environments like the Oil & Gas sector. Our inventory features high-performance Material Handling equipment that ensures safety and efficiency across warehouses and production lines. We are a leading supplier of Truck Hydraulics and Industrial Hydraulics, offering components that withstand the extreme heat of the GCC region. Our range includes high-efficiency Industrial Pumps & Motors sourced from world-class manufacturers for maximum reliability. We provide advanced Automation Control Systems to help businesses transition toward Industry 4.0 and smart manufacturing. Our supply chain includes specialized Lubricants and Chemicals that meet stringent environmental certifications. We understand that "Time is Money" in the industrial sector, which is why we offer optimized logistics for the UAE, KSA, and beyond. Every product is vetted for durability and compliance with international quality standards. We offer tailored procurement solutions for the manufacturing, mining, and energy sectors. Our digital inventory management ensures that critical spares are always in stock when you need them most. From hydraulic seals to complex motor assemblies, we cover every maintenance requirement. Europower bridges the gap between global innovation and local industrial application. We focus on reducing the Total Cost of Ownership (TCO) for our clients through smarter sourcing. Our logistics network ensures seamless door-to-door delivery across Africa, Asia, and Europe. Trust us for consistent quality and technical support in every transaction. We are your partner in maintaining operational excellence and mechanical integrity. Enhance your maintenance strategy with Europower’s reliable MRO supply chain. We deliver the components that keep the world’s most demanding industries moving forward.""",

    "SUPPLY CHAIN OF INDUSTRIAL PRODUCTS": """Our Supply Chain of Industrial Products is built on the pillars of safety, precision, and heavy-duty performance. We supply a comprehensive range of Hand Tools and Power Tools designed for professional use in construction and fabrication. Europower prioritizes worker safety with a full suite of Industrial PPE and Construction PPE that meets global safety ratings. We offer high-precision Measuring and Testing Instruments essential for quality control in engineering projects. Our inventory includes Heavy Duty Rigging Hardware capable of managing massive loads in challenging environments. We provide reliable Pneumatic & Hydraulic Tools that offer high torque and durability for industrial assembly lines. Safety is paramount, and our Safety & Protective Gear is selected to protect your workforce against site-specific hazards. We serve the building, infrastructure, and oilfield sectors with top-tier hardware and equipment. Our supply chain is optimized for the Middle East, ensuring compliance with regional safety regulations and standards. We offer bulk procurement options for large-scale contractors and government projects. Every tool in our catalog is tested for longevity and ergonomic efficiency. We provide the essential hardware that powers the construction booms in Dubai, Riyadh, and Doha. Our logistics team ensures that your site never stops due to a lack of quality equipment. We source from reputable global brands to guarantee the highest level of craftsmanship. Europower is the preferred choice for procurement managers seeking reliability and competitive pricing. We provide the strength and precision required for modern engineering marvels. Protect your team and empower your projects with our premium industrial hardware. From the smallest hand tool to the heaviest rigging gear, we deliver excellence.""",

    "SUPPLY CHAIN OF MARINE PRODUCTS": """Europower is a dominant force in the Supply Chain of Marine Products, serving major ports and offshore installations globally. We provide certified Marine Handling Gear and Offshore Lifting Equipment designed for the corrosive maritime environment. Our Cargo Handling Gear ensures the safe and swift movement of goods in busy international shipping lanes. We supply a vast array of Ship Parts and Ship Deck Machinery to maintain vessel seaworthiness and operational safety. Our range of heavy-duty Winches and anchoring systems are built to withstand the toughest sea conditions. We specialize in Marine Engine Spares, providing genuine parts to keep your propulsion systems running smoothly. Our inventory includes high-capacity Electric Chain Hoists for efficient shipboard maintenance and cargo movement. We are a key provider of Corrosion Resistant Chain Hoists, essential for long-term durability in high-salinity maritime zones. Every marine product we supply meets IMO standards and international maritime certifications. We support the offshore energy sector with specialized rigging and subsea lifting solutions. Our supply chain is tuned for the urgency of the maritime industry, offering 24/7 logistics support. We bridge the gap between global marine manufacturers and fleet operators in the Arabian Gulf and Far East. From deck to engine room, we provide the components that ensure maritime safety. Our expertise helps reduce vessel turnaround time and prevents costly mechanical failures at sea. Trust Europower for high-quality marine engineering components and seamless logistics. We keep the global maritime industry afloat with precision-engineered solutions. Your fleet deserves the reliability and strength that only Europower can provide. We are the wind in your sails for all maritime procurement needs."""
}

def to_slug(title):
    return title.lower().replace(" ", "-")

base_dir = '/Users/mubashirt/Desktop/industrie-study/industrie.rstheme.com/html'

# Step 1: Update existing HTML files (remove modal, update mega menus)
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# Title to slug map for replacing mega menus
title_to_slug = {k: to_slug(k) for k in topics.keys()}

for file in html_files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update mega menus. We match <h5 class="... service-topic-link" ...> ... </h5>
    # This regex is a bit tricky, but since we know the titles, we can do a targeted replacement.
    for title, slug in title_to_slug.items():
        # Sometimes it's Title Case in HTML
        # Let's do a case-insensitive replace of the whole H5 tag
        # e.g., <h5 class="title service-topic-link" ...>IT Solutions</h5> or with <a> inside
        # We will use re.sub with IGNORECASE
        pattern1 = r'<h5([^>]*class="[^"]*service-topic-link[^"]*"[^>]*)>\s*' + re.escape(title) + r'\s*</h5>'
        repl1 = f'<h5\\1><a href="{slug}.html" style="color: inherit; text-decoration: none;">{title.title()}</a></h5>'
        content = re.sub(pattern1, repl1, content, flags=re.IGNORECASE)

        pattern2 = r'<h5([^>]*class="[^"]*service-topic-link[^"]*"[^>]*)>\s*<a[^>]*>\s*' + re.escape(title) + r'\s*</a>\s*</h5>'
        repl2 = f'<h5\\1><a href="{slug}.html" style="color: inherit; text-decoration: none;">{title.title()}</a></h5>'
        content = re.sub(pattern2, repl2, content, flags=re.IGNORECASE)

    # 2. Remove script tag
    content = re.sub(r'<script\s+src="assets/js/custom-services\.js"></script>', '', content)

    # 3. Remove modal HTML. It looks like:
    # <!-- Modal --> ... <div class="modal fade" id="serviceModal" ...> ... </div>
    # Let's just remove anything from id="serviceModal" to its matching end.
    # A simple regex for the modal block if it exists:
    content = re.sub(r'<!--\s*Service Modal\s*-->.*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    # Also just find id="serviceModal" and try to wipe it out broadly:
    content = re.sub(r'<div class="modal fade" id="serviceModal".*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Step 2: Create new pages based on the UPDATED about.html (so they have the correct menus)
with open(os.path.join(base_dir, 'about.html'), 'r', encoding='utf-8') as f:
    about_content = f.read()

# Replace the inner content
for title, text in topics.items():
    slug = to_slug(title)
    display_title = title.title()

    new_content = about_content

    # Change page title
    new_content = re.sub(r'<title>.*?</title>', f'<title>EUROPOWER - {display_title}</title>', new_content)

    # Change breadcrumb title
    new_content = re.sub(r'<h1 class="rs-breadcrumb-title">About Us</h1>', f'<h1 class="rs-breadcrumb-title">{display_title}</h1>', new_content)
    new_content = re.sub(r'<li><span>About Us</span></li>', f'<li><span>{display_title}</span></li>', new_content)

    # Replace body content. Look for <!-- about area start --> ... <!-- blog area end -->
    section_html = f"""
        <!-- service details area start -->
        <section class="rs-service-details-area section-space">
            <div class="container">
                <div class="row g-5 justify-content-center">
                    <div class="col-xl-10 col-lg-10">
                        <div class="rs-service-details-content">
                            <h2 class="rs-service-details-title">{display_title}</h2>
                            <p style="font-size: 18px; line-height: 1.8; color: #555;">
                                {text}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- service details area end -->
"""
    new_content = re.sub(r'<!-- about area start -->.*?<!-- blog area end -->', section_html, new_content, flags=re.DOTALL)

    # Also remove any remaining `menu-item-has-children` active class from "About Us" if applicable
    # Just to be clean.

    with open(os.path.join(base_dir, f'{slug}.html'), 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Generated 10 pages and updated HTML files!")

import os
import re

nav_html = """
                                <li><a href="index.html">Home</a></li>
                                <li><a href="about.html">About Us</a></li>
                                <li class="has-mega-menu menu-item-has-children">
                                    <a href="index.html#services">Services</a>
                                    <ul class="mega-menu mega-grid">
                                        <li>
                                            <h5 class="title">Services</h5>
                                            <ul>
                                                <li><a href="about.html">IT Consulting</a></li>
                                                <li><a href="about.html">Technical Support</a></li>
                                                <li><a href="about.html">Cloud Services</a></li>
                                                <li><a href="about.html">Branding & Logo Design</a></li>
                                                <li><a href="about.html">Web Development</a></li>
                                                <li><a href="about.html">Mobile App Development</a></li>
                                                <li><a href="products.html">Strategic Sourcing</a></li>
                                                <li><a href="products.html">Industrial MRO Supply</a></li>
                                                <li><a href="products.html">TCO Optimization</a></li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li class="has-mega-menu menu-item-has-children">
                                    <a href="about.html">Consulting</a>
                                    <ul class="mega-menu mega-grid">
                                        <li>
                                            <h5 class="title">Consulting</h5>
                                            <ul>
                                                <li><a href="about.html">HR Consulting</a></li>
                                                <li><a href="about.html">Payroll Management</a></li>
                                                <li><a href="about.html">HRMS Automation</a></li>
                                                <li><a href="about.html">PRO Services</a></li>
                                                <li><a href="about.html">Engineering Consulting</a></li>
                                                <li><a href="about.html">Technical Expertise</a></li>
                                                <li><a href="about.html">Project Support</a></li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li><a href="contact.html">Contact</a></li>"""

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Target all <ul class="multipage-menu">...</ul> sections
    # and replace them with our unified menu.
    # We use a pattern that matches the whole ul block including its contents.
    new_content = re.sub(r'<ul class="multipage-menu">.*?</ul>', f'<ul class="multipage-menu">{nav_html}\n                            </ul>', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"All menus synchronized in {filename}")
    else:
        print(f"Skipped {filename}")

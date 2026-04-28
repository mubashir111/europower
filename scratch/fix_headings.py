import os
import re

topics = [
    "IT SOLUTIONS",
    "INDUSTRIAL SOLUTIONS",
    "MARINE SOLUTIONS",
    "HARDWARE SOLUTIONS",
    "HR TRAINING PROGRAMS",
    "HUMAN RESOURCE RECRUITMENT",
    "ENGINEERING CONSULTING",
    "SUPPLY CHAIN OF MRO PRODUCTS",
    "SUPPLY CHAIN OF INDUSTRIAL PRODUCTS",
    "SUPPLY CHAIN OF MARINE PRODUCTS"
]

def to_slug(title):
    return title.lower().replace(" ", "-")

base_dir = '/Users/mubashirt/Desktop/industrie-study/industrie.rstheme.com/html'

html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

title_to_slug = {k: to_slug(k) for k in topics}

for file in html_files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for title, slug in title_to_slug.items():
        # Match <h5 class="title"...>Title</h5> (NO <a> tag inside)
        # Note: We don't require service-topic-link
        pattern1 = r'<h5([^>]*class="[^"]*title[^"]*"[^>]*)>\s*' + re.escape(title) + r'\s*</h5>'
        repl1 = f'<h5\\1><a href="{slug}.html" style="color: inherit; text-decoration: none;">{title.title()}</a></h5>'
        content = re.sub(pattern1, repl1, content, flags=re.IGNORECASE)

        # Match <h5 class="title"...>Title</h5> (Sometimes class="title service-topic-link")
        # In case the regex didn't catch it because of spacing or something.
        
        # Let's also make sure we don't double link. If it already has <a href="it-solutions.html"> inside, we skip.
        # But our pattern1 doesn't match if there is an <a> tag because we don't have <a> in the regex.
        
        # Another case: what about "Hardware Solution" instead of "Hardware Solutions"?
        # Let's check for slight variations if needed.
        if title == "HARDWARE SOLUTIONS":
            pattern_var = r'<h5([^>]*class="[^"]*title[^"]*"[^>]*)>\s*Hardware Solution\s*</h5>'
            repl_var = f'<h5\\1><a href="hardware-solutions.html" style="color: inherit; text-decoration: none;">Hardware Solutions</a></h5>'
            content = re.sub(pattern_var, repl_var, content, flags=re.IGNORECASE)
            
        if title == "INDUSTRIAL SOLUTIONS":
            pattern_var = r'<h5([^>]*class="[^"]*title[^"]*"[^>]*)>\s*Industrial Solution\s*</h5>'
            repl_var = f'<h5\\1><a href="industrial-solutions.html" style="color: inherit; text-decoration: none;">Industrial Solutions</a></h5>'
            content = re.sub(pattern_var, repl_var, content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed missed headings in all HTML files!")

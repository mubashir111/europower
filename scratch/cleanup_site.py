import os
import re

def clean_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace industries.html with index.html#services (already done but safe to repeat)
    content = content.replace('industries.html', 'index.html#services')

    # 2. Remove social media blocks (active and commented)
    patterns = [
        r'<!--\s*<div class="rs-footer-social">.*?</div>\s*-->',
        r'<!--\s*<div class="rs-theme-social.*?</div>\s*-->',
        r'<!--\s*<div class="offcanvas-social">.*?</div>\s*-->',
        r'<!--\s*<div class="rs-contact-social-wrapper">.*?</div>\s*-->',
        r'<div class="rs-theme-social.*?</div>',
        r'<div class="rs-footer-social">.*?</div>',
        r'<div class="offcanvas-social">.*?</div>',
        r'<div class="rs-contact-social-wrapper.*?</div>'
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)

    # 3. Specific cleanup for about.html (already done but safe to repeat)
    if filepath.endswith('about.html'):
        content = re.sub(r'<!-- history area start -->.*?<!-- history area end -->', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- counter area start -->.*?<!-- counter area end -->', '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for html_file in html_files:
        print(f"Cleaning {html_file}...")
        clean_html_file(html_file)

if __name__ == "__main__":
    main()

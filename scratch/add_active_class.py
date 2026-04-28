import os
import re

base_dir = '/Users/mubashirt/Desktop/industrie-study/industrie.rstheme.com/html'

# The list of target HTML files that are in our mega menu topics
target_files = [
    'it-solutions.html',
    'industrial-solutions.html',
    'marine-solutions.html',
    'hardware-solutions.html',
    'hr-training-programs.html',
    'human-resource-recruitment.html',
    'engineering-consulting.html',
    'supply-chain-of-mro-products.html',
    'supply-chain-of-industrial-products.html',
    'supply-chain-of-marine-products.html'
]

# Function to add class="active" to the matching anchor tag
for filename in target_files:
    file_path = os.path.join(base_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # We first need to remove any existing class="active" from other mega menu links in this file, just to be safe
        # Although right now none of them have it. Let's just be direct.

        # Find the specific a tag: <a href="filename.html" ...>
        # and ensure it has class="active".
        # E.g. <a href="it-solutions.html" style="color: inherit; text-decoration: none;">
        
        # It's safer to just regex replace the specific href for this file.
        # Pattern: look for href="filename"
        pattern = r'(<a\s+href="{})"([^>]*)>'.format(re.escape(filename))
        
        def add_active_class(match):
            # If it already has class="active", do nothing.
            # Otherwise, add class="active" before the other attributes.
            href_part = match.group(1) + '"'
            rest = match.group(2)
            if 'class="active"' not in rest:
                return f'{href_part} class="active"{rest}>'
            return match.group(0)

        new_content = re.sub(pattern, add_active_class, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added active class in {filename}")
        else:
            print(f"No changes needed for {filename}")


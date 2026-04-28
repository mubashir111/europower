import os
import re

base_dir = '/Users/mubashirt/Desktop/industrie-study/industrie.rstheme.com/html'

html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# We want to replace `<li...><a href="javascript:void(0)" ...>Text</a></li>` with `<li style="...">Text</li>`
# And similarly for `products.html` where it is a sub-item (we assume all `products.html` links in the dropdown are sub-items, wait, what if "Products" itself links to products.html? No, the mega menu trigger is `<a style="cursor:default;">Products</a>`).

for file in html_files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace all `javascript:void(0)` links inside lists
    pattern1 = r'<li([^>]*)>\s*<a[^>]*href="javascript:void\(0\)"[^>]*>(.*?)</a>\s*</li>'
    # Force the style to match the user's manual fix for consistency
    repl1 = r'<li style="padding: 6px 0; font-size: 15px; color: #555; display: block; border: none; line-height: 1.4;">\n                                                    \2</li>'
    content = re.sub(pattern1, repl1, content, flags=re.IGNORECASE)

    # Find and replace all `products.html` links inside lists
    pattern2 = r'<li([^>]*)>\s*<a[^>]*href="products\.html"[^>]*>(.*?)</a>\s*</li>'
    repl2 = r'<li style="padding: 6px 0; font-size: 15px; color: #555; display: block; border: none; line-height: 1.4;">\n                                                    \2</li>'
    content = re.sub(pattern2, repl2, content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sub-item links removed successfully.")

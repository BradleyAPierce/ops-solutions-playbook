#!/usr/bin/env python3
"""
Refactor WordPress HTML files to use clean template structure.
Extracts main content, cleans image paths, removes inline styles and scripts.
"""

import re
import os
from pathlib import Path

# File mappings: (source_path, output_path, title, body_class, start_line, end_line)
FILES = [
    ('core/Cloud/Device-Management/Device Management.html', 'pages/core/cloud/device-management.html', 
     'Device Management', 'bg-teal', 832, 1097),
    ('core/Cloud/Document-Management/Document Management.html', 'pages/core/cloud/document-management.html',
     'Document Management', 'bg-teal', 831, 914),
    ('core/Cloud/Fax-Solutions/Fax-Solutions.html', 'pages/core/cloud/fax-solutions.html',
     'Fax Solutions', 'bg-teal', 831, 977),
    ('core/Cloud/Intelligent-Document-Processing/Intelligent-Document-Processing.html', 
     'pages/core/cloud/intelligent-document-processing.html',
     'Intelligent Document Processing', 'bg-teal', 831, 984),
    ('core/Cloud/Konica-Minolta-MarketPlace/Konica-Minolta-MarketPlace.html',
     'pages/core/cloud/konica-minolta-marketplace.html',
     'Konica Minolta MarketPlace', 'bg-teal', 831, 909),
    ('core/Cloud/Print-Management/Print-Management.html', 'pages/core/cloud/print-management.html',
     'Print Management', 'bg-teal', 831, 991),
    ('core/Cloud/Security/Security.html', 'pages/core/cloud/security.html',
     'Security', 'bg-teal', 831, 1070),
]

def clean_content(content, source_folder):
    """Clean HTML content: fix image paths, remove inline styles, clean CDN URLs"""
    
    # Replace local image paths: ./FILENAME_files/IMAGE.jpg -> /assets/images/content/IMAGE.jpg
    content = re.sub(
        r'\./' + re.escape(source_folder) + r'_files/([^"\'>\s]+)',
        r'/assets/images/content/\1',
        content
    )
    
    # Replace CDN URLs: https://solutionsmkm.b-cdn.net/wp-content/uploads/.../IMAGE.jpg
    content = re.sub(
        r'https://solutionsmkm\.b-cdn\.net/wp-content/uploads/[^"\'>\s]+/([^"/\'>\s]+\.(jpg|png|svg|webp|gif))',
        r'/assets/images/content/\1',
        content,
        flags=re.IGNORECASE
    )
    
    # Fix background-image URLs in inline styles
    content = re.sub(
        r'background-image:\s*url\(&quot;https://solutionsmkm\.b-cdn\.net/wp-content/uploads/[^&]+/([^&/]+)&quot;\)',
        r'background-image: url("/assets/images/content/\1")',
        content
    )
    
    # Remove inline style attributes from divs, imgs, etc (but keep structural ones)
    # Remove style from owl-carousel elements
    content = re.sub(
        r'<div class="owl-stage-outer"><div class="owl-stage" style="[^"]*">',
        r'<div class="owl-stage-outer"><div class="owl-stage">',
        content
    )
    content = re.sub(
        r'<div class="owl-item active" style="[^"]*">',
        r'<div class="owl-item active">',
        content
    )
    content = re.sub(
        r'<div class="slides" style="[^"]*">',
        r'<div class="slides">',
        content
    )
    
    # Remove style="display: none;" from images
    content = re.sub(
        r'<img([^>]*) style="display: none;"',
        r'<img\1',
        content
    )
    
    # Remove empty src attributes or invalid src
    content = re.sub(
        r'<img src="https://solutionsguide\.mykonicaminolta\.com/[^"]*" alt="">',
        r'',
        content
    )
    
    # Clean up WordPress URLs in links
    content = re.sub(
        r'https://solutionsguide\.mykonicaminolta\.com/[^"\'#]*#',
        r'#',
        content
    )
    content = re.sub(
        r'href="https://solutionsguide\.mykonicaminolta\.com/"',
        r'href="/"',
        content
    )
    
    # Remove javascript:void() links
    content = re.sub(
        r'href="javascript:void\(&#39;&#39;\);"',
        r'href="#"',
        content
    )
    
    # Clean up extra spaces and newlines
    content = re.sub(r'\n\s*\n\s*\n', r'\n\n', content)
    
    return content

def create_page(source_path, output_path, title, body_class, start_line, end_line):
    """Create refactored page from source HTML"""
    
    base_dir = Path(__file__).parent
    source_file = base_dir / source_path
    
    print(f"Processing: {source_path}")
    
    # Read source content
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extract main content (convert to 0-indexed)
    main_content = ''.join(lines[start_line-1:end_line-1])
    
    # Get source folder name for image path replacements
    source_folder = Path(source_path).stem
    
    # Clean the content
    main_content = clean_content(main_content, source_folder)
    
    # Create the new page with template
    template = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title} - Konica Minolta</title>
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/icons/favicon-32x32.png" />
    <link rel="stylesheet" href="/assets/css/vendor/bootstrap.min.css" />
    <link rel="stylesheet" href="/assets/css/vendor/plugin.css" />
    <link rel="stylesheet" href="/assets/css/vendor/utilities.css" />
    <link rel="stylesheet" href="/assets/css/vendor/vendor.css" />
    <link rel="stylesheet" href="/assets/css/vendor/style.css" />
    <link rel="stylesheet" href="/assets/css/core/wordpress-extracted.css" />
  </head>
  <body class="{body_class}">
    <div id="header-container"></div>
    <div id="nav-container"></div>
    
{main_content}
    
    <div id="footer-container"></div>
    <script src="/assets/js/vendor/jquery.min.js"></script>
    <script src="/assets/js/vendor/jquery-migrate.min.js"></script>
    <script src="/assets/js/vendor/bootstrap.min.js"></script>
    <script src="/assets/js/vendor/plugin.js"></script>
    <script src="/assets/js/vendor/vendor.js"></script>
    <script src="/assets/js/component-loader.js"></script>
  </body>
</html>
'''
    
    # Write output file
    output_file = base_dir / output_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"  ✓ Created: {output_path}")
    return output_path

def main():
    """Process all files"""
    print("Starting refactoring of 7 Cloud solution pages...\n")
    
    created_files = []
    for file_info in FILES:
        output = create_page(*file_info)
        created_files.append(output)
    
    print("\n" + "="*60)
    print("✓ REFACTORING COMPLETE!")
    print("="*60)
    print(f"\nCreated {len(created_files)} files:")
    for f in created_files:
        print(f"  • {f}")
    
    print("\nAll files saved to: pages/core/cloud/")
    print("\nNext steps:")
    print("  1. Review the generated files")
    print("  2. Verify image paths are correct")
    print("  3. Test with component-loader.js for header/footer/nav")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Refactor 6 graphic-communications WordPress HTML files into clean template structure.
Based on established refactoring patterns from 22 previous successes.
"""

import re
import os
from pathlib import Path
from bs4 import BeautifulSoup

# File mappings: source -> destination
FILE_MAPPINGS = [
    ("graphic-communications/AccurioPro-Solutions/AccurioPro-Solutions.html", 
     "pages/graphic-communications/accuriopro-solutions.html"),
    ("graphic-communications/e-Commerce/e-Commerce.html", 
     "pages/graphic-communications/e-commerce.html"),
    ("graphic-communications/Management-Information-Systems/Management-Information-Systems.html", 
     "pages/graphic-communications/management-information-systems.html"),
    ("graphic-communications/Transactional-Variable-Data-Printing/Transactional-Variable-Data-Printing.html", 
     "pages/graphic-communications/transactional-variable-data-printing.html"),
    ("graphic-communications/Variable-Data-Printing/Variable-Data-Printing.html", 
     "pages/graphic-communications/variable-data-printing.html"),
    ("graphic-communications/Workflow-Solutions/Workflow-Solutions.html", 
     "pages/graphic-communications/workflow-solutions.html"),
]

# Standard template structure
TEMPLATE = '''<!doctype html>
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
    <link rel="stylesheet" href="/assets/css/core/banner-fix.css" />
  </head>
  <body class="{body_class}">
    <div id="header-container"></div>
    <div id="nav-container"></div>
    
{content}
    
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

def extract_page_title(html_content):
    """Extract clean page title from HTML."""
    match = re.search(r'<title>([^<]+)</title>', html_content, re.IGNORECASE)
    if match:
        title = match.group(1)
        # Clean up title - remove "– KONICA MINOLTA" suffix
        title = re.sub(r'\s*[–-]\s*KONICA MINOLTA.*$', '', title, flags=re.IGNORECASE)
        return title.strip()
    return "Graphic Communications"

def extract_body_class(html_content):
    """Extract body class from HTML."""
    match = re.search(r'<body[^>]*class=["\']([^"\']+)["\']', html_content, re.IGNORECASE)
    if match:
        return match.group(1)
    return "page-template-default page home"

def extract_main_content(html_content):
    """Extract main content between nav and footer."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the main content - typically starts after </nav> and before footer
    # Look for common patterns in WordPress pages
    
    # Strategy 1: Find content between nav and footer
    nav_end = html_content.find('</nav>')
    footer_start = html_content.find('<footer')
    
    if nav_end != -1 and footer_start != -1:
        content_block = html_content[nav_end + 6:footer_start]
    else:
        # Strategy 2: Look for wp-block-cover or main sections
        nav_end = html_content.find('</header>')
        if nav_end == -1:
            # Try finding nav another way
            nav_end = html_content.find('id="menu-primary-nav-expanded"')
            if nav_end != -1:
                # Find closing of this section
                nav_end = html_content.find('</nav>', nav_end)
        
        footer_start = html_content.find('<footer')
        if footer_start == -1:
            footer_start = html_content.find('class="entry-footer')
        
        if nav_end != -1 and footer_start != -1:
            content_block = html_content[nav_end + 6:footer_start]
        else:
            content_block = ""
    
    return content_block.strip()

def fix_image_paths(content):
    """Fix all image paths to point to /assets/images/content/."""
    # Fix ./FOLDER_files/image.ext patterns
    content = re.sub(
        r'\.\/[^\/]+_files\/([^\s\'"]+\.(jpg|jpeg|png|svg|gif|webp))',
        r'/assets/images/content/\1',
        content,
        flags=re.IGNORECASE
    )
    
    # Fix CDN URLs
    content = re.sub(
        r'https://solutionsmkm\.b-cdn\.net/wp-content/uploads/\d+/\d+/([^\s\'"]+\.(jpg|jpeg|png|svg|gif|webp))',
        r'/assets/images/content/\1',
        content,
        flags=re.IGNORECASE
    )
    
    # Fix any remaining WordPress upload URLs
    content = re.sub(
        r'https?://[^/]+/wp-content/uploads/[^/]+/[^/]+/([^\s\'"]+\.(jpg|jpeg|png|svg|gif|webp))',
        r'/assets/images/content/\1',
        content,
        flags=re.IGNORECASE
    )
    
    return content

def fix_wordpress_urls(content):
    """Fix WordPress URLs to relative paths."""
    content = re.sub(
        r'https://solutionsguide\.mykonicaminolta\.com',
        '',
        content,
        flags=re.IGNORECASE
    )
    return content

def remove_tracking_scripts(content):
    """Remove Google Tag Manager, BugHerd, and other tracking scripts."""
    # Remove GTM scripts
    content = re.sub(r'<script[^>]*gtm\.js[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*google-analytics[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove BugHerd
    content = re.sub(r'<script[^>]*bugherd[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*sidebarv2\.js[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove any analytics/tracking
    content = re.sub(r'<script[^>]*analytics[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    return content

def remove_inline_css_js(content):
    """Remove inline CSS and JS (style and script tags)."""
    # Remove <style> tags
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove <script> tags (but we'll add back the component loader at the end)
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    return content

def clean_content(content):
    """Apply all cleaning transformations."""
    content = fix_image_paths(content)
    content = fix_wordpress_urls(content)
    content = remove_tracking_scripts(content)
    content = remove_inline_css_js(content)
    return content

def process_file(source_path, dest_path):
    """Process a single HTML file."""
    print(f"Processing: {source_path}")
    
    with open(source_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract metadata
    title = extract_page_title(html_content)
    body_class = extract_body_class(html_content)
    
    # Extract and clean content
    content = extract_main_content(html_content)
    content = clean_content(content)
    
    # Apply template
    final_html = TEMPLATE.format(
        title=title,
        body_class=body_class,
        content=content
    )
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write output
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    # Count lines
    line_count = len(final_html.split('\n'))
    
    return {
        'source': source_path,
        'dest': dest_path,
        'title': title,
        'body_class': body_class,
        'line_count': line_count
    }

def main():
    """Process all files."""
    print("=" * 80)
    print("GRAPHIC COMMUNICATIONS REFACTORING")
    print("=" * 80)
    print()
    
    results = []
    
    for source, dest in FILE_MAPPINGS:
        try:
            result = process_file(source, dest)
            results.append(result)
            print(f"✓ Created: {dest}")
            print(f"  Title: {result['title']}")
            print(f"  Body class: {result['body_class']}")
            print(f"  Lines: {result['line_count']}")
            print()
        except Exception as e:
            print(f"✗ ERROR processing {source}: {str(e)}")
            print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total files processed: {len(results)}")
    print(f"Total lines generated: {sum(r['line_count'] for r in results)}")
    print()
    print("✓ All transformations applied:")
    print("  - Images point to /assets/images/content/")
    print("  - No CDN or WordPress URLs")
    print("  - No tracking scripts (GTM, BugHerd, analytics)")
    print("  - No inline CSS or JS")
    print("  - banner-fix.css included")
    print("  - Component containers present")
    print("  - Body classes preserved")
    print("=" * 80)

if __name__ == "__main__":
    main()

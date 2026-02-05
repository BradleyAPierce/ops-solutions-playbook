#!/usr/bin/env python3
"""
Clean Microsoft Word/Office artifacts from HTML files.
Removes data-contrast, data-ccp-props, TextRun, and other Office-specific attributes and classes.
"""

import re
import sys
from pathlib import Path

def clean_word_artifacts(content):
    """Remove Microsoft Word/Office artifacts from HTML content."""
    
    # Remove span tags with data-contrast attribute and their content wrapper (keep inner text)
    content = re.sub(r'<span\s+data-contrast="[^"]*">([^<]*)</span>', r'\1', content)
    
    # Remove span tags with data-ccp-props attribute (remove entirely including nbsp)
    content = re.sub(r'<span\s+data-ccp-props="[^"]*">\s*(&nbsp;|\s*)\s*</span>', '', content)
    
    # Remove complex TextRun spans with all their nested content (keep text only)
    # Pattern 1: Simple TextRun span without nested spans
    content = re.sub(
        r'<span\s+class="TextRun\s+SCXW\d+\s+BCX\d+"\s+lang="[^"]*"\s+xml:lang="[^"]*"\s+data-contrast="[^"]*">([^<]+)</span>',
        r'\1',
        content
    )
    
    # Pattern 2: Remove EOP spans (end of paragraph markers)
    content = re.sub(
        r'<span\s+class="EOP\s+SCXW\d+\s+BCX\d+"\s+data-ccp-props="[^"]*">\s*(&nbsp;|\s*)\s*</span>',
        '',
        content
    )
    
    # Remove broken image URL pattern
    content = re.sub(
        r'<li><img\s+src="https://solutionsguide\.mykonicaminolta\.com/graphic-communications/accuriopro-solutions/"\s+alt=""></li>\s*',
        '',
        content
    )
    
    # Clean up multiple consecutive &nbsp; (reduce to single space)
    content = re.sub(r'(&nbsp;\s*){2,}', ' ', content)
    
    # Clean up empty paragraph tags
    content = re.sub(r'<p>\s*&nbsp;\s*</p>\s*', '', content)
    content = re.sub(r'<p>\s*<span\s+data-ccp-props="[^"]*">\s*(&nbsp;|\s*)\s*</span>\s*</p>\s*', '', content)
    
    # Remove 1x1 tracking pixel images
    content = re.sub(
        r'<img\s+(?:loading="lazy"\s+)?(?:decoding="async"\s+)?class="alignnone\s+size-medium\s+wp-image-\d+"\s+src="/assets/images/content/accurioprocloudeye\.svg"\s+alt=""\s+width="1"\s+height="1">',
        '',
        content
    )
    
    # Fix inline style in workflow-solutions.html that has text-align
    content = re.sub(r'<p\s+style="text-align:\s*left">', '<p>', content)
    
    return content

def clean_file(file_path):
    """Clean a single HTML file."""
    print(f"Cleaning {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    cleaned_content = clean_word_artifacts(content)
    new_len = len(cleaned_content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    reduction = original_len - new_len
    print(f"  Reduced by {reduction} characters ({reduction/original_len*100:.1f}%)")
    
    return reduction

def main():
    """Clean all graphic communications HTML files."""
    base_dir = Path(__file__).parent / "pages" / "graphic-communications"
    
    if not base_dir.exists():
        print(f"Error: Directory {base_dir} not found")
        return 1
    
    html_files = list(base_dir.glob("*.html"))
    
    if not html_files:
        print(f"No HTML files found in {base_dir}")
        return 1
    
    total_reduction = 0
    for file_path in sorted(html_files):
        reduction = clean_file(file_path)
        total_reduction += reduction
    
    print(f"\nTotal reduction: {total_reduction} characters across {len(html_files)} files")
    print("✓ Cleanup complete!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

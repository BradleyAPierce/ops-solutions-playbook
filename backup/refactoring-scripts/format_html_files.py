#!/usr/bin/env python3
"""Format HTML files with consistent 2-space indentation."""

import re
from pathlib import Path

def format_html_file(filepath):
    """Format an HTML file with 2-space indentation."""
    print(f"Formatting: {filepath.name}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into lines and process
        lines = content.split('\n')
        formatted_lines = []
        indent_level = 0
        
        # Tags that increase indentation
        opening_tags = r'<(html|head|body|div|section|header|footer|nav|ul|ol|li|table|thead|tbody|tr|td|th|form|select|article|main|aside)[\s>]'
        # Tags that decrease indentation
        closing_tags = r'</(html|head|body|div|section|header|footer|nav|ul|ol|li|table|thead|tbody|tr|td|th|form|select|article|main|aside)>'
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            
            # Decrease indent for closing tags
            if re.match(closing_tags, stripped):
                indent_level = max(0, indent_level - 1)
            
            # Add the line with proper indentation
            formatted_lines.append('  ' * indent_level + stripped)
            
            # Increase indent for opening tags (but not self-closing)
            if re.search(opening_tags, stripped) and not re.search(r'/>\s*$', stripped) and not re.search(closing_tags, stripped):
                indent_level += 1
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(formatted_lines) + '\n')
        
        print(f"  ✓ Done")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    """Format all graphic communications HTML files."""
    base_dir = Path(__file__).parent / "pages" / "graphic-communications"
    html_files = sorted(base_dir.glob("*.html"))
    
    print("=" * 60)
    print("HTML Formatting")
    print("=" * 60)
    
    success = sum(1 for f in html_files if format_html_file(f))
    
    print("=" * 60)
    print(f"✓ Formatted {success}/{len(html_files)} files")
    return 0

if __name__ == "__main__":
    main()

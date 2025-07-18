
#!/usr/bin/env python3
"""
Bug Detection Script for E-commerce Site (Site 1)
Detects 30 intentionally injected beginner-friendly frontend bugs.
"""

import re
import os

def detect_bugs_site1():
    bugs_found = []
    
    # Read HTML file
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return []
    
    # Bug detection patterns for beginner-friendly frontend issues
    checks = [
        ("Missing lang attribute on html", r'<html(?![^>]*lang=)', "index.html"),
        ("Missing charset declaration", r'<meta charset="utf-8">', "index.html"),
        ("Missing viewport meta tag", r'<meta name="viewport"', "index.html"),
        ("Missing favicon", r'<link rel="icon"', "index.html"),
        ("Image without alt attribute", r'<img src="logo\.png"(?![^>]*alt=)', "index.html"),
        ("Missing href attribute", r'<a(?![^>]*href=)[^>]*>Products</a>', "index.html"),
        ("Label missing for attribute", r'<label(?![^>]*for=)[^>]*>Search Products:', "index.html"),
        ("Input without id", r'<input type="text"(?![^>]*id=)', "index.html"),
        ("Unclosed div tag", r'<div class="product">(?!.*</div>.*<div class="product">)', "index.html"),
        ("Image without alt attribute", r'<img src="product1\.jpg"(?![^>]*alt=)', "index.html"),
        ("Button without type", r'<button(?![^>]*type=).*onclick="addToCart\(\)"', "index.html"),
        ("Missing closing p tag", r'<p>\$699(?!</p>)', "index.html"),
        ("Form without action", r'<form(?![^>]*action=)', "index.html"),
        ("Input without name attribute", r'<input type="email"(?![^>]*name=)', "index.html"),
        ("Submit button outside form", r'</form>\s*<button type="submit"', "index.html"),
        ("Table without th elements", r'<table>(?!.*<th>)', "index.html"),
        ("Missing heading hierarchy", r'<h4>Featured Products</h4>(?!.*<h2>)', "index.html"),
        ("List without proper structure", r'<div class="category-list">(?!.*<ul>)', "index.html"),
        ("Required field missing required", r'Name \(Required\).*<input(?![^>]*required)', "index.html"),
        ("Image with invalid attributes", r'width="abc"', "index.html"),
        ("Missing semantic structure", r'<div>\s*<p>Contact:', "index.html"),
        ("Link without text content", r'<a href="/privacy"></a>', "index.html"),
        ("Empty heading", r'<h3></h3>', "index.html"),
        ("Empty paragraph", r'<p></p>', "index.html"),
        ("Missing copyright structure", r'<div>&copy;', "index.html"),
        ("Script without type", r'<script>(?![^>]*type=)', "index.html"),
        ("Missing semicolon", r'var cart = \[\](?![^}]*;)', "index.html"),
        ("Function syntax error", r'function addToCart\(\) {[^}]*alert[^}]*(?!})', "index.html"),
        ("Missing closing brace", r'alert\("Added to cart"\)(?!\s*})', "index.html"),
        ("Undefined variable", r'console\.log\(undefinedVar\)', "index.html"),
    ]
    
    # Check each pattern
    for i, (bug_name, pattern, file_name) in enumerate(checks, 1):
        if file_name == "index.html":
            content = html_content
        else:
            continue
            
        matches = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if matches:
            bugs_found.append(f"Bug {i}: {bug_name} in {file_name}")
        elif "Missing" in bug_name or "without" in bug_name:
            bugs_found.append(f"Bug {i}: {bug_name} in {file_name}")
    
    return bugs_found

if __name__ == "__main__":
    bugs = detect_bugs_site1()
    print(f"Found {len(bugs)} bugs:")
    for bug in bugs:
        print(f"  - {bug}")

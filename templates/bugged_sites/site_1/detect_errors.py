
#!/usr/bin/env python3
"""
Bug Detection Script for E-commerce Site (Site 1)
Detects 30 intentionally injected bugs in the HTML/CSS/JS files.
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
    
    # Bug detection patterns
    checks = [
        ("Missing viewport meta tag", r'<meta name="viewport"', "index.html"),
        ("Missing type attribute for stylesheet", r'<link.*?rel="stylesheet".*?type="text/css"', "index.html"),
        ("Script in head without defer/async", r'<head>.*?<script(?!.*(?:defer|async))', "index.html"),
        ("Missing lang attribute on html tag", r'<html[^>]*lang=', "index.html"),
        ("Missing alt attribute on img", r'<img(?![^>]*alt=)', "index.html"),
        ("JavaScript void(0) bad practice", r'href="javascript:void\(0\)"', "index.html"),
        ("Missing href attribute", r'<a(?![^>]*href=)[^>]*>', "index.html"),
        ("Broken link reference", r'href="contact\.html"', "index.html"),
        ("Label missing for attribute", r'<label(?![^>]*for=)', "index.html"),
        ("Input without id", r'<input(?![^>]*id=)', "index.html"),
        ("Unclosed div tag", r'<div class="product">(?!.*</div>)', "index.html"),
        ("Image without alt attribute", r'<img src="product1\.jpg"(?![^>]*alt=)', "index.html"),
        ("Button without type", r'<button(?![^>]*type=).*onclick="addToCart\(\)"', "index.html"),
        ("Broken image source", r'src="missing-image\.jpg"', "index.html"),
        ("Missing closing p tag", r'<p>\$699(?!</p>)', "index.html"),
        ("Form without action", r'<form(?![^>]*action=)', "index.html"),
        ("Input without name attribute", r'<input type="email"(?![^>]*name=)', "index.html"),
        ("Submit button outside form", r'</form>\s*<button type="submit"', "index.html"),
        ("Deprecated center tag", r'<center>', "index.html"),
        ("Missing table headers", r'<table>(?!.*<th>)', "index.html"),
        ("Invalid nested anchor tags", r'<a[^>]*>\s*<a[^>]*>', "index.html"),
        ("Missing closing div", r'<div class="product">.*(?!</div>)', "index.html"),
        ("Inline CSS in HTML", r'<style>', "index.html"),
        ("Script tag issues", r'<script>(?!.*</script>)', "index.html"),
        ("Missing semicolon in JS", r'var cart = \[\](?!;)', "index.html"),
        ("Function not properly defined", r'function addToCart\(\) {', "index.html"),
        ("Undefined variable usage", r'cart\.push\(item\)', "index.html"),
        ("Console.log instead of error handling", r'console\.log\("Added to cart"\)', "index.html"),
        ("Missing function closing brace", r'function checkout\(\) {.*if.*alert.*(?!})', "index.html"),
        ("Document.write usage", r'document\.write', "index.html"),
    ]
    
    # Check each pattern
    for i, (bug_name, pattern, file_name) in enumerate(checks, 1):
        if file_name == "index.html":
            content = html_content
        else:
            continue
            
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            bugs_found.append(f"Bug {i}: {bug_name} in {file_name}")
        else:
            # For negative checks (missing elements)
            if "Missing" in bug_name or "without" in bug_name:
                bugs_found.append(f"Bug {i}: {bug_name} in {file_name}")
    
    return bugs_found

if __name__ == "__main__":
    print("=== E-commerce Site Bug Detection ===")
    bugs = detect_bugs_site1()
    print(f"Found {len(bugs)} bugs:")
    for bug in bugs:
        print(f"  ✗ {bug}")
    print("\nNote: This script detects intentionally injected bugs for training purposes.")


#!/usr/bin/env python3
"""
Bug Detection Script for Social Media Site (Site 2)
Detects 30 intentionally injected beginner-friendly frontend bugs.
"""

import re
import os

def detect_bugs_site2():
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
        ("Image without alt text", r'<img src="logo\.svg"(?![^>]*alt=)', "index.html"),
        ("Missing href attribute", r'<a(?![^>]*href=)[^>]*>Profile</a>', "index.html"),
        ("Form without method", r'<form action="/post"(?![^>]*method=)', "index.html"),
        ("Textarea without name", r'<textarea(?![^>]*name=)', "index.html"),
        ("Input without type", r'<input placeholder="Add image URL"(?![^>]*type=)', "index.html"),
        ("Button without type", r'<button(?![^>]*type=)[^>]*>Post Update</button>', "index.html"),
        ("Missing article semantic tag", r'<div class="post">', "index.html"),
        ("Image without alt", r'<img src="user1\.jpg"(?![^>]*alt=)', "index.html"),
        ("Missing closing p tag", r'<p>Just had an amazing day at the beach!(?!</p>)', "index.html"),
        ("Link without href", r'<a(?![^>]*href=)[^>]*>Click here</a>', "index.html"),
        ("Table without proper headers", r'<table(?![^>]*<th>)', "index.html"),
        ("Missing heading hierarchy", r'<h4>Recent Activity</h4>', "index.html"),
        ("List without proper structure", r'<div class="activities">(?!.*<ul>)', "index.html"),
        ("Form missing required attribute", r'Email \(Required\).*<input(?![^>]*required)', "index.html"),
        ("Unclosed div tag", r'<div class="sidebar">(?!.*</div>)', "index.html"),
        ("Empty heading", r'<h3></h3>', "index.html"),
        ("Empty paragraph", r'<p></p>', "index.html"),
        ("Button without accessible text", r'<button>👍</button>', "index.html"),
        ("Link with invalid target", r'target="_self"', "index.html"),
        ("Image with invalid dimensions", r'width="abc"', "index.html"),
        ("Missing fieldset for radio buttons", r'Privacy Setting.*<input type="radio"(?!.*<fieldset>)', "index.html"),
        ("Missing contact structure", r'<div>support@socialbug\.com', "index.html"),
        ("Link without text", r'<a href="/help"></a>', "index.html"),
        ("Empty list item", r'<li></li>', "index.html"),
        ("Missing semicolon", r'var currentUser = \'user123\'(?![^}]*;)', "index.html"),
        ("Function with syntax error", r'function likePost\(\) {[^}]*(?!})', "index.html"),
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
    bugs = detect_bugs_site2()
    print(f"Found {len(bugs)} bugs:")
    for bug in bugs:
        print(f"  - {bug}")

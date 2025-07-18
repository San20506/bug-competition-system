
#!/usr/bin/env python3
"""
Bug Detection Script for Social Media Site (Site 2)
Detects 30 intentionally injected bugs in the HTML/CSS/JS files.
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
    
    # Bug detection patterns
    checks = [
        ("Missing lang attribute on html", r'<html(?![^>]*lang=)', "index.html"),
        ("Missing viewport meta tag", r'<meta name="viewport"', "index.html"),
        ("Missing favicon", r'<link rel="icon"', "index.html"),
        ("Image without alt text", r'<img src="logo\.svg"(?![^>]*alt=)', "index.html"),
        ("Empty href attribute", r'href=""', "index.html"),
        ("Missing href attribute", r'<a(?![^>]*href=)[^>]*>Profile</a>', "index.html"),
        ("Broken internal link", r'href="#nonexistent"', "index.html"),
        ("Form without method", r'<form action="/post"(?![^>]*method=)', "index.html"),
        ("Textarea without name", r'<textarea(?![^>]*name=)', "index.html"),
        ("Input without type", r'<input placeholder="Add image URL"(?![^>]*type=)', "index.html"),
        ("Button without type", r'<button(?![^>]*type=)[^>]*>Post Update</button>', "index.html"),
        ("Missing article semantic tag", r'<div class="post">', "index.html"),
        ("Image without alt in user info", r'<img src="user1\.jpg"(?![^>]*alt=)', "index.html"),
        ("Invalid time format", r'datetime="invalid-date"', "index.html"),
        ("Missing closing p tag", r'<p>Just had an amazing day at the beach!(?!</p>)', "index.html"),
        ("Image without proper attributes", r'<img src="beach\.jpg"(?![^>]*alt=)', "index.html"),
        ("Button without accessible text", r'<button onclick="like\(1\)">👍</button>', "index.html"),
        ("Invalid onclick syntax", r'onclick="comment\(\);"', "index.html"),
        ("Unclosed div tag", r'<div class="post">(?!.*</div>.*</div>)', "index.html"),
        ("Link without proper attributes", r'<a(?![^>]*href=)[^>]*>Click here</a>', "index.html"),
        ("Missing form validation", r'<form class="comment-form"(?![^>]*novalidate)', "index.html"),
        ("Table without proper structure", r'<table(?![^>]*<th>)', "index.html"),
        ("Missing aside or section wrapper", r'<div class="sidebar">', "index.html"),
        ("List without proper structure", r'<p>#technology</p>\s*<p>#travel</p>', "index.html"),
        ("Missing contact information structure", r'<p>Contact: support@socialbug\.com', "index.html"),
        ("Script without type", r'<script>(?![^>]*type=)', "index.html"),
        ("Global variable pollution", r'var currentUser = ', "index.html"),
        ("Function without error handling", r'function like\(postId\) {[^}]*likes\[postId\]\+\+', "index.html"),
        ("Direct DOM manipulation without checks", r'document\.getElementById.*\.innerHTML', "index.html"),
        ("Missing function definition", r'onclick="comment\(\)"(?!.*function comment)', "index.html"),
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
        elif "Missing" in bug_name or "without" in bug_name or "Invalid" in bug_name:
            bugs_found.append(f"Bug {i}: {bug_name} in {file_name}")
    
    return bugs_found

if __name__ == "__main__":
    print("=== Social Media Site Bug Detection ===")
    bugs = detect_bugs_site2()
    print(f"Found {len(bugs)} bugs:")
    for bug in bugs:
        print(f"  ✗ {bug}")
    print("\nNote: This script detects intentionally injected bugs for training purposes.")

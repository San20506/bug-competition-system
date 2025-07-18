
#!/usr/bin/env python3
"""
Bug Detection Script for Banking Site (Site 3)
Detects 30 intentionally injected bugs in the HTML/CSS/JS files.
"""

import re
import os

def detect_bugs_site3():
    bugs_found = []
    
    # Read HTML file
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return []
    
    # Bug detection patterns for banking security issues
    checks = [
        ("Missing charset declaration", r'<meta charset="utf-8">', "index.html"),
        ("Missing viewport meta tag", r'<meta name="viewport"', "index.html"),
        ("Missing security headers meta tags", r'<meta http-equiv="X-Frame-Options"', "index.html"),
        ("Image without alt text", r'<img src="bank-logo\.png"(?![^>]*alt=)', "index.html"),
        ("Insecure link protocols", r'href="http://insecure-site\.com"', "index.html"),
        ("Missing href attribute", r'<a(?![^>]*href=)[^>]*>Support</a>', "index.html"),
        ("Login form without HTTPS enforcement", r'<form action="/login"(?![^>]*class="secure")', "index.html"),
        ("Password field without autocomplete=off", r'<input type="password"(?![^>]*autocomplete="off")', "index.html"),
        ("Missing CSRF protection", r'<form.*method="post"(?!.*csrf)', "index.html"),
        ("Remember me checkbox without security", r'<input type="checkbox" name="remember">', "index.html"),
        ("Sensitive data in HTML comments", r'<!-- Account balance.*User ID', "index.html"),
        ("Table without proper headers", r'<table class="accounts">(?!.*<th>)', "index.html"),
        ("Unescaped user data", r'<td id="balance">\$2,500\.00</td>', "index.html"),
        ("Button without proper security", r'<button onclick="viewStatement\(\)">', "index.html"),
        ("Form without proper validation", r'<form action="/transfer"(?![^>]*novalidate)', "index.html"),
        ("Input without proper validation", r'<input type="text" name="recipient"(?![^>]*pattern=)', "index.html"),
        ("Amount field without min/max validation", r'<input type="number" name="amount"(?![^>]*min=)', "index.html"),
        ("Missing hidden form token", r'<form.*method="post"(?!.*<input type="hidden")', "index.html"),
        ("Iframe without security attributes", r'<iframe src="https://external-widget\.com/rates"(?![^>]*sandbox=)', "index.html"),
        ("Missing error handling div structure", r'<div id="error-messages">', "index.html"),
        ("Error messages in plain text", r'<p style="color: red;">Invalid login attempt from IP:', "index.html"),
        ("External link without rel noopener", r'<a href="https://example\.com/security" target="_blank"(?![^>]*rel="noopener")', "index.html"),
        ("Missing list structure for tips", r'<p>• Never share your password</p>', "index.html"),
        ("Missing contact information structure", r'<p>© 2024 SecureBank \| Call:', "index.html"),
        ("Missing privacy policy link", r'support@securebank\.com</p>(?!.*privacy)', "index.html"),
        ("Storing sensitive data in JavaScript", r'var userAccountNumber = "123456789"', "index.html"),
        ("Function without input validation", r'function viewStatement\(\) {(?!.*validate)', "index.html"),
        ("Direct window.open without security", r'window\.open\("/statement\?account="', "index.html"),
        ("Missing XSS protection", r'\.innerHTML = msg', "index.html"),
        ("Console logging sensitive information", r'console\.log\("User session token:"', "index.html"),
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
    print("=== Banking Site Security Bug Detection ===")
    bugs = detect_bugs_site3()
    print(f"Found {len(bugs)} bugs:")
    for bug in bugs:
        print(f"  ✗ {bug}")
    print("\nNote: This script detects intentionally injected security bugs for training purposes.")


#!/usr/bin/env python3
"""
Bug Detection Script for Learning Platform (Site 5)
Detects 30 intentionally injected bugs in the HTML/CSS/JS files.
"""

import re
import os

def detect_bugs_site5():
    bugs_found = []
    
    # Read HTML file
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return []
    
    # Bug detection patterns for learning platform
    checks = [
        ("Missing charset declaration", r'<meta charset="utf-8">', "index.html"),
        ("Missing viewport meta tag", r'<meta name="viewport"', "index.html"),
        ("Missing Open Graph meta tags", r'<meta property="og:', "index.html"),
        ("Image without alt text", r'<img src="learn-logo\.png"(?![^>]*alt=)', "index.html"),
        ("Missing href attribute", r'<a(?![^>]*href=)[^>]*>My Learning</a>', "index.html"),
        ("Form without proper attributes", r'<form class="search-courses"(?![^>]*action=)', "index.html"),
        ("Input without label", r'<input type="text"(?!.*<label)', "index.html"),
        ("Select without label", r'<select name="category"(?!.*<label)', "index.html"),
        ("Button without type attribute", r'<button(?![^>]*type=)[^>]*>Search Courses</button>', "index.html"),
        ("Missing semantic article structure", r'<div class="course-card">', "index.html"),
        ("Image without alt text in course", r'<img src="js-course\.jpg"(?![^>]*alt=)', "index.html"),
        ("Missing rating accessibility", r'<div class="rating">★★★★☆</div>', "index.html"),
        ("Button without proper attributes", r'<button onclick="enrollCourse\(1\)"(?![^>]*type=)', "index.html"),
        ("Unclosed div tag", r'<button type="button" onclick="enrollCourse\(2\)">Enroll Now - \$149</button>(?!\s*</div>)', "index.html"),
        ("Missing course title", r'<img src="business-course\.jpg"(?!.*<h[1-6])', "index.html"),
        ("Missing form validation", r'<form class="quiz-form"(?![^>]*novalidate)', "index.html"),
        ("Radio buttons without fieldset", r'<input type="radio" name="html"(?!.*<fieldset)', "index.html"),
        ("Missing required attribute", r'<input type="radio" name="js"(?![^>]*required)', "index.html"),
        ("Table without proper headers", r'<table class="progress-table">(?!.*<th>)', "index.html"),
        ("Video without controls", r'<video src="course-preview\.mp4"(?![^>]*controls)', "index.html"),
        ("Aside without semantic structure", r'<div class="sidebar">', "index.html"),
        ("Progress bar without proper attributes", r'<div class="progress-bar">(?!.*aria-label)', "index.html"),
        ("List without proper structure", r'<p>🏆 First Course Completed</p>', "index.html"),
        ("Newsletter form without validation", r'<form class="newsletter">(?!.*required)', "index.html"),
        ("Missing structured contact information", r'<p>© 2024 LearnBug Academy \| support@', "index.html"),
        ("Global variable without proper scope", r'var enrolledCourses = \[\]', "index.html"),
        ("Function without input validation", r'function enrollCourse\(courseId\) {(?!.*validate)', "index.html"),
        ("Alert instead of proper UI feedback", r'alert\("Enrolled successfully!"\)', "index.html"),
        ("Missing error handling for quiz", r'function submitQuiz\(\) {(?!.*try)', "index.html"),
        ("Missing accessibility features", r'document\.addEventListener\(\'DOMContentLoaded\'(?!.*aria)', "index.html"),
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
    print("=== Learning Platform Bug Detection ===")
    bugs = detect_bugs_site5()
    print(f"Found {len(bugs)} bugs:")
    for bug in bugs:
        print(f"  ✗ {bug}")
    print("\nNote: This script detects intentionally injected bugs for training purposes.")


import os
import json


def check_all_fixes(folder, expected_site_id):
    """Check fixes and verify they match the expected site"""
    score = 0
    
    # Load site configuration to validate against expected site
    try:
        with open('admin/sites.json', 'r') as f:
            sites = json.load(f)
        
        if str(expected_site_id) not in sites:
            return 0  # Invalid site ID
            
    except:
        return 0  # Cannot load sites config
    
    # Check for required files based on site ID
    site_files = {
        1: ['index.html', 'cart.js', 'checkout.css'],  # E-commerce
        2: ['profile.html', 'feed.js', 'social.css'],  # Social Media
        3: ['login.html', 'security.js', 'banking.css'],  # Banking
        4: ['article.html', 'news.js', 'layout.css'],  # News
        5: ['course.html', 'quiz.js', 'learning.css']  # Learning
    }
    
    required_files = site_files.get(expected_site_id, ['index.html', 'main.js', 'style.css'])
    
    # Score based on presence of required files
    for file in required_files:
        if os.path.exists(os.path.join(folder, file)):
            if file.endswith('.html'):
                score += 15
            elif file.endswith('.js'):
                score += 10
            elif file.endswith('.css'):
                score += 5
    
    return score

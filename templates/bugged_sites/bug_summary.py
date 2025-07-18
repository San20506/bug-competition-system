
#!/usr/bin/env python3
"""
Master Bug Detection Script
Runs detection for all 5 bugged sites and generates a summary CSV.
"""

import os
import csv
import sys

def run_site_detection(site_id):
    """Run bug detection for a specific site"""
    site_dir = f"site_{site_id}"
    
    if not os.path.exists(site_dir):
        return []
    
    original_dir = os.getcwd()
    os.chdir(site_dir)
    
    try:
        if site_id == 1:
            from detect_errors import detect_bugs_site1 as detect_bugs
        elif site_id == 2:
            from detect_errors import detect_bugs_site2 as detect_bugs
        elif site_id == 3:
            from detect_errors import detect_bugs_site3 as detect_bugs
        elif site_id == 4:
            from detect_errors import detect_bugs_site4 as detect_bugs
        elif site_id == 5:
            from detect_errors import detect_bugs_site5 as detect_bugs
        else:
            return []
        
        bugs = detect_bugs()
        return bugs
    except Exception as e:
        print(f"Error detecting bugs for site {site_id}: {e}")
        return []
    finally:
        os.chdir(original_dir)

def generate_summary():
    """Generate summary of all bugs found across all sites"""
    
    site_info = {
        1: {"name": "E-commerce Site", "type": "Shopping Platform"},
        2: {"name": "Social Media Platform", "type": "Social Network"},
        3: {"name": "Banking Portal", "type": "Financial Services"},
        4: {"name": "News Website", "type": "Media/Publishing"},
        5: {"name": "Online Learning", "type": "Education Platform"}
    }
    
    summary_data = []
    total_bugs = 0
    
    print("=" * 80)
    print("BUG BOUNTY PLATFORM - COMPREHENSIVE BUG DETECTION SUMMARY")
    print("=" * 80)
    
    for site_id in range(1, 6):
        print(f"\n🔍 Scanning Site {site_id}: {site_info[site_id]['name']}")
        print("-" * 50)
        
        bugs = run_site_detection(site_id)
        bug_count = len(bugs)
        total_bugs += bug_count
        
        print(f"Found {bug_count} bugs:")
        for bug in bugs[:5]:  # Show first 5 bugs
            print(f"  ✗ {bug}")
        
        if len(bugs) > 5:
            print(f"  ... and {len(bugs) - 5} more bugs")
        
        # Categorize bugs
        categories = {
            "HTML Structure": 0,
            "Accessibility": 0,
            "Security": 0,
            "JavaScript": 0,
            "Forms": 0,
            "Images": 0,
            "Other": 0
        }
        
        for bug in bugs:
            bug_text = bug.lower()
            if any(word in bug_text for word in ['missing', 'unclosed', 'semantic', 'structure']):
                categories["HTML Structure"] += 1
            elif any(word in bug_text for word in ['alt', 'aria', 'accessibility', 'label']):
                categories["Accessibility"] += 1
            elif any(word in bug_text for word in ['security', 'csrf', 'xss', 'password', 'token']):
                categories["Security"] += 1
            elif any(word in bug_text for word in ['javascript', 'function', 'variable', 'error handling']):
                categories["JavaScript"] += 1
            elif any(word in bug_text for word in ['form', 'input', 'button', 'validation']):
                categories["Forms"] += 1
            elif any(word in bug_text for word in ['image', 'img', 'alt']):
                categories["Images"] += 1
            else:
                categories["Other"] += 1
        
        # Create bug list string
        bug_list = "; ".join([bug.split(": ", 1)[1] if ": " in bug else bug for bug in bugs])
        
        summary_data.append([
            site_info[site_id]['name'],
            site_info[site_id]['type'],
            bug_count,
            categories["HTML Structure"],
            categories["Accessibility"],
            categories["Security"],
            categories["JavaScript"],
            categories["Forms"],
            categories["Images"],
            categories["Other"],
            bug_list[:500] + "..." if len(bug_list) > 500 else bug_list
        ])
    
    print(f"\n📊 OVERALL SUMMARY")
    print("=" * 50)
    print(f"Total Sites: 5")
    print(f"Total Bugs: {total_bugs}")
    print(f"Average Bugs per Site: {total_bugs / 5:.1f}")
    
    # Generate CSV report
    csv_filename = "bug_detection_summary.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Header row
        writer.writerow([
            "Site Name",
            "Site Type",
            "Total Bugs",
            "HTML Structure",
            "Accessibility",
            "Security",
            "JavaScript",
            "Forms",
            "Images",
            "Other",
            "Bug Details"
        ])
        
        # Data rows
        for row in summary_data:
            writer.writerow(row)
    
    print(f"\n📄 Summary saved to: {csv_filename}")
    
    print(f"\n🎯 BUG BOUNTY CHALLENGE READY!")
    print("Each team will be assigned one of these 5 sites to debug.")
    print("Teams must identify and fix the bugs in their assigned site.")
    print("The detection scripts can be used to verify fixes.")

if __name__ == "__main__":
    generate_summary()

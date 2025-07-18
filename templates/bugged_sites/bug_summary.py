
#!/usr/bin/env python3
"""
Master Bug Detection and Drive Link Management Script
Generates comprehensive reports for all 5 bug bounty sites with Google Drive integration.
"""

import os
import csv
import sys
import json
import qrcode
from datetime import datetime

def generate_qr_code(url, site_id):
    """Generate QR code for Google Drive link"""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure qr directory exists
    os.makedirs('../../../static/qr', exist_ok=True)
    img.save(f'../../../static/qr/site_{site_id}.png')
    print(f"✅ QR code generated for Site {site_id}")

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

def generate_drive_qr_codes():
    """Generate QR codes for all Google Drive links"""
    try:
        with open('../../../admin/sites.json', 'r') as f:
            sites = json.load(f)
        
        for site_id, site_info in sites.items():
            drive_link = site_info.get('drive_link', '')
            if drive_link:
                generate_qr_code(drive_link, site_id)
                
    except Exception as e:
        print(f"Error generating QR codes: {e}")

def export_bugs_to_csv():
    """Export all bugs to CSV for admin download"""
    
    site_info = {
        1: {"name": "E-commerce Store", "type": "Shopping Platform"},
        2: {"name": "Social Media Platform", "type": "Social Network"},
        3: {"name": "Banking Portal", "type": "Financial Services"},
        4: {"name": "News Website", "type": "Media/Publishing"},
        5: {"name": "Online Learning Platform", "type": "Education"}
    }
    
    # Create comprehensive CSV report
    csv_filename = "../../../static/bug_reports_complete.csv"
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Header row
        writer.writerow([
            "Site ID",
            "Site Name", 
            "Site Type",
            "Bug Number",
            "Bug Description",
            "File Location",
            "Bug Category",
            "Severity"
        ])
        
        total_bugs = 0
        
        for site_id in range(1, 6):
            bugs = run_site_detection(site_id)
            total_bugs += len(bugs)
            
            for i, bug in enumerate(bugs, 1):
                # Parse bug description
                bug_parts = bug.split(": ", 1)
                bug_desc = bug_parts[1] if len(bug_parts) > 1 else bug
                
                # Categorize bug
                category = "Other"
                severity = "Medium"
                
                if any(word in bug_desc.lower() for word in ['missing alt', 'accessibility', 'aria']):
                    category = "Accessibility"
                    severity = "High"
                elif any(word in bug_desc.lower() for word in ['security', 'csrf', 'xss', 'password']):
                    category = "Security"
                    severity = "Critical"
                elif any(word in bug_desc.lower() for word in ['javascript', 'function', 'variable']):
                    category = "JavaScript"
                    severity = "Medium"
                elif any(word in bug_desc.lower() for word in ['form', 'input', 'validation']):
                    category = "Forms"
                    severity = "High"
                elif any(word in bug_desc.lower() for word in ['html', 'tag', 'structure']):
                    category = "HTML Structure"
                    severity = "Medium"
                
                writer.writerow([
                    site_id,
                    site_info[site_id]['name'],
                    site_info[site_id]['type'],
                    i,
                    bug_desc,
                    "index.html",  # Most bugs are in main HTML file
                    category,
                    severity
                ])
        
        print(f"📊 Bug report exported to: {csv_filename}")
        print(f"Total bugs across all sites: {total_bugs}")

def generate_summary():
    """Generate comprehensive summary with drive integration"""
    
    site_info = {
        1: {"name": "E-commerce Store", "type": "Shopping Platform"},
        2: {"name": "Social Media Platform", "type": "Social Network"},
        3: {"name": "Banking Portal", "type": "Financial Services"},
        4: {"name": "News Website", "type": "Media/Publishing"},
        5: {"name": "Online Learning Platform", "type": "Education"}
    }
    
    print("=" * 80)
    print("🎯 BUG BOUNTY TRAINING PLATFORM - COMPREHENSIVE SETUP")
    print("=" * 80)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Generate QR codes for Drive links
    print("\n🔗 Generating QR codes for Google Drive links...")
    generate_drive_qr_codes()
    
    total_bugs = 0
    
    for site_id in range(1, 6):
        print(f"\n🔍 Site {site_id}: {site_info[site_id]['name']}")
        print("-" * 50)
        
        bugs = run_site_detection(site_id)
        bug_count = len(bugs)
        total_bugs += bug_count
        
        print(f"📋 Bugs Found: {bug_count}/30")
        print(f"🎯 Type: {site_info[site_id]['type']}")
        
        # Show sample bugs
        if bugs:
            print("Sample bugs:")
            for bug in bugs[:3]:
                print(f"  ❌ {bug}")
            if len(bugs) > 3:
                print(f"  ... and {len(bugs) - 3} more")
    
    # Export comprehensive CSV
    print(f"\n📊 Exporting comprehensive bug reports...")
    export_bugs_to_csv()
    
    print(f"\n🎉 SETUP COMPLETE!")
    print(f"✅ 5 Templates with {total_bugs} total bugs")
    print(f"✅ Google Drive integration ready")
    print(f"✅ QR codes generated")
    print(f"✅ Admin reports exported")
    
    print(f"\n📋 Next Steps:")
    print(f"1. Teams scan QR codes to access their assigned Google Drive folder")
    print(f"2. Teams download buggy templates and fix issues")
    print(f"3. Teams upload fixed versions back to their folder")
    print(f"4. Admin can track progress and verify fixes")

if __name__ == "__main__":
    generate_summary()

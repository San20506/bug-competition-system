
from flask import Flask, render_template, request, redirect, session, send_from_directory, jsonify
import os, zipfile, shutil, json, sqlite3, csv, io, qrcode
from datetime import datetime
from bug_rules import check_all_fixes

app = Flask(__name__)
app.secret_key = 'super-secret-key'
ADMIN_PASS = 'admin'

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)
if not os.path.exists('static/qr'):
    os.makedirs('static/qr')


def generate_qr_code(url, site_id):
    """Generate QR code for the given URL and save it for specific site"""
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        qr_path = f'static/qr/site_{site_id}.png'
        img.save(qr_path)
        return qr_path
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None


def get_sites():
    """Get all sites from configuration"""
    try:
        with open('admin/sites.json', 'r') as f:
            return json.load(f)
    except:
        return {}


def get_team_site(team_name):
    """Get the site ID assigned to a team"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT site_id FROM teams WHERE name = ?", (team_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 1


def format_time(seconds):
    """Convert seconds to mm:ss format"""
    if seconds <= 0:
        return "00:00"
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def export_bug_reports():
    """Export comprehensive bug reports to CSV"""
    try:
        # Run the bug summary script to generate reports
        import subprocess
        result = subprocess.run(['python', 'templates/bugged_sites/bug_summary.py'], 
                              capture_output=True, text=True, cwd='.')
        return "✅ Bug reports exported successfully!"
    except Exception as e:
        return f"❌ Error exporting reports: {str(e)}"


# ---- STATIC FILES ----
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


# ---- LOGIN ROUTE ----
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        name = request.form['username'].strip()
        pw = request.form.get('password', '')

        if name.lower() == 'admin' and pw == ADMIN_PASS:
            session['admin'] = True
            return redirect('/admin/dashboard')

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT password FROM teams WHERE name = ?", (name,))
        result = c.fetchone()
        conn.close()

        if result and result[0] == pw:
            session['team'] = name
            return redirect('/')
        else:
            error = "❌ Invalid team name or password"

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# ---- BUG SITE QR CODE (TEAM-SPECIFIC VIEW) ----
@app.route('/bug')
def bug_site():
    if 'team' not in session:
        return redirect('/login')

    team_name = session['team']
    site_id = get_team_site(team_name)
    sites = get_sites()

    site_info = sites.get(str(site_id), {})
    site_name = site_info.get('name', f'Site {site_id}')
    drive_link = site_info.get('drive_link', '#')

    qr_path = f'static/qr/site_{site_id}.png'

    return render_template('bug_site.html', 
                         site_name=site_name, 
                         bug_url=drive_link,
                         qr_path=qr_path,
                         site_id=site_id,
                         site_info=site_info)


# ---- DOWNLOAD SITE FILES ----
@app.route('/download_site/<int:site_id>')
def download_site(site_id):
    """Download site files as ZIP for editing"""
    if 'team' not in session:
        return redirect('/login')

    team_name = session['team']
    team_site_id = get_team_site(team_name)

    # Teams can only download their assigned site
    if site_id != team_site_id:
        return "Access denied: You can only download your assigned site", 403

    site_path = f'templates/bugged_sites/site_{site_id}'
    if not os.path.exists(site_path):
        return "Site not found", 404

    # Create ZIP file
    zip_filename = f'site_{site_id}_buggy_files.zip'
    zip_path = os.path.join('uploads', zip_filename)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(site_path):
            for file in files:
                if not file.endswith('.py'):  # Exclude detection scripts
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, site_path)
                    zipf.write(file_path, arc_name)

    return send_from_directory('uploads', zip_filename, as_attachment=True)


# ---- TEAM SUBMISSION PAGE ----
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'team' not in session:
        return redirect('/login')

    timer_active = False
    remaining = 0

    if os.path.exists('admin/status.json'):
        with open('admin/status.json') as f:
            status = json.load(f)
            if status['status'] == 'running' and status['start_time']:
                elapsed = (datetime.now() - datetime.fromisoformat(status['start_time'])).total_seconds()
                remaining = int(status['duration']) * 60 - int(elapsed)
                timer_active = remaining > 0
            else:
                timer_active = False

    if request.method == 'POST':
        if not timer_active:
            return render_template("index.html", error="Event is closed", timer_active=False, remaining=0)

        if 'zipfile' not in request.files or request.files['zipfile'].filename == '':
            return render_template("index.html", error="No file provided", timer_active=True, remaining=remaining)

        file = request.files['zipfile']
        teamname = session['team']
        team_site_id = get_team_site(teamname)

        if os.path.exists(UPLOAD_FOLDER):
            shutil.rmtree(UPLOAD_FOLDER)
        os.makedirs(UPLOAD_FOLDER)

        zip_path = 'temp.zip'
        file.save(zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(UPLOAD_FOLDER)
        os.remove(zip_path)

        # Pass site ID to scoring function for validation
        score = check_all_fixes(UPLOAD_FOLDER, team_site_id)
        time_taken = int(status['duration']) * 60 - remaining

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT id FROM scores WHERE name=?", (teamname,))
        existing = c.fetchone()
        if existing:
            c.execute("UPDATE scores SET score=?, duration=?, site_id=? WHERE name=?", (score, time_taken, team_site_id, teamname))
        else:
            c.execute("INSERT INTO scores (name, score, duration, site_id) VALUES (?, ?, ?, ?)", (teamname, score, time_taken, team_site_id))
        conn.commit()
        conn.close()

        return render_template("result.html", name=teamname, score=score, time_taken=format_time(time_taken))

    return render_template("index.html", timer_active=timer_active, remaining=remaining)


# ---- PUBLIC LEADERBOARD ----
@app.route('/leaderboard')
def leaderboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT s.name, s.score, s.duration, s.site_id FROM scores s ORDER BY s.score DESC, s.duration ASC")
    rows = c.fetchall()
    conn.close()

    sites = get_sites()

    # Format time for display and add site names
    formatted_rows = []
    for row in rows:
        site_name = sites.get(str(row[3]), {}).get('name', f'Site {row[3]}')
        formatted_rows.append((row[0], row[1], format_time(row[2]), site_name))

    return render_template("leaderboard.html", rows=formatted_rows)


# ---- ADMIN SITES MANAGEMENT ----
@app.route('/admin/sites', methods=['GET', 'POST'])
def admin_sites():
    if 'admin' not in session:
        return redirect('/login')

    msg = ""
    sites = get_sites()
    team_assignments = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'update_site':
            site_id = request.form.get('site_id')
            site_name = request.form.get('site_name', '').strip()
            site_type = request.form.get('site_type', '').strip()
            drive_link = request.form.get('drive_link', '').strip()
            description = request.form.get('description', '').strip()

            if site_id and site_name and drive_link:
                sites[site_id] = {
                    'name': site_name,
                    'type': site_type,
                    'drive_link': drive_link,
                    'description': description,
                    'bugs_count': sites.get(site_id, {}).get('bugs_count', 30),
                    'qr_path': f'static/qr/site_{site_id}.png'
                }

                with open('admin/sites.json', 'w') as f:
                    json.dump(sites, f, indent=2)

                # Regenerate QR code
                qr_path = generate_qr_code(drive_link, site_id)
                if qr_path:
                    sites[site_id]['qr_path'] = qr_path
                    with open('admin/sites.json', 'w') as f:
                        json.dump(sites, f, indent=2)

                msg = f"✅ Site {site_id} updated and QR code regenerated!"

        elif action == 'regenerate_qr':
            site_id = request.form.get('site_id')
            if site_id and site_id in sites:
                drive_link = sites[site_id].get('drive_link', '')
                if drive_link:
                    qr_path = generate_qr_code(drive_link, site_id)
                    if qr_path:
                        sites[site_id]['qr_path'] = qr_path
                        with open('admin/sites.json', 'w') as f:
                            json.dump(sites, f, indent=2)
                        msg = f"🔄 QR code regenerated for Site {site_id}!"

        elif action == 'regenerate_all_qr':
            regenerated = 0
            for site_id, site_info in sites.items():
                drive_link = site_info.get('drive_link', '')
                if drive_link:
                    qr_path = generate_qr_code(drive_link, site_id)
                    if qr_path:
                        sites[site_id]['qr_path'] = qr_path
                        regenerated += 1
            
            with open('admin/sites.json', 'w') as f:
                json.dump(sites, f, indent=2)
            msg = f"🔄 {regenerated} QR codes regenerated!"

        elif action == 'export_bug_reports':
            result = export_bug_reports()
            msg = result

        elif action == 'view_assignments':
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("SELECT name, site_id FROM teams ORDER BY site_id, name")
            assignments = c.fetchall()
            conn.close()
            
            team_assignments = []
            for team_name, site_id in assignments:
                site_name = sites.get(str(site_id), {}).get('name', f'Site {site_id}')
                team_assignments.append({
                    'team_name': team_name,
                    'site_id': site_id,
                    'site_name': site_name
                })

    return render_template('admin_sites.html', msg=msg, sites=sites, team_assignments=team_assignments)


# ---- ADMIN DASHBOARD ----
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if 'admin' not in session:
        return redirect('/login')

    msg = ""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == "start_timer":
            mins = int(request.form.get('duration', 0))
            status = {
                "status": "running",
                "start_time": datetime.now().isoformat(),
                "duration": mins
            }
            with open('admin/status.json', 'w') as f:
                json.dump(status, f)
            msg = f"▶ Timer started for {mins} minutes."

        elif action == "stop_timer":
            with open('admin/status.json') as f:
                status = json.load(f)
            status["status"] = "stopped"
            with open('admin/status.json', 'w') as f:
                json.dump(status, f)
            msg = "⏹ Timer stopped."

        elif action == "reset_timer":
            status = {
                "status": "stopped",
                "start_time": None,
                "duration": 0
            }
            with open('admin/status.json', 'w') as f:
                json.dump(status, f)
            msg = "🔄 Timer reset."

        elif action == "reset_scores":
            c.execute("DELETE FROM scores")
            conn.commit()
            msg = "🗑 Scores cleared."

        elif action == "update_scores":
            for key in request.form:
                if key.startswith("score_"):
                    uid = key.split("_")[1]
                    score = request.form[key]
                    dur = request.form.get(f'duration_{uid}')
                    c.execute("UPDATE scores SET score=?, duration=? WHERE id=?", (score, dur, uid))
            conn.commit()
            msg = "✅ Scores updated."

        elif action == "add_team":
            name = request.form.get("teamname", "").strip()
            password = request.form.get("teampassword", "").strip()
            site_id = int(request.form.get("site_id", 1))
            try:
                c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", (name, password, site_id))
                conn.commit()
                msg = f"✅ Team '{name}' added with Site {site_id}."
            except:
                msg = f"⚠️ Team '{name}' already exists."

        elif action == "delete_team":
            name = request.form.get("teamname", "").strip()
            c.execute("DELETE FROM teams WHERE name = ?", (name,))
            c.execute("DELETE FROM scores WHERE name = ?", (name,))
            conn.commit()
            msg = f"🗑 Team '{name}' deleted."

        elif action == "change_password":
            name = request.form.get("teamname", "").strip()
            new_password = request.form.get("newpassword", "").strip()
            c.execute("UPDATE teams SET password = ? WHERE name = ?", (new_password, name))
            conn.commit()
            msg = f"🔑 Password changed for team '{name}'."

        elif action == "change_site":
            name = request.form.get("teamname", "").strip()
            new_site_id = int(request.form.get("site_id", 1))
            c.execute("UPDATE teams SET site_id = ? WHERE name = ?", (new_site_id, name))
            conn.commit()
            msg = f"🎯 Site assignment changed for team '{name}' to Site {new_site_id}."

        elif action == "bulk_teams":
            file = request.files.get("file")
            if file:
                added = 0
                content = file.read().decode('utf-8')
                csv_reader = csv.reader(io.StringIO(content))
                for row in csv_reader:
                    if len(row) >= 2:
                        name, password = row[0].strip(), row[1].strip()
                        site_id = int(row[2]) if len(row) > 2 and row[2].strip().isdigit() else 1
                        try:
                            c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", (name, password, site_id))
                            added += 1
                        except:
                            continue
                conn.commit()
                msg = f"📥 {added} team(s) imported from CSV."

        elif action == "reset_db":
            conn.close()
            import subprocess
            subprocess.run(['python', 'reset_db.py'])
            msg = "💥 Database reset. All teams and scores removed."
            return redirect('/admin/dashboard')

    with open('admin/status.json') as f:
        timer = json.load(f)
    c.execute("SELECT id, name, score, duration FROM scores ORDER BY score DESC")
    scores = c.fetchall()
    c.execute("SELECT name, password, site_id FROM teams ORDER BY name")
    teams = c.fetchall()
    conn.close()

    sites = get_sites()

    return render_template("dashboard.html", msg=msg, timer=timer, scores=scores, teams=teams, sites=sites)


# ---- RUN SERVER ----
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)

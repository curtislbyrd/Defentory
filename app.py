# app.py — Final version with Heatmap + Export JSON + everything
from flask import Flask, render_template, request, redirect, url_for, Response
import sqlite3
from datetime import datetime
import csv
from io import StringIO
import json

app = Flask(__name__)

def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS detections (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        environment TEXT NOT NULL,
                        log_source TEXT NOT NULL,
                        siem_type TEXT NOT NULL,
                        attack_tactics TEXT DEFAULT '',
                        defend_tactics TEXT DEFAULT '',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
        for col, definition in [("attack_tactics", "TEXT DEFAULT ''"), ("defend_tactics", "TEXT DEFAULT ''")]:
            try:
                c.execute(f"ALTER TABLE detections ADD COLUMN {col} {definition}")
            except sqlite3.OperationalError:
                pass
        conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/intake', methods=['GET', 'POST'])
def intake():
    if request.method == 'POST':
        name = request.form['name']
        environment = request.form['environment']
        log_source = request.form['log_source']
        siem_type = request.form['siem_type']
        attack_tactics = ','.join(request.form.getlist('attack_tactics'))
        defend_tactics = ','.join(request.form.getlist('defend_tactics'))

        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute("""INSERT INTO detections 
                         (name, environment, log_source, siem_type, attack_tactics, defend_tactics) 
                         VALUES (?, ?, ?, ?, ?, ?)""",
                      (name, environment, log_source, siem_type, attack_tactics, defend_tactics))
            conn.commit()
        return redirect(url_for('defendreport'))
    return render_template('intake.html')

@app.route('/report')
def report():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM detections ORDER BY created_at DESC")
        detections = c.fetchall()
    return render_template('report.html', detections=detections)

@app.route('/defendreport')
def defendreport():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM detections ORDER BY created_at DESC")
        detections = c.fetchall()
    return render_template('defendreport.html', detections=detections)

# NEW: D3FEND HEATMAP PAGE
@app.route('/heatmap')
def heatmap():
    counts = {'Harden': 0, 'Detect': 0, 'Isolate': 0, 'Deceive': 0, 'Restore': 0}
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT defend_tactics FROM detections")
        rows = c.fetchall()
        for row in rows:
            if row['defend_tactics']:
                for t in row['defend_tactics'].split(','):
                    clean = t.strip()
                    if clean in counts:
                        counts[clean] += 1
    return render_template('heatmap.html', counts=counts)

@app.route('/export-csv')
def export_csv():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT name, environment, log_source, siem_type, attack_tactics, defend_tactics, created_at FROM detections ORDER BY created_at DESC")
        rows = c.fetchall()

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Detection Name', 'Environment', 'Log Source', 'SIEM', 'ATT&CK Tactics', 'D3FEND Tactics', 'Added On'])
    for row in rows:
        writer.writerow([row['name'], row['environment'], row['log_source'], row['siem_type'],
                         row['attack_tactics'] or '—', row['defend_tactics'] or '—', row['created_at'][:19].replace(' ', 'T')])
    today = datetime.now().strftime('%Y-%m-%d')
    return Response(output.getvalue(), mimetype='text/csv',
                    headers={'Content-Disposition': f'attachment;filename=defentory-detections-{today}.csv'})

@app.route('/export-json')
def export_json():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM detections ORDER BY created_at DESC")
        rows = c.fetchall()
    data = [dict(row) for row in rows]
    json_data = json.dumps(data, indent=2, default=str)
    today = datetime.now().strftime('%Y-%m-%d')
    return Response(json_data, mimetype='application/json',
                    headers={'Content-Disposition': f'attachment;filename=defentory-detections-{today}.json'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
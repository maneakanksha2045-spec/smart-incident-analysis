from flask import Flask, jsonify, request, render_template
from datetime import datetime
import json
import os
import sqlite3
print("Application Starting...")

app = Flask(__name__)

def create_table():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    incident_id TEXT PRIMARY KEY,
    timestamp TEXT,
    service TEXT,
    severity TEXT,
    root_cause TEXT,
    recommendation TEXT
)
""")

    conn.commit()
    conn.close()

# Dummy Metrics
def fetch_metrics():
    return {
        "cpu": 92,
        "memory": 85,
        "disk": 70,
        "db_latency": 300
    }

# Dummy Logs
def fetch_logs():
    return [
        "ERROR: Database connection timeout",
        "WARN: CPU usage high",
        "ERROR: Application thread blocked"
    ]
# Save Incident History
def save_incident(incident):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO incidents VALUES (?, ?, ?, ?, ?, ?)
    """, (
        incident["incident_id"],
        incident["timestamp"],
        incident["service"],
        incident["severity"],
        incident["root_cause"],
        incident["recommendation"]
    ))

    conn.commit()
    conn.close()

# Call function here
create_table()

# Root Cause Analysis Logic
def analyze_root_cause(metrics,logs):

    if metrics["cpu"] > 90:
        return {
            "root_cause": "High CPU Utilization",
            "recommendation": "Scale service or optimize application code"
        }

    if metrics["memory"] > 80:
        return {
            "root_cause": "Memory Leak",
            "recommendation": "Restart service and investigate memory usage"
        }

    if metrics["disk"] > 90:
        return {
            "root_cause": "Disk Full",
            "recommendation": "Clean logs or increase storage"
        }

    if metrics["db_latency"] > 250:
        return {
            "root_cause": "Database Performance Issue",
            "recommendation": "Optimize database queries"
        }
    if any("ERROR" in log for log in logs):
        return {
            "root_cause": "Application Error",
            "recommendation": "Check application logs and restart service"
        }
    return {
        "root_cause": "Unknown Issue",
        "recommendation": "Manual investigation required"
    }

# Home Page
@app.route("/")
def home():
    return "Smart Incident Analyzer Running"

# Metrics API
@app.route("/metrics")
def metrics():
    return jsonify(fetch_metrics())

# Incident Analysis API
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    metrics = fetch_metrics()
    logs = fetch_logs()

    result = analyze_root_cause(metrics, logs)

    incident_record = {
        "incident_id": data.get("incident_id"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "service": data.get("service"),
        "severity": data.get("severity"),
        "root_cause": result["root_cause"],
        "recommendation": result["recommendation"]
    }

    save_incident(incident_record)

    return jsonify(incident_record)

@app.route("/incidents")
def get_incidents():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM incidents")

    rows = cursor.fetchall()

    conn.close()

    incidents = []

    for row in rows:
        incidents.append({
            "incident_id": row[0],
            "timestamp": row[1],
            "service": row[2],
            "severity": row[3],
            "root_cause": row[4],
            "recommendation": row[5]
        })

    return jsonify(incidents)

@app.route("/incident/<incident_id>")
def get_incident_by_id(incident_id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM incidents WHERE incident_id=?",
        (incident_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return jsonify({
            "incident_id": row[0],
            "timestamp": row[1],
            "service": row[2],
            "severity": row[3],
            "root_cause": row[4],
            "recommendation": row[5]
        })

    return jsonify({"message": "Incident not found"})

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()

    conn.close()

    incidents = []

    for row in rows:
        incidents.append({
            "incident_id": row[0],
            "timestamp": row[1],
            "service": row[2],
            "severity": row[3],
            "root_cause": row[4],
            "recommendation": row[5]
        })

    return render_template(
        "dashboard.html",
        incidents=incidents,
        total_incidents=len(incidents)
    )

# Main Program
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
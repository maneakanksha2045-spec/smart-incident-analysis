from flask import Flask, jsonify, request
from datetime import datetime
import json
import os
print("Application Starting...")

app = Flask(__name__)

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

    with open("incidents.json", "r") as file:
        incidents = json.load(file)

    incidents.append(incident)

    with open("incidents.json", "w") as file:
        json.dump(incidents, file, indent=4)
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

    with open("incidents.json", "r") as file:
        incidents = json.load(file)

    return jsonify(incidents)

@app.route("/incident/<incident_id>")
def get_incident_by_id(incident_id):

    with open("incidents.json", "r") as file:
        incidents = json.load(file)

    for incident in incidents:
        if incident["incident_id"] == incident_id:
            return jsonify(incident)

    return jsonify({"message": "Incident not found"})

@app.route("/dashboard")
def dashboard():

    with open("incidents.json", "r") as file:
        incidents = json.load(file)

    total_incidents = len(incidents)

    html = f"""
    <html>
    <head>
        <title>Incident Dashboard</title>
    </head>
    <body>
        <h1>Smart Incident Dashboard</h1>

        <h2>Total Incidents: {total_incidents}</h2>

        <h3>Incident History</h3>

        <ul>
    """

    for incident in incidents:
        html += f"""
        <li>
        {incident['incident_id']} -
        {incident['service']} -
        {incident['severity']}
        </li>
        """

    html += """
        </ul>
    </body>
    </html>
    """

    return html

# Main Program
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, jsonify, request, render_template
import jwt
from datetime import datetime, timedelta
from functools import wraps
import json
from db_config import db
import os
import mysql.connector
print("Application Starting...")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'smartincidentsecret'
cursor = db.cursor()
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="incidentuser",
        password="Incident123",
        database="incident_db"
    )

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
          token = request.cookies.get("token")

        try:
            data = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithms=["HS256"]
            )

            print("Decoded Token:", data)

        except Exception as e:
            print("JWT Error:", e)
            return jsonify({"message": str(e)}), 401

        return f(*args, **kwargs)

    return decorated

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

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO incidents
    (incident_id,timestamp,service,severity,root_cause,recommendation)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        incident["incident_id"],
        incident["timestamp"],
        incident["service"],
        incident["severity"],
        incident["root_cause"],
        incident["recommendation"]
    )

    cursor.execute(query, values)

    conn.commit()
    conn.close()

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
@token_required
def get_incidents():

    conn = get_connection()
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
@token_required
def get_incident_by_id(incident_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM incidents WHERE incident_id=%s",
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

    conn = get_connection()
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

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        token = jwt.encode(
            {
                "username": username,
                "role": user[3],
                "exp": datetime.utcnow() + timedelta(hours=1)
            },
            app.config['SECRET_KEY'],
            algorithm="HS256"
        )

        return jsonify({
            "message": "Login Successful",
            "token": token
        })

    return jsonify({
        "message": "Invalid Credentials"
    }), 401

@app.route("/login-page")
def login_page():
    return render_template("login.html")

# Main Program
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="incidentuser",
    password="Incident123",
    database="incident_db"
)

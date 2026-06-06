import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akanksha123",
    database="incident_db"
)

cursor = db.cursor()
# Smart Incident Analyzer

A Flask-based Incident Management System that performs Root Cause Analysis, stores incidents in MySQL, provides a dashboard for monitoring, and secures APIs using JWT Authentication.

## Features

- Incident Creation and Tracking
- Root Cause Analysis Engine
- MySQL Database Integration
- JWT Authentication
- User Login System
- Incident Dashboard
- REST APIs
- Incident Search and Monitoring

## Tech Stack

- Python
- Flask
- MySQL
- JWT (PyJWT)
- HTML
- CSS
- Bootstrap
- JavaScript

## Project Structure

smart-incident-analysis/

├── app.py

├── db_config.py

├── requirements.txt

├── templates/

│ ├── login.html

│ └── dashboard.html

└── README.md

## Database Setup

### Create Database

```sql
CREATE DATABASE incident_db;
USE incident_db;
```

### Create Incidents Table

```sql
CREATE TABLE incidents (
    incident_id VARCHAR(50) PRIMARY KEY,
    timestamp DATETIME,
    service VARCHAR(100),
    severity VARCHAR(50),
    root_cause TEXT,
    recommendation TEXT
);
```

### Create Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);
```

### Insert Admin User

```sql
INSERT INTO users(username,password,role)
VALUES(
'admin',
'admin123',
'Admin'
);
```

## Installation

### Clone Repository

```bash
git clone <your-github-repository-url>
cd smart-incident-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

## Application URLs

### Login Page

http://127.0.0.1:8080/login-page

### Dashboard

http://127.0.0.1:8080/dashboard

### Metrics API

http://127.0.0.1:8080/metrics

## Default Credentials

Username: admin

Password: admin123

## JWT Authentication

Users must authenticate through the login API.

After successful login, a JWT token is generated and used to access protected APIs.

## Future Enhancements

- AI-Based Root Cause Analysis
- Email Notifications
- Cloud Deployment (AWS/Render)
- Role-Based Access Control
- Real-Time Monitoring Dashboard

## Author

Akanksha Mane

BCA Student
# Smart Incident Analysis Tool

## Overview

Smart Incident Analysis Tool is a Flask-based web application that analyzes incidents, identifies root causes, stores incident history, and provides a dashboard for monitoring incidents.

## Features

- Incident Analysis
- Root Cause Detection
- Severity Classification
- Incident History Tracking
- SQLite Database Integration
- REST API Endpoints
- Dashboard for Incident Monitoring
- Cloud Deployment on Render

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git
- GitHub
- Render

## Project Structure

```text
smart-incident-analysis/
│
├── app.py
├── database.db
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── dashboard.html
```

## Installation

### Clone Repository

```bash
git clone https://github.com/maneakanksha2045-spec/smart-incident-analysis.git
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

### Open Browser

```text
http://127.0.0.1:8080
```

## Live Demo

https://smart-incident-analysis.onrender.com

## API Endpoints

| Endpoint | Description |
|-----------|-------------|
| / | Home Page |
| /metrics | System Metrics |
| /analyze | Analyze Incident |
| /incidents | View All Incidents |
| /incident/<incident_id> | View Incident by ID |
| /dashboard | Incident Dashboard |

## Sample Incident

```json
{
  "incident_id": "INC2001",
  "service": "Payment-Service",
  "severity": "Critical"
}
```

## Future Enhancements

- User Authentication
- Email Notifications
- AI-Based Incident Prediction
- Charts and Analytics Dashboard
- Role-Based Access Control

## Live Project

https://smart-incident-analysis.onrender.com

## GitHub Repository

https://github.com/maneakanksha2045-spec/smart-incident-analysis

## Author

**Akanksha Mane**
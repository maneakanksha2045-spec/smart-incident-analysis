# Smart Incident Analysis Tool

## Overview
A Python Flask-based Incident Analysis System that detects root causes from metrics and logs, generates recommendations, and stores incident history.

## Features
- Incident Analysis API
- Root Cause Detection
- Log Analysis
- Incident History Storage
- Search Incident by ID
- Dashboard View
- Timestamp Tracking

## Technologies Used
- Python
- Flask
- JSON
- REST APIs

## API Endpoints

### Home
GET /

### Metrics
GET /metrics

### Analyze Incident
POST /analyze

### Get All Incidents
GET /incidents

### Search Incident
GET /incident/<incident_id>

### Dashboard
GET /dashboard

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```
# Smart Incident Analyzer

A cloud-based incident analysis application built using Flask, MariaDB, and AWS EC2. The system analyzes incidents, identifies possible root causes, and stores incident history for monitoring and troubleshooting.

## Live Demo

The application is deployed on AWS EC2.

Dashboard:
http://3.109.115.108:8080/dashboard

Home:
http://3.109.115.108:8080

## Features

- Incident Analysis API
- Root Cause Detection
- Incident History Storage
- JWT Authentication
- Dashboard for Incident Monitoring
- MariaDB Database Integration
- AWS EC2 Deployment

## Tech Stack

- Python
- Flask
- MariaDB
- AWS EC2
- GitHub
- HTML
- CSS
- JavaScript

## Project Structure

```text
smart-incident-analysis/
│
├── app.py
├── db_config.py
├── requirements.txt
├── templates/
│   ├── dashboard.html
│   └── login.html
├── incident_db_users.sql
├── incident_db_incidents.sql
└── README.md
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

### Configure Database

Create a MariaDB database:

```sql
CREATE DATABASE incident_db;
```

Import SQL files:

```bash
mysql -u username -p incident_db < incident_db_users.sql
mysql -u username -p incident_db < incident_db_incidents.sql
```

### Run Application

```bash
python app.py
```

Application will run on:

```text
http://localhost:8080
```

## API Endpoints

### Home

```http
GET /
```

### Metrics

```http
GET /metrics
```

### Analyze Incident

```http
POST /analyze
```

Example Request:

```json
{
  "incident_id": "INC001",
  "service": "Payment-Service",
  "severity": "High"
}
```

### Get All Incidents

```http
GET /incidents
```

### Get Incident by ID

```http
GET /incident/<incident_id>
```

### Login

```http
POST /login
```

## Dashboard

Access dashboard:

```text
http://3.109.115.108:8080/dashboard
```

## AWS Deployment

The project is deployed on AWS EC2 using:

- Amazon Linux
- Flask
- MariaDB
- GitHub

## Learning Outcomes

- Cloud Deployment on AWS EC2
- Database Integration with MariaDB
- REST API Development
- JWT Authentication
- Linux Server Management
- Git and GitHub Version Control

## Author

Akanksha Mane

GitHub:
https://github.com/maneakanksha2045-spec

# Smart Medicine Safety & Drug Interaction Assistant

## Overview

Smart Medicine Safety & Drug Interaction Assistant is an AI-powered healthcare application designed to improve medication safety by helping users identify medicines, detect potential drug interactions, analyze prescription images, and generate patient-friendly safety reports.

The platform combines OCR, RxNorm clinical terminology, AI-powered explanations, and interactive reporting into a single web-based solution.

---

## Problem Statement

Medication errors and drug interactions are a major cause of preventable healthcare complications worldwide.

Patients often:

- Take multiple medicines simultaneously.
- Misread prescriptions.
- Are unaware of drug-drug interactions.
- Do not understand medical terminology.
- Lack access to quick medication safety guidance.

This project addresses these challenges through automated medicine validation, interaction screening, prescription scanning, and report generation.

---

## Key Features

### User Authentication

- Secure registration
- Login system
- Session management
- Password hashing using bcrypt

### Medicine Search Engine

- RxNorm medicine lookup
- Automatic spelling correction
- Medicine validation

### Drug Interaction Analysis

- Multi-drug interaction checking
- Risk identification
- Clinical interaction information

### OCR Prescription Scanner

- Upload prescription images
- Extract medicine names
- Automated medicine recognition

### AI Safety Assistant

- Medicine explanation
- Patient-friendly summaries
- Safety recommendations

### PDF Report Generation

- Downloadable safety reports
- Interaction summaries
- Patient medication records

### Modern Web Dashboard

- Responsive interface
- Animated UI
- Interactive workflow

---

## Technology Stack

### Frontend

- Streamlit
- HTML
- CSS

### Backend

- Python

### APIs

- RxNorm API
- Gemini AI API

### AI & OCR

- Google Gemini
- EasyOCR
- OpenCV

### Data Storage

- JSON-based local storage

### Reporting

- ReportLab PDF Engine

---

## System Architecture

User
↓
Web Dashboard (Streamlit)
↓
Medicine Input / Prescription Upload
↓
OCR Engine
↓
RxNorm Validation
↓
Drug Interaction Engine
↓
AI Safety Analysis
↓
PDF Report Generator
↓
Download Report

---

## Project Structure

```text
Smart-Medicine-Safety-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── authentication.py
│   ├── storage.py
│   ├── rxnorm_engine.py
│   ├── interaction_engine.py
│   ├── ocr_engine.py
│   ├── ai_assistant.py
│   └── pdf_generator.py
│
├── data/
│   ├── users.json
│   ├── medications.json
│   ├── interaction_history.json
│
├── uploads/
├── reports/
│
└── assets/
    ├── screenshots/
    └── images/
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Medicine-Safety-Assistant.git
```

Move into project directory:

```bash
cd Smart-Medicine-Safety-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

## Usage

### Medicine Search

1. Open dashboard
2. Search medicine name
3. View validated medicine information

### Interaction Screening

1. Enter multiple medicines
2. Run safety analysis
3. Review interaction results

### OCR Prescription Analysis

1. Upload prescription image
2. Extract medicines
3. Validate medicines
4. Analyze interactions

### Generate Report

1. Complete analysis
2. Click Generate Report
3. Download PDF

---

## Innovation

This project combines:

- Clinical terminology validation
- Prescription OCR
- AI-powered explanations
- Drug interaction analysis
- Automated reporting

within a single healthcare platform.

---

## Future Enhancements

- Doctor Portal
- Cloud Database Integration
- Appointment Scheduling
- Medication Reminder System
- Multi-language Support
- Mobile Application
- Electronic Health Record Integration

---

## Impact

The solution aims to:

- Improve patient safety
- Reduce medication errors
- Increase healthcare accessibility
- Support medication awareness
- Promote responsible medicine usage

---

## Team

Hackathon Project Submission

Smart Medicine Safety & Drug Interaction Assistant

2026

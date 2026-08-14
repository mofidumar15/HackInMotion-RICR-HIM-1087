# CureDrug – AI-Powered Smart Medicine Safety Assistant

## Overview

CureDrug is an intelligent healthcare web application designed to improve medication safety by helping users identify medicines, detect drug-drug interactions, analyze prescriptions, and receive AI-powered medication guidance.

The platform combines RxNorm clinical terminology services, Optical Character Recognition (OCR), and Generative AI to provide a comprehensive medicine safety ecosystem for patients, pharmacists, healthcare professionals, and researchers.

Medication errors and adverse drug interactions remain one of the leading causes of preventable healthcare complications. CureDrug addresses this challenge through an accessible, user-friendly, and intelligent digital platform.

---

# Problem Statement

Millions of patients consume multiple medications simultaneously without fully understanding:

- Potential drug interactions
- Contraindications
- Medication safety risks
- Prescription instructions
- Medicine identification

Common challenges include:

- Illegible handwritten prescriptions
- Lack of medication awareness
- Drug duplication
- Incorrect self-medication
- Delayed pharmacist consultation

There is a need for a smart healthcare assistant capable of assisting users in understanding medications safely and effectively.

---

# Solution

CureDrug provides a centralized medicine intelligence platform that enables users to:

### Drug Search

Search medicines using standardized RxNorm terminology.

### Interaction Analysis

Identify possible drug-drug interactions between multiple medications.

### OCR Prescription Analysis

Upload prescription images and automatically extract medicine information.

### AI Medication Assistant

Generate patient-friendly explanations and medicine summaries using Generative AI.

### Medicine Intelligence

Provide structured medication information for informed healthcare decisions.

---

# Key Features

## 1. Smart Drug Search

- Medicine lookup
- RxNorm integration
- Medicine normalization
- RxCUI identification
- Standardized terminology retrieval

---

## 2. Drug Interaction Detection

Users can:

- Enter multiple medicines
- Analyze combinations
- Identify potential risks
- View interaction details
- Understand severity levels

---

## 3. OCR Prescription Scanner

Supports:

- Prescription image upload
- Text extraction
- Medicine detection
- Prescription digitization

Technologies:

- OCR Engine
- Image Processing
- Prescription Parsing

---

## 4. AI Medicine Assistant

Powered by Gemini AI.

Capabilities:

- Drug explanation
- Interaction summaries
- Medication guidance
- Patient-friendly responses
- Simplified healthcare communication

---

## 5. Patient Safety Dashboard

Provides:

- Medicine overview
- Interaction reports
- Safety recommendations
- Risk awareness

---

# Technology Stack

## Frontend

- Next.js
- React
- JavaScript
- Tailwind CSS

---

## Backend

- Next.js API Routes
- Node.js

---

## AI Layer

- Gemini AI

---

## Healthcare APIs

- RxNorm API
- NIH Clinical Terminology Services

---

## OCR Layer

- OCR Engine
- Prescription Recognition

---

## Utilities

- Custom Hooks
- Validation Layer
- Service Architecture

---

# Project Structure

```text
CureDrug
│
├── app
│   ├── api
│   │   ├── check-interactions
│   │   ├── drug-search
│   │   └── ocr
│   │
│   ├── layout.js
│   ├── page.js
│   └── globals.css
│
├── components
│   ├── Navbar.js
│   ├── HeroSection.js
│   ├── DrugSearch.js
│   ├── InteractionChecker.js
│   ├── PrescriptionOCR.js
│   ├── RiskCard.js
│   └── Footer.js
│
├── services
│   ├── rxnormService.js
│   ├── interactionService.js
│   ├── geminiService.js
│   └── ocrService.js
│
├── hooks
│   ├── useDrugSearch.js
│   ├── useOCR.js
│   └── useInteractions.js
│
├── utils
│   ├── medicineUtils.js
│   ├── reportUtils.js
│   └── formatters.js
│
├── lib
│   ├── constants.js
│   ├── validators.js
│   ├── helpers.js
│   └── apiClient.js
│
├── docs
│   ├── architecture.md
│   ├── api-documentation.md
│   └── problem-statement.md
│
└── README.md
```

---

# System Architecture

```text
┌─────────────────────────────┐
│          User               │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Next.js Frontend      │
│                             │
│  Drug Search Interface      │
│  OCR Upload Interface       │
│  Interaction Dashboard      │
│  AI Assistant Interface     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Service Layer          │
│                             │
│ RxNorm Service              │
│ Interaction Service         │
│ OCR Service                 │
│ Gemini Service              │
└──────────────┬──────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│RxNorm  │ │ Gemini │ │  OCR   │
│  API   │ │   AI   │ │ Engine │
└────────┘ └────────┘ └────────┘
               │
               ▼
┌─────────────────────────────┐
│     Processed Results       │
│                             │
│ Drug Details                │
│ Interactions                │
│ OCR Output                  │
│ AI Summaries                │
└─────────────────────────────┘
```

---

# Application Workflow

## Drug Search Flow

```text
User
  ↓
Enter Medicine Name
  ↓
RxNorm Service
  ↓
RxNorm API
  ↓
Medicine Information
  ↓
Display Results
```

---

## Interaction Analysis Flow

```text
User
  ↓
Select Medicines
  ↓
Interaction Engine
  ↓
Risk Calculation
  ↓
Interaction Report
  ↓
Patient Guidance
```

---

## OCR Workflow

```text
Prescription Upload
        ↓
Image Processing
        ↓
OCR Extraction
        ↓
Medicine Detection
        ↓
Medicine Verification
        ↓
Structured Output
```

---

## AI Assistant Workflow

```text
Medicine Data
      ↓
Gemini AI
      ↓
Safety Analysis
      ↓
Patient Friendly Explanation
      ↓
User Dashboard
```

---

# Security Considerations

- Input validation
- API request sanitization
- Secure environment variables
- Controlled external API access
- Error handling mechanisms

---

# Future Enhancements

### Phase 2

- Multi-language support
- Voice assistant
- Drug allergy detection
- PDF report generation
- Medication reminders

### Phase 3

- Doctor dashboard
- Pharmacist dashboard
- Electronic prescriptions
- Healthcare provider integration
- Mobile application

---

# Impact

CureDrug aims to:

- Reduce medication errors
- Improve patient awareness
- Support medication adherence
- Simplify prescription understanding
- Enhance medicine safety

---

# Team

Hackathon Project Submission

**Project Name:** CureDrug

**Category:** Healthcare Technology

**Theme:** AI-Powered Medicine Safety & Drug Interaction Intelligence Platform

---

# Disclaimer

CureDrug is an educational and decision-support platform.

The information generated by the application should not replace professional medical advice, diagnosis, or treatment. Users should always consult qualified healthcare professionals before making medication-related decisions.

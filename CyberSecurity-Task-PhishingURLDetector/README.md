# Phishing URL Detection System

## Overview

This project was developed as part of the **Oasis Infobyte Cyber Security Internship (OIBSIP)**.

The objective of this project is to analyze URLs and identify potentially suspicious or phishing websites using security-based URL analysis techniques.

The tool checks different URL characteristics and generates a risk score based on detected phishing indicators.

---

## Objectives

- Analyze URLs for phishing indicators
- Detect suspicious URL patterns
- Identify risky keywords and characters
- Calculate a URL risk score
- Provide security recommendations

---

## Features

- HTTPS verification
- URL length analysis
- Suspicious keyword detection
- Special character analysis
- IP address-based URL detection
- Risk score generation
- Safe/Suspicious classification

---

## Technologies Used

- Python 3
- Regular Expressions
- URL Parsing
- Command Line Interface

---

## Project Structure

```
CyberSecurity-Task-PhishingURLDetector

│
├── Code
│   └── phishing_detector.py
│
├── Screenshots
│   ├── 01_Safe_URL_Test.png
│   ├── 02_Suspicious_URL_Test.png
│   └── 03_Detector_Execution.png
│
├── Reports
│
└── README.md
```

---

## Working Methodology

The system follows these steps:

1. User enters a URL.
2. The program extracts URL characteristics.
3. Multiple security checks are performed.
4. A risk score is calculated.
5. The URL is classified as safe or suspicious.
6. Security recommendations are displayed.

---

## Detection Parameters

The system analyzes:

### HTTPS Security

Checks whether the website uses secure HTTPS communication.

### URL Length

Long and unusual URLs may indicate phishing attempts.

### Suspicious Keywords

Detects words commonly used in phishing links:

- login
- verify
- account
- password
- secure

### Special Characters

Analyzes characters commonly used in suspicious URLs.

### IP Address URLs

Detects URLs using direct IP addresses instead of domain names.

---

## Sample Output

```
PHISHING URL DETECTOR

URL:
http://paypal-login-verify-account.com

Risk Score:
75/100

Result:
Suspicious URL

Reasons:
- No HTTPS security detected
- Suspicious keyword detected: login
- Suspicious keyword detected: verify
```

---

## Learning Outcomes

Through this project, I learned:

- Phishing attack concepts
- URL-based threat detection
- Python automation for cybersecurity
- Security analysis techniques
- Risk-based decision making

---

## Future Enhancements

- Machine Learning based URL classification
- Real-time phishing database checking
- Browser extension integration
- Web dashboard
- Threat intelligence API integration

---

## Disclaimer

This project was developed for educational purposes as part of the Oasis Infobyte Cyber Security Internship.

The tool is intended for security learning and authorized analysis only.

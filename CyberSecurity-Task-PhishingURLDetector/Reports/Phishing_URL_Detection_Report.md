# Phishing URL Detection System Report

## Student Details

**Name:** Akshita Kaul  
**University:** Amity University Mumbai  
**Program:** B.Tech Computer Science Engineering  
**Specialization:** Cybersecurity and Cloud Computing  

**Internship:** Oasis Infobyte Cyber Security Internship (OIBSIP)




# 1. Introduction

Phishing attacks are one of the most common cybersecurity threats where attackers create fake websites or malicious links to steal sensitive information such as usernames, passwords, and financial details.

This project focuses on detecting potentially suspicious URLs by analyzing different URL characteristics and assigning a risk score based on identified phishing indicators.


# 2. Objective

The objectives of this project are:

- To analyze URLs for phishing-related characteristics.
- To identify suspicious URL patterns.
- To implement security checks using Python.
- To calculate a risk score for URLs.
- To provide users with security recommendations.


# 3. Tools and Technologies Used

| Tool/Technology | Purpose |
|---|---|
| Python | Development of detection system |
| Regular Expressions | Pattern detection |
| URL Parsing | URL analysis |
| Command Line Interface | User interaction |


# 4. Project Methodology

The system follows these steps:

1. User enters a URL.
2. The URL is analyzed using multiple security checks.
3. Suspicious indicators are identified.
4. A risk score is calculated.
5. The URL is classified as safe or suspicious.


# 5. Detection Techniques


## 5.1 HTTPS Analysis

The system checks whether the URL uses HTTPS.

URLs without HTTPS are considered less secure because communication may not be encrypted.


## 5.2 URL Length Analysis

Very long URLs can be used by attackers to hide malicious domains or create misleading links.


## 5.3 Suspicious Keyword Detection

The system checks for phishing-related keywords:

- login
- verify
- account
- password
- secure


## 5.4 Special Character Analysis

The system identifies unusual characters that may be used to confuse users or hide malicious URLs.


## 5.5 IP Address Detection

URLs containing direct IP addresses instead of domain names are considered suspicious.


# 6. Implementation

The application was developed using Python.

Workflow:
User URL Input

    ↓

URL Feature Extraction

    ↓

Security Checks

    ↓

Risk Score Calculation

    ↓

Safe/Suspicious Result

# 7. Testing and Results


## Test Case 1: Safe URL

Input:


https://google.com


Result:


Likely Safe URL



## Test Case 2: Suspicious URL

Input:


http://paypal-login-verify-account.com


Detected indicators:

- No HTTPS security
- Suspicious keywords
- Suspicious URL structure

Result:


Suspicious URL



# 8. Screenshots Evidence

The following screenshots demonstrate:

1. Safe URL analysis
2. Suspicious URL detection
3. Program execution


# 9. Challenges Faced

- Understanding phishing URL characteristics.
- Selecting effective detection parameters.
- Implementing URL analysis logic using Python.
- Designing a risk scoring mechanism.


# 10. Learning Outcomes

Through this project, the following skills were developed:

- Understanding phishing attacks.
- Python-based security automation.
- URL threat analysis.
- Basic cybersecurity risk assessment.


# 11. Future Enhancements

Future improvements include:

- Machine learning-based URL classification.
- Integration with threat intelligence APIs.
- Real-time phishing database checking.
- Browser extension implementation.
- Web-based security dashboard.


# 12. Conclusion

This project demonstrates a basic phishing URL detection system capable of identifying suspicious URL patterns using security-based analysis techniques.

The project provided practical understanding of phishing detection, cybersecurity automation

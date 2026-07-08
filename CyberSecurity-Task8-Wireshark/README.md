# CyberSecurity Task 8 - Network Traffic Analysis Using Wireshark

## Overview

This project was completed as part of the **Oasis Infobyte Cyber Security Internship (OIBSIP)**.

The objective of this task was to capture, analyze, and interpret network traffic using **Wireshark** and automate packet analysis using **Python** and **Scapy**. The project demonstrates basic network traffic inspection, protocol analysis, IP analysis, and automated security report generation.

---

## Objectives

- Capture live network traffic using Wireshark
- Analyze captured packets
- Identify network protocols
- Analyze source and destination IP addresses
- Generate an automated network security report using Python

---

## Tools Used

- Wireshark
- Python 3
- Scapy
- Matplotlib
- Windows 11

---

## Features

- Reads PCAP/PCAPNG capture files
- Detects network protocols
- Calculates protocol distribution
- Calculates protocol percentages
- Displays Top Source IP addresses
- Displays Top Destination IP addresses
- Performs basic security analysis
- Generates an automated network report

---

## Project Structure

```
CyberSecurity-Task8-Wireshark

│── Analyzer
│     └── packet_analyzer.py

│── Reports
│     └── Network_Report.txt

│── Screenshots
│     ├── 01_Wireshark_Packet_Capture.png
│     ├── 02_Protocol_Analysis.png
│     ├── 03_NetGuard_Output.png
│     ├── 04_Generated_Report.png
│     └── 05_Project_Structure.png

└── README.md
```

---

## Sample Output

```
NETGUARD SECURITY REPORT

Total Packets Captured : 33274

Protocol Distribution

UDP : 33191 (99.75%)
ICMP : 37 (0.11%)
Other : 46 (0.14%)

Top Source IP Addresses

Top Destination IP Addresses

Security Alerts

Overall Risk Level : LOW
```

---

## Screenshots

The project includes screenshots demonstrating:

- Live packet capture using Wireshark
- Protocol analysis
- Python analyzer output
- Generated security report
- Project folder structure

---

## Learning Outcomes

Through this project, I learned:

- Fundamentals of packet capture
- Network traffic analysis
- PCAP/PCAPNG file analysis
- Protocol identification
- Source and destination IP analysis
- Basic network security monitoring
- Automating packet analysis using Python

---

## Future Improvements

- Advanced threat detection
- Port scan detection
- DNS traffic analysis
- Interactive dashboard
- Graphical data visualization
- PDF report generation
- Risk scoring engine

---

## Disclaimer

This project was developed solely for educational purposes as part of the Oasis Infobyte Cyber Security Internship. Network traffic analysis was performed only on authorized and personal network captures.

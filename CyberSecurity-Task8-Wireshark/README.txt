# NetGuard - Network Traffic Analyzer

## Overview

NetGuard is a Python-based network traffic analysis tool developed using Scapy and Wireshark. It reads packet capture (PCAP/PCAPNG) files, analyzes network traffic, identifies communication patterns, and generates automated security reports.

## Features

- Analyze PCAP/PCAPNG files
- Protocol distribution analysis
- Protocol percentage calculation
- Top Source IP analysis
- Top Destination IP analysis
- Basic security alert detection
- Automatic report generation

## Technologies Used

- Python
- Scapy
- Wireshark
- Matplotlib (Future Enhancements)

## Project Structure

```
NetGuard-Network-Traffic-Analyzer

├── Analyzer
│   └── packet_analyzer.py

├── Captures
│   └── sample_capture.pcapng

├── Reports
│   └── Network_Report.txt

├── Screenshots

├── Documentation

└── README.md
```

## Sample Output

```
NETGUARD SECURITY REPORT

Total Packets Captured

Protocol Distribution

Top Source IP Addresses

Top Destination IP Addresses

Security Alerts

Overall Risk Level
```

## Future Improvements

- Interactive Dashboard
- Threat Detection Engine
- Risk Scoring
- PDF Report Generation
- Data Visualization
- AI-assisted Traffic Analysis

## Disclaimer

This project was developed for educational and cybersecurity learning purposes only.
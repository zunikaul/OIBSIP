# Security Analysis Report

## Project Title
Local Network Security Assessment Using Nmap

## Objective

The objective of this assessment was to identify open ports, 
running services, and possible security risks on a local Windows 
machine using the Nmap network scanning tool.

The assessment was performed only on the local system 
(127.0.0.1) for educational and authorized security testing purposes.

---

# 1. Identified Open Ports

| Port | Service | Description | Risk Level |
|------|---------|-------------|------------|
| 135 | MSRPC | Microsoft Remote Procedure Call service used by Windows components | Medium |
| 445 | SMB/Microsoft-DS | File and printer sharing service | Medium/High |
| 3306 | MySQL | Database service | Medium |
| 6646 | Unknown | Unknown running service | Low/Medium |

---

# 2. Detailed Security Analysis

## Port 135 - Microsoft RPC

### Description

Microsoft Remote Procedure Call (RPC) allows Windows services 
and applications to communicate with each other.

### Security Risk

Exposed RPC services may provide attackers with information 
about Windows services and can become targets if vulnerabilities 
exist.

### Possible Impact

- Unauthorized remote interaction
- Information disclosure
- Exploitation of vulnerable Windows services

### Recommendations

- Keep Windows security patches updated
- Restrict RPC access using firewall rules
- Disable unnecessary services

---

# Port 445 - SMB (Server Message Block)

### Description

SMB is a protocol used for file and printer sharing between 
systems in a network.

### Security Risk

SMB has historically been targeted by attackers due to 
vulnerabilities in older implementations.

A famous example is the WannaCry ransomware attack, 
which exploited an SMB vulnerability to spread across networks.

### Possible Impact

- Unauthorized file access
- Malware propagation
- Network compromise

### Recommendations

- Disable SMBv1
- Apply security updates regularly
- Restrict SMB access to trusted networks only

---

# Port 3306 - MySQL Database

### Description

Port 3306 is commonly used by MySQL database servers.

### Security Risk

If a database service is exposed unnecessarily, attackers 
may attempt unauthorized access through weak credentials 
or configuration weaknesses.

### Possible Impact

- Database theft
- Data modification
- Unauthorized access

### Recommendations

- Use strong database passwords
- Restrict database access
- Do not expose database ports publicly

---

# Unknown Service - Port 6646

### Description

Nmap detected an open port but could not identify the service.

### Security Risk

Unknown services should be investigated because unused 
applications increase the attack surface.

### Recommendations

- Identify the running application
- Disable unnecessary services
- Monitor network activity

---

# Overall Security Assessment

The scan identified multiple active services running on the 
local machine. While these services may be legitimate, 
unnecessary exposed ports increase the attack surface.

Regular patching, firewall configuration, and service 
management are recommended to maintain system security.

---

# Conclusion

Network scanning is an important first step in cybersecurity 
assessment. Tools like Nmap help security professionals 
discover exposed services and identify areas requiring 
security improvements.

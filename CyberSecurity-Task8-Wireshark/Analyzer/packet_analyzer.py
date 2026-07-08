from scapy.all import *
from collections import Counter

# ==========================================
# NetGuard - Network Traffic Analyzer v4
# ==========================================

pcap_file = "../Captures/sample_capture.pcapng"

# Read packets
packets = rdpcap(pcap_file)

protocols = Counter()
source_ips = Counter()
destination_ips = Counter()

# Analyze packets
for packet in packets:

    # Protocol Analysis
    if packet.haslayer(TCP):
        protocols["TCP"] += 1

    elif packet.haslayer(UDP):
        protocols["UDP"] += 1

    elif packet.haslayer(ICMP):
        protocols["ICMP"] += 1

    else:
        protocols["Other"] += 1

    # IP Address Analysis
    if packet.haslayer(IP):
        source_ips[packet[IP].src] += 1
        destination_ips[packet[IP].dst] += 1


# ===============================
# Display Report
# ===============================

print("=" * 50)
print("        NETGUARD SECURITY REPORT")
print("=" * 50)

print(f"\nTotal Packets Captured : {len(packets)}")

print("\nProtocol Distribution")
print("-" * 30)

total = len(packets)

for protocol, count in protocols.items():
    percentage = (count / total) * 100
    print(f"{protocol:<10} {count:<8} ({percentage:.2f}%)")


print("\nTop 5 Source IP Addresses")
print("-" * 30)

for ip, count in source_ips.most_common(5):
    print(f"{ip:<20} {count}")


print("\nTop 5 Destination IP Addresses")
print("-" * 30)

for ip, count in destination_ips.most_common(5):
    print(f"{ip:<20} {count}")


print("\nSecurity Alerts")
print("-" * 30)

if protocols["UDP"] > protocols["TCP"]:
    print("✓ High UDP traffic detected.")

if protocols["ICMP"] > 100:
    print("⚠ Possible ICMP Flood detected.")
else:
    print("✓ No ICMP flooding detected.")

print("\nOverall Risk Level : LOW")
print("=" * 50)


# ===============================
# Save Report to File
# ===============================

report_path = "../Reports/Network_Report.txt"

with open(report_path, "w") as report:

    report.write("=========================================\n")
    report.write("      NETGUARD SECURITY REPORT\n")
    report.write("=========================================\n\n")

    report.write(f"Total Packets Captured : {len(packets)}\n\n")

    report.write("Protocol Distribution\n")
    report.write("------------------------------\n")

    for protocol, count in protocols.items():
        percentage = (count / total) * 100
        report.write(f"{protocol}: {count} ({percentage:.2f}%)\n")

    report.write("\nTop 5 Source IP Addresses\n")
    report.write("------------------------------\n")

    for ip, count in source_ips.most_common(5):
        report.write(f"{ip}: {count}\n")

    report.write("\nTop 5 Destination IP Addresses\n")
    report.write("------------------------------\n")

    for ip, count in destination_ips.most_common(5):
        report.write(f"{ip}: {count}\n")

    report.write("\nSecurity Alerts\n")
    report.write("------------------------------\n")

    if protocols["UDP"] > protocols["TCP"]:
        report.write("High UDP traffic detected.\n")

    if protocols["ICMP"] > 100:
        report.write("Possible ICMP Flood detected.\n")
    else:
        report.write("No ICMP flooding detected.\n")

    report.write("\nOverall Risk Level : LOW\n")

print("\nReport saved successfully!")
print(f"Location: {report_path}")
import re
from urllib.parse import urlparse


print("=" * 50)
print("       PHISHING URL DETECTOR")
print("=" * 50)


url = input("\nEnter URL to analyze: ")


risk_score = 0
reasons = []



if url.startswith("https://"):
    pass
else:
    risk_score += 20
    reasons.append("No HTTPS security detected")



if len(url) > 75:
    risk_score += 20
    reasons.append("URL length is unusually long")



keywords = [
    "login",
    "verify",
    "update",
    "secure",
    "account",
    "bank",
    "password",
    "confirm"
]


for word in keywords:
    if word in url.lower():
        risk_score += 10
        reasons.append(f"Suspicious keyword detected: {word}")



special_chars = ["@", "-", "_"]

for char in special_chars:
    if char in url:
        risk_score += 5
        reasons.append(f"Suspicious character detected: {char}")




ip_pattern = r"https?://\d+\.\d+\.\d+\.\d+"

if re.search(ip_pattern, url):
    risk_score += 30
    reasons.append("URL uses an IP address instead of domain")




if risk_score > 100:
    risk_score = 100




print("\n========== ANALYSIS RESULT ==========")

print(f"URL: {url}")

print(f"\nRisk Score: {risk_score}/100")


if risk_score >= 50:
    print("\nResult: ⚠ Suspicious URL")

else:
    print("\nResult: ✓ Likely Safe URL")


print("\nReasons:")

if reasons:
    for reason in reasons:
        print("-", reason)

else:
    print("No suspicious indicators found.")


print("\nRecommendation:")

if risk_score >= 50:
    print("Avoid opening this URL and verify the source.")

else:
    print("URL appears normal, but always verify unknown links.")

print("=" * 50)
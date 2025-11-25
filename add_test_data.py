# add_test_data.py
# Run this once: python3 add_test_data.py
# Adds 20 realistic detections with random ATT&CK + D3FEND tactics

import sqlite3
import random
from datetime import datetime, timedelta

# Connect to your existing DB
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Realistic field options
detection_names = [
    "Suspicious PowerShell Execution",
    "Living Off the Land Binary (LOLBin) Usage",
    "Lateral Movement via PsExec",
    "Credential Dumping via LSASS Access",
    "Golden Ticket Detected (Pass-the-Ticket)",
    "Kerberoasting Activity",
    "Unusual Child Process of lsass.exe",
    "Ransomware Encryption Behavior",
    "Outbound Connection to Known C2 Domain",
    "Mimikatz Execution Detected",
    "Suspicious WMI Event Subscription",
    "Remote Desktop Brute Force",
    "Exfiltration Over Alternative Protocol",
    "Fileless Malware via PowerShell",
    "Privilege Escalation via UAC Bypass",
    "Suspicious Scheduled Task Creation",
    "Web Shell Detection",
    "DNS Tunneling Activity",
    "BloodHound/Sharphound Execution",
    "ZeroLogon Exploitation Attempt"
]

environments = ["Production", "Development", "Staging", "Cloud", "Endpoint"]
log_sources = [
    "Windows Event Logs", "CrowdStrike Falcon", "Microsoft Defender", "Sysmon",
    "Okta Logs", "AWS CloudTrail", "Azure AD Sign-in Logs", "Splunk Forwarder"
]
siem_types = ["Splunk", "Elastic", "Microsoft Sentinel", "QRadar", "Panther", "Sumo Logic"]

attack_tactics = [
    "Reconnaissance", "Resource Development", "Initial Access", "Execution",
    "Persistence", "Privilege Escalation", "Defense Evasion", "Credential Access",
    "Discovery", "Lateral Movement", "Collection", "Command and Control",
    "Exfiltration", "Impact"
]

defend_tactics = ["Harden", "Detect", "Isolate", "Deceive", "Restore"]

# Clear existing data (optional — remove if you want to keep current data)
c.execute("DELETE FROM detections")
conn.commit()

# Insert 20 random detections
for i in range(20):
    name = random.choice(detection_names)
    environment = random.choice(environments)
    log_source = random.choice(log_sources)
    siem_type = random.choice(siem_types)
    
    # Randomly assign 1–4 ATT&CK tactics
    num_attack = random.randint(1, 4)
    selected_attack = random.sample(attack_tactics, num_attack)
    
    # Randomly assign 1–3 D3FEND tactics (realistic distribution)
    num_defend = random.choices([1, 2, 3], weights=[40, 45, 15], k=1)[0]
    selected_defend = random.sample(defend_tactics, num_defend)
    
    # Random date in last 90 days
    days_ago = random.randint(0, 90)
    created_at = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M:%S")

    c.execute("""
        INSERT INTO detections 
        (name, environment, log_source, siem_type, attack_tactics, defend_tactics, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        environment,
        log_source,
        siem_type,
        ','.join(selected_attack),
        ','.join(selected_defend),
        created_at
    ))

conn.commit()
conn.close()

print("20 realistic test detections added successfully!")
print("Go to http://127.0.0.1:5001/defendreport to see your beautiful dashboard in action!")
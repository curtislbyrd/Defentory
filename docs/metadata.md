# Enterprise Detection Coverage Metadata Dictionary
### For MITRE ATT&CK (Offensive) + D3FEND (Defensive) Mapping & Visibility Across Host, Cloud, and Hybrid Environments


---
$ = must have
% = nice to have

### 1. Detection Content Metadata
| Field                    | Purpose                                                  |
|--------------------------|----------------------------------------------------------|
| Rule / Analytic ID $     | Unique identifier across the enterprise                  |
| Rule Name $                | Human-readable name                                      |
| Implementation Status          | Deployed, Partial, Planned, Not Implemented                     |
| Detection Logic Summary $ | Short description (e.g., “Detects PowerShell downloading from pastebin”) |
| Detection Code  $      | Code for the detection (If using Detections as Code)                        |
| Detection Type  $        |                                                    Analytic, Behavioral, Anomaly, Threat Intel Match, ML-based |
| Detection Confidence $   | Overall reliability (High / Medium / Low) based on FP rate, visibility, etc.  |
| False Positive Rate   %   | Low / Medium / High (or numeric)                         |
| Mean Time to Detect (MTTD) %| Measured or estimated detection latency                  |
| Evidence Source   $             | Defender logs, EDR blocked events, MFA failure alerts, firewall deny logs |
| Validated Date   | 2025-11-20, 2025-08-15, Never - Used for checkups                                   |                                      |

---



### 2. MITRE D3FEND Countermeasures Metadata (Defensive Coverage)

| Field                          | Example Values / D3FEND IDs                                      |
|--------------------------------|------------------------------------------------------------------|
| D3FEND Tactic $                 | Harden, Detect, Isolate, Deceive, Evict                          |
| D3FEND Technique ID(s) $       | D3-ET, D3-ANPS, D3-MPA, D3-EXE, D3-NSE                           |
| Defensive Technique Name $      | Executable Allowlisting, Anti-Malware Scan, Multi-Factor Authentication, Network Segmentation |
| Detects ATT&CK Technique(s) $   | T1078 (failed MFA), T1059.001 (blocked execution)               |
| Prevents ATT&CK Technique(s) %  | T1059.001, T1078.004, T1210, T1021.001                           |
| Mitigates ATT&CK Technique(s) % | T1566.001, T1110, T1078                                          |
| Control Maturity  %             | Initial, Managed, Defined, Optimized                             |
| Bypass Feasibility  $            | Low, Medium, High, Known Public Bypass                           |


---
**Why this D3FEND section is critical for a mature program:**

- Shows **prevention** coverage (most orgs only track detection)
- Enables **kill chain disruption scoring** (how many phases are hardened?)
- Supports **defensive gap analysis** (“We detect T1059.001 well, but don’t prevent it at all”)
- Powers **risk-based prioritization** (focus on high-impact missing countermeasures)
- Directly answers leadership questions like: “Are we just detecting attacks, or actually stopping them?”


### 4. Log Visibility & Coverage Metadata - Not valid until log reporting module 
| Field                   | Why It Matters                                              |
|-------------------------|-------------------------------------------------------------|
| Covered Assets %        | % of endpoints/servers/cloud accounts with this source     |
| Deployment Status       | Current rollout state                                       | Deployed, Partial, Planned, Not Feasible |
| Geographic Scope        | Data residency & collection boundaries                      | Global, US-only, EU-only |
| Environment Scope       | Which environments are included                             | Prod only, Prod + Dev, All |
| Collection Frequency    | Latency of detection capability                             | Real-time, Hourly, Daily |
| Data Retention          | How long raw events are available                           | 30 days, 90 days, 1 year |

---

### 5. Host / Endpoint-Specific Metadata
| Field                        | Example Values                              |
|------------------------------|---------------------------------------------|
| OS Type & Version            | Windows 10 22H2, Ubuntu 20.04, macOS Ventura |
| Sensor/Agent Version         | CrowdStrike 6.44, Defender 10.8230          |
| Process Command Line Logging | Enabled / Disabled                          |
| Script Block Logging / AMSI  | Enabled / Disabled                          |

---

### 6. Cloud & Hybrid-Specific Metadata
| Field                     | Example Values                                           |
|---------------------------|----------------------------------------------------------|
| Cloud Provider            | AWS, Azure, GCP, Multi-cloud                             |
| Cloud Service Coverage    | EC2, Lambda, S3, Azure VMs, AKS, GuardDuty, Defender for Cloud |
| Control Plane Logging     | CloudTrail, Azure Activity Log, GCP Admin Activity      |
| Data Plane Logging        | VPC Flow Logs, S3 Access Logs, GuardDuty Findings       |
| SaaS Applications         | Office 365, Okta, Salesforce, GitHub                    |
| Identity Provider Coverage| Azure AD, Okta, Ping, On-prem AD                        |

---
### 7. Data Source Metadata (Core for Coverage Mapping)
| Field                  | Why It Matters                                      | Example Values                                      |
|------------------------|-----------------------------------------------------|-----------------------------------------------------|
| Data Source Name       | Human-readable identifier                           | Microsoft Defender for Endpoint, CrowdStrike Falcon, AWS CloudTrail |
| Data Source Type       | Categorizes the telemetry type                      | EDR, NDR, Cloud Logs, IAM Logs, Firewall, SIEM     |
| Platform / Environment | Indicates where the data lives                      | AWS, Azure, GCP, Windows, Linux, macOS, Kubernetes, SaaS (O365, Okta) |
| Vendor / Product       | Tracks vendor-specific gaps and capabilities        | Microsoft, Crowdstrike, Palo Alto Cortex, Splunk, SentinelOne |
| Log Type / Event Type  | Granular source of the telemetry                    | Process Creation, DNS Query, CloudTrail Management Event, Okta SystemLog |

---

### 8. Gaps & Recommendations Metadata
| Field                   | Use                                                         |
|-------------------------|-------------------------------------------------------------|
| Coverage Gap Reason     | Why visibility/detection is missing                         | No sensor, No logging, Cost, Technical limitation |
| Recommended Data Source | Actionable next step                                        | “Enable OSQuery fleet”, “Turn on CloudTrail data events” |
| Priority                | Business impact of the gap                                  | P0 (Critical), P1, P2, P3 |
| Effort to Implement     | Resource requirement to close the gap                       | Low / Medium / High |

---



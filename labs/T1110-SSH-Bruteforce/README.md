# T1110 - SSH Brute Force Detection Lab

![MITRE ATT&CK](https://img.shields.io/badge/MITRE-T1110.001-red)
![Wazuh](https://img.shields.io/badge/Wazuh-4.x-blue)
![Status](https://img.shields.io/badge/Status-In_Progress-green)

## Executive Summary

This lab demonstrates how an SSH brute force attack can be simulated, detected, and analyzed using Wazuh.  
The main focus of this lab is not only detecting failed SSH login attempts, but also explaining the detection logic, MITRE ATT&CK mapping, and incident analysis workflow.

## Technique

- MITRE ATT&CK ID: T1110.001
- Technique: Brute Force
- Sub-technique: Password Guessing
- Tactic: Credential Access
- Scenario: SSH password guessing against an Ubuntu server

## Lab Environment

| Component | Role |
|---|---|
| Kali Linux | Attacker machine |
| Ubuntu 24.04 | SSH target and Wazuh-monitored host |
| Wazuh Manager | SIEM and detection engine |
| Wazuh Dashboard | Alert visualization |
| Hydra | Attack simulation tool |
| Airia AI | AI-assisted incident analysis |

## Attack Flow

```text
Kali Linux
    ↓
Hydra SSH Brute Force
    ↓
Ubuntu SSH Server
    ↓
Wazuh SSHD Logs
    ↓
Custom Rule 100200
    ↓
MITRE ATT&CK Mapping
    ↓
AI-Assisted Incident Analysis
```

## Documents in This Lab

| Document | Covers |
|---|---|
| [attack.md](attack.md) | Attack simulation setup and password list |
| [detection.md](detection.md) | Detection logic and custom rule walkthrough |
| [mitre.md](mitre.md) | MITRE ATT&CK mapping and rationale |
| [threshold-tuning.md](threshold-tuning.md) | Why `frequency=3`, `timeframe=60`, `level=12` were chosen |
| [false-positive-analysis.md](false-positive-analysis.md) | Legitimate scenarios that could trigger this rule |
| [ai-assisted-analysis.md](ai-assisted-analysis.md) | How the AI triage layer explains this alert |

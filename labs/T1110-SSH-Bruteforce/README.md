# T1110 - SSH Brute Force Detection Lab

## Executive Summary

This lab demonstrates how an SSH brute force attack can be simulated, detected, and analyzed using Wazuh.  
The main focus of this lab is not only detecting failed SSH login attempts, but also explaining the detection logic, MITRE ATT&CK mapping, and incident analysis workflow.

## Technique

- MITRE ATT&CK ID: T1110
- Technique: Brute Force
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

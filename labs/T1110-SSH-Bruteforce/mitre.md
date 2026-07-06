# MITRE ATT&CK Mapping

## Objective

This lab maps the simulated SSH brute force attack to the MITRE ATT&CK framework in order to provide a standardized description of the observed adversary behavior.

---

# Technique

| Field | Value |
|---------|-------------|
| Tactic | Credential Access |
| Technique | Brute Force |
| Sub-technique | Password Guessing |
| MITRE ID | T1110.001 |

---

# Why T1110.001?

The attack performed in this laboratory uses Hydra to repeatedly attempt different passwords against a single SSH account.

Characteristics of the attack:

- Same username
- Multiple password attempts
- SSH authentication
- Password guessing
- Repeated failures before success

This behavior directly matches the MITRE ATT&CK sub-technique:

**T1110.001 - Password Guessing**

---

# Attack Flow

```text
Kali Linux
      │
      ▼
Hydra
      │
      ▼
SSH Password Guessing
      │
      ▼
Ubuntu SSH Server
      │
      ▼
Authentication Logs
      │
      ▼
Wazuh Detection
      │
      ▼
Rule 100200
```

---

# Detection Mapping

| Detection Stage | Description |
|-----------------|-------------|
| Event Source | OpenSSH Authentication Logs |
| Detection Engine | Wazuh Manager |
| Detection Type | Correlation Rule |
| Rule ID | 100200 |
| MITRE Mapping | T1110.001 |

---

# Why MITRE ATT&CK?

Using MITRE ATT&CK provides a common language for describing attacker behavior.

Instead of saying:

"SSH brute force"

the detection can be classified as:

Credential Access → T1110.001 → Password Guessing

This makes detections easier to understand, document, and compare with other security tools.

---

# Lessons Learned

During this lab:

- SSH brute force activity was successfully mapped to MITRE ATT&CK.
- The custom Wazuh detection rule was associated with T1110.001.
- MITRE mapping improved the context available to security analysts during incident investigation.

# False Positive Analysis

## Objective

A good detection rule should identify malicious activity while minimizing unnecessary alerts.

This document analyzes situations where repeated SSH authentication failures may appear suspicious but are actually legitimate.

---

# Why False Positives Matter

Every unnecessary alert consumes analyst time.

If a detection rule generates excessive false positives, analysts may begin to ignore alerts or spend valuable time investigating benign activity.

Detection engineering aims to maximize detection quality while minimizing alert fatigue.

---

# Possible False Positive Scenarios

## Scenario 1 – User Mistyped Password

A user accidentally enters an incorrect password multiple times before successfully logging in.

Example:

```text
Failed password
Failed password
Failed password
Accepted password
```

This behavior is common and does not necessarily indicate malicious activity.

---

## Scenario 2 – Outdated Automation Script

An automation script continues attempting authentication using an old password.

The repeated authentication failures resemble a brute-force attack even though the source is a legitimate internal system.

---

## Scenario 3 – System Administrator Error

A system administrator attempts to connect to a server using outdated credentials after a password change.

Multiple authentication failures may occur before the correct password is used.

---

## Scenario 4 – Monitoring or Backup Software

Backup or monitoring applications may repeatedly authenticate using stored credentials.

If those credentials become invalid, authentication failures may trigger the detection rule.

---

# Why Rule 100200 Still Adds Value

The custom rule does not claim that every repeated authentication failure is malicious.

Instead, it increases analyst awareness by identifying activity that deserves investigation.

The alert should be considered an indicator rather than proof of compromise.

---

# Investigation Checklist

When Rule 100200 is triggered, the analyst should verify:

- Source IP address
- Target username
- Number of authentication failures
- Successful login after failures
- Geographical location (if available)
- Historical login activity
- Related alerts

---

# Future Improvements

Potential enhancements include:

- Correlating source IP addresses
- Correlating usernames
- Whitelisting trusted automation systems
- Integrating threat intelligence feeds
- Risk-based alert scoring

---

# Lessons Learned

Detection engineering is not about eliminating all false positives.

It is about producing alerts that provide meaningful context and support efficient analyst decision-making.

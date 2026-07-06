# Threshold Tuning

## Objective

Detection engineering is not only about creating detection rules.

It is also about selecting thresholds that balance detection quality and false positive reduction.

This document explains why the current threshold values were selected for the SSH brute-force detection rule.

---

# Initial Detection Rule

Custom Rule

```
Rule ID: 100200
```

Configuration

```
frequency = 3
timeframe = 60
level = 12
```

---

# Threshold Validation

Several threshold values were evaluated during testing.

| Frequency | Observation | Decision |
|------------|-------------|----------|
| 1 | Too many alerts generated from normal user mistakes | Rejected |
| 2 | Reduced noise but still triggered during common authentication errors | Rejected |
| 3 | Good balance between sensitivity and alert quality | Selected |
| 5 | Some short brute-force attacks could be missed | Rejected |

---

# Why Frequency = 3?

A single failed SSH login attempt is not unusual.

Examples include:

- Typing mistakes
- Incorrect passwords
- Expired credentials
- SSH client configuration errors

Multiple consecutive failures within a short period provide stronger evidence of malicious behavior.

For this laboratory, three failed authentication attempts offered a practical balance between detection capability and alert quality.

---

# Why Timeframe = 60 Seconds?

Brute-force attacks usually generate authentication failures rapidly.

Using a 60-second observation window allows repeated authentication failures to be correlated while avoiding long monitoring windows that could combine unrelated events.

---

# Why Level = 12?

Severity Level 12 was selected because repeated authentication failures indicate a significantly higher risk than a single failed login.

This alert should attract analyst attention but still requires investigation before concluding that malicious activity occurred.

---

# Engineering Trade-offs

Lower thresholds:

Advantages

- Faster detection

Disadvantages

- More false positives

Higher thresholds:

Advantages

- Fewer alerts

Disadvantages

- Lower detection sensitivity

---

# Final Decision

The following values were selected for this laboratory:

| Parameter | Value |
|------------|-------|
| Frequency | 3 |
| Timeframe | 60 Seconds |
| Severity | 12 |

These values provided the best balance between detection accuracy and operational usability within the scope of this project.

---

# Lessons Learned

Threshold tuning is one of the most important aspects of detection engineering.

Well-designed thresholds improve alert quality while reducing unnecessary analyst workload.

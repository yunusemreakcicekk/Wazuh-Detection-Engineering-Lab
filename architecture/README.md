# Architecture

This directory contains the architecture documentation for the Wazuh Detection Engineering Lab.

## Main Workflow

The lab follows this workflow:

```text
Attack Simulation
↓
Log Collection
↓
Detection Rules
↓
Correlation Rule
↓
MITRE Mapping
↓
Incident Analysis
↓
AI-Assisted Triage
```

Detection is performed entirely by Wazuh. The AI-assisted triage step only
runs after Wazuh has already generated an alert - it explains the alert in
plain language, it does not decide whether an alert fires.

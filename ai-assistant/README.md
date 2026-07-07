# AI-Assisted Incident Analysis

This folder is a small helper layer on top of Wazuh alerts. It is **not**
a detection engine and it does **not** replace Wazuh.

- Detection (matching failed logins, thresholds, correlation) is performed
  entirely by Wazuh rules - see [`custom-rules/100200.xml`](../custom-rules/100200.xml).
- This code only takes an alert that Wazuh already generated, extracts the
  useful fields, and (optionally) asks an AI model to explain it in plain
  language and suggest next steps for the analyst.
- If the AI service is not configured or unreachable, the scripts fall back
  to a simple local summary instead of failing.

## Files

| File | Purpose |
|---|---|
| `alert_parser.py` | Reads a Wazuh alert JSON and extracts the relevant fields. |
| `airia_client.py` | Minimal client for calling the Airia AI API. |
| `report_generator.py` | Builds a markdown incident summary (AI or local fallback). |
| `config.example.py` | Template for the Airia endpoint URL. Copy to `config.py`. |
| `sample_alert.json` | Sanitized example Wazuh alert (SSH brute force, rule 100200). |
| `requirements.txt` | Python dependencies. |

## How to run

```bash
pip install -r requirements.txt

# 1. Parse a sample alert and print the extracted fields
python alert_parser.py sample_alert.json

# 2. Generate an incident report (AI summary if configured, local fallback otherwise)
python report_generator.py sample_alert.json
```

## Enabling the AI summary (optional)

1. Copy `config.example.py` to `config.py` and set your Airia endpoint/model.
2. Set your API key as an environment variable (never hardcode it):

```bash
# Linux/macOS
export AIRIA_API_KEY="your-key"

# Windows PowerShell
$env:AIRIA_API_KEY = "your-key"
```

Without a valid key/endpoint, `report_generator.py` still works and simply
produces the local fallback summary.

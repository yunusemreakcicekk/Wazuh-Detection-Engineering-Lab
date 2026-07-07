# Screenshots

This folder holds Wazuh dashboard and alert screenshots that support the
labs in this repository (e.g. triggered alerts, rule test results).

Screenshots are grouped in a subfolder per lab, in the order they occur in
the attack -> detection -> AI-assisted analysis workflow.

## [`T1110-SSH-Bruteforce/`](T1110-SSH-Bruteforce/)

| File | Shows |
|---|---|
| `01-hydra-attack.png` | Hydra SSH password guessing attack from Kali against the target user |
| `02-wazuh-events-overview.png` | Wazuh Threat Hunting events view, default rule `5760` escalating to custom rule `100200` |
| `03-wazuh-alert-detail.png` | Full document detail of the triggered `100200` alert |
| `04-custom-rule-100200.png` | The custom detection rule (`custom-rules/100200.xml`) |
| `05-ai-analysis-output-1.png` | Live terminal output of `report_generator.py` (part 1) |
| `06-ai-analysis-output-2.png` | Live terminal output of `report_generator.py` (part 2) |

These are referenced inline in [`labs/T1110-SSH-Bruteforce/`](../labs/T1110-SSH-Bruteforce/).

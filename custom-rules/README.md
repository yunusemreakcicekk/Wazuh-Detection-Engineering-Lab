# Custom Rules

This folder contains custom Wazuh detection rules written for this lab.
Rules are added to a Wazuh Manager via **Rules > Custom rules** (or by
placing the file under `/var/ossec/etc/rules/` and restarting the manager).

## [`100200.xml`](100200.xml) - SSH Brute Force Attack Detected

```xml
<group name="local,syslog,sshd,">
  <rule id="100200" level="12" frequency="3" timeframe="60">
    <if_matched_sid>5760</if_matched_sid>
    <description>Custom Detection: SSH Brute Force Attack Detected</description>
    <mitre>
      <id>T1110.001</id>
    </mitre>
    <group>brute_force,credential_access,custom_soc_lab,ssh_bruteforce,</group>
  </rule>
</group>
```

| Line | Field | Meaning |
|---|---|---|
| `<group name="local,syslog,sshd,">` | Parent group | Places the rule alongside Wazuh's built-in `syslog`/`sshd` rule groups so it inherits the same decoding context. |
| `id="100200"` | Rule ID | Custom rule IDs must be outside Wazuh's reserved built-in range (0-99999). `100200` is in the local/custom range. |
| `level="12"` | Severity | High severity - repeated authentication failures are a stronger signal than a single failed login (see [threshold-tuning.md](../labs/T1110-SSH-Bruteforce/threshold-tuning.md)). |
| `frequency="3"` | Correlation count | The rule only fires after the referenced event (`if_matched_sid`) has occurred **3 times**. |
| `timeframe="60"` | Correlation window | Those 3 occurrences must happen within a **60-second** window, or the counter resets. |
| `<if_matched_sid>5760</if_matched_sid>` | Base event | `5760` is Wazuh's built-in "sshd authentication failed" rule. This custom rule correlates repeated hits of that rule rather than inspecting raw logs itself. |
| `<description>` | Alert title | Human-readable text shown in the Wazuh dashboard for this alert. |
| `<mitre><id>T1110.001</id></mitre>` | MITRE ATT&CK mapping | Tags the alert with sub-technique **T1110.001 - Password Guessing** (see [mitre.md](../labs/T1110-SSH-Bruteforce/mitre.md)). |
| `<group>brute_force,credential_access,custom_soc_lab,ssh_bruteforce,</group>` | Rule groups | Free-text tags used for filtering/searching in the Wazuh dashboard and for grouping this rule with other lab rules. |

### Why correlate instead of matching raw logs directly

A single failed SSH login (rule `5760`) is common and often benign - see
[false-positive-analysis.md](../labs/T1110-SSH-Bruteforce/false-positive-analysis.md).
Rule `100200` does not re-parse the SSH log; it uses Wazuh's built-in
`frequency`/`timeframe` correlation to escalate only when the same
underlying event repeats fast enough to suggest a brute-force attempt,
rather than firing high-severity alerts on every single failure.

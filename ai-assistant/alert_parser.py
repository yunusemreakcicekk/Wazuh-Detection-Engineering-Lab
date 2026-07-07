"""
alert_parser.py

Reads a Wazuh alert (JSON) and extracts the fields needed for
AI-assisted analysis. Missing fields never raise an error - they
are simply reported as "N/A" so the pipeline keeps working even
with partial or malformed alerts.
"""

import json
import sys


def safe_get(data: dict, path: str, default: str = "N/A"):
    """
    Walk a dotted path (e.g. "rule.mitre.id") through nested dicts/lists
    and return the value, or `default` if any part of the path is missing.
    """
    current = data
    for key in path.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    # Wazuh often stores mitre id/tactic/technique as lists -> flatten to a string
    if isinstance(current, list):
        return ", ".join(str(item) for item in current) if current else default

    if current in (None, ""):
        return default

    return current


def load_alert(file_path: str) -> dict:
    """
    Load a Wazuh alert JSON file from disk.

    Wazuh Dashboard's "View JSON" export wraps the actual alert fields
    inside a top-level "_source" key (alongside _index/_id/_score
    metadata). Unwrap it so the same field paths work whether the file
    came from that export or is a plain alert object.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        alert = json.load(f)

    if isinstance(alert, dict) and "_source" in alert:
        return alert["_source"]
    return alert


def parse_alert(alert: dict) -> dict:
    """
    Extract the fields relevant to incident analysis and return a
    clean dictionary that can be handed off to the AI client.
    """
    return {
        "rule_id": safe_get(alert, "rule.id"),
        "rule_description": safe_get(alert, "rule.description"),
        "rule_level": safe_get(alert, "rule.level"),
        "mitre_id": safe_get(alert, "rule.mitre.id"),
        "mitre_tactic": safe_get(alert, "rule.mitre.tactic"),
        "mitre_technique": safe_get(alert, "rule.mitre.technique"),
        "src_ip": safe_get(alert, "data.srcip"),
        "dst_user": safe_get(alert, "data.dstuser"),
        "full_log": safe_get(alert, "full_log"),
        "agent_name": safe_get(alert, "agent.name"),
        "timestamp": safe_get(alert, "timestamp"),
    }


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "sample_alert.json"

    alert = load_alert(file_path)
    parsed = parse_alert(alert)

    print(json.dumps(parsed, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

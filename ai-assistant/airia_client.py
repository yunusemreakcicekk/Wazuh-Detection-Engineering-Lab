"""
airia_client.py

Minimal, safe client skeleton for calling the Airia AI API.

Security notes:
- The API key is NEVER hardcoded here. It is read only from the
  AIRIA_API_KEY environment variable.
- The endpoint and model name are read from config.py (copy
  config.example.py to config.py and edit it - config.py is not
  committed to the repository).
"""

import os
import requests

try:
    # config.py is the user's local copy (see config.example.py).
    from config import AIRIA_API_ENDPOINT, MODEL_NAME
except ImportError:
    # No local config.py yet - fall back to the same placeholders
    # shown in config.example.py so the script can still be imported.
    AIRIA_API_ENDPOINT = "https://your-airia-endpoint.example/api"
    MODEL_NAME = "your-soc-playbook-model"


class AiriaClientError(Exception):
    """Raised when the Airia client cannot be used or a call fails."""


class AiriaClient:
    """Small wrapper around the Airia AI API for alert analysis."""

    def __init__(self):
        api_key = os.environ.get("AIRIA_API_KEY")
        if not api_key:
            raise AiriaClientError(
                "AIRIA_API_KEY environment variable is not set.\n"
                "Set it before running, e.g.:\n"
                "  Windows PowerShell : $env:AIRIA_API_KEY = 'your-key'\n"
                "  Linux/macOS        : export AIRIA_API_KEY='your-key'"
            )

        self.api_key = api_key
        self.endpoint = AIRIA_API_ENDPOINT
        self.model_name = MODEL_NAME

    def analyze_alert(self, parsed_alert: dict) -> str:
        """
        Send a parsed Wazuh alert to Airia and return the AI-generated
        explanation/recommendation as plain text.

        Returns None if the call fails, so the caller can fall back to
        a local summary instead of crashing.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model_name,
            "alert": parsed_alert,
        }

        try:
            response = requests.post(
                self.endpoint, json=payload, headers=headers, timeout=15
            )
            response.raise_for_status()
            return response.json().get("output", "N/A")
        except requests.RequestException as exc:
            print(f"[airia_client] Airia API call failed: {exc}")
            return None

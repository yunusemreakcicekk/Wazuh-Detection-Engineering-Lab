"""
airia_client.py

Minimal, safe client for calling the Airia Pipeline Execution API.

Security notes:
- The API key is NEVER hardcoded here. It is read only from the
  AIRIA_API_KEY environment variable.
- The endpoint is read from config.py (copy config.example.py to
  config.py and edit it - config.py is not committed to the repository).
  It is the per-agent URL shown under Agent Studio -> Settings ->
  Interfaces -> View API Info for the pipeline you built in Airia.

API contract (per Airia's Pipeline Execution API):
- Auth header : X-API-KEY: <your key>
- Body        : {"userInput": "<text>", "asyncOutput": false}
- The model/pipeline itself is selected by which endpoint URL you call,
  not by a field in the request body.
"""

import os
import requests

try:
    # config.py is the user's local copy (see config.example.py).
    from config import AIRIA_API_ENDPOINT
except ImportError:
    # No local config.py yet - fall back to the same placeholder
    # shown in config.example.py so the script can still be imported.
    AIRIA_API_ENDPOINT = "https://your-airia-endpoint.example/api"


class AiriaClientError(Exception):
    """Raised when the Airia client cannot be used or a call fails."""


class AiriaClient:
    """Small wrapper around the Airia Pipeline Execution API."""

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

    def analyze_alert(self, prompt: str) -> str:
        """
        Send a text prompt (built from a parsed Wazuh alert) to the
        Airia pipeline and return the AI-generated response as plain text.

        Returns None if the call fails, so the caller can fall back to
        a local summary instead of crashing.
        """
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
        }
        payload = {
            "userInput": prompt,
            "asyncOutput": False,
        }

        try:
            response = requests.post(
                self.endpoint, json=payload, headers=headers, timeout=30
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            print(f"[airia_client] Airia API call failed: {exc}")
            return None

        # The exact response shape depends on how the pipeline's output
        # node is configured. Try common field names first, otherwise
        # fall back to the raw response body.
        try:
            data = response.json()
        except ValueError:
            return response.text

        if isinstance(data, dict):
            for key in ("result", "output", "response", "text"):
                if key in data:
                    return data[key]
        return response.text

"""
config.example.py

Copy this file to config.py and fill in your own values.
config.py is not committed to the repository - the API key itself
is never stored here, it is only ever read from an environment
variable (see airia_client.py).
"""

# Per-agent Pipeline Execution URL from Airia:
# Agent Studio -> Settings -> Interfaces -> View API Info.
# The pipeline/model itself is baked into this URL, not passed in the request.
AIRIA_API_ENDPOINT = "https://your-airia-endpoint.example/api"

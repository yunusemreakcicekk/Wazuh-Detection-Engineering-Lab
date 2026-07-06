"""
config.example.py

Copy this file to config.py and fill in your own values.
config.py is not committed to the repository - the API key itself
is never stored here, it is only ever read from an environment
variable (see airia_client.py).
"""

# Placeholder endpoint - replace with your actual Airia deployment URL.
AIRIA_API_ENDPOINT = "https://your-airia-endpoint.example/api"

# Name of the model/pipeline configured in Airia for SOC playbook analysis.
MODEL_NAME = "your-soc-playbook-model"

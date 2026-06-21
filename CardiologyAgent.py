import requests
import os
import uuid

api_key = 'sk-GehHxbXrGEGxOI6EyeCRhOiwKVrVI_KY717BskvQXU0'
url = "http://localhost:7860/api/v1/run/76a78ae4-edc8-4391-b488-94b4ab170b6d"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Hello, how are you?"
}
payload["session_id"] = str(uuid.uuid4())

headers = {"x-api-key": api_key}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
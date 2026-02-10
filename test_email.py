import requests
import json

url = "http://127.0.0.1:8000/send-email"
payload = {
    "to_email": "test@example.com",
    "subject": "Test Subject",
    "content": "This is a test email content."
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

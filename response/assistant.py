import requests, dotenv, os

dotenv.load_dotenv()



API_KEY = os.getenv("CLAUDE_KEY")
API_URL = "https://api.anthropic.com/v1/complete"

prompt = "Hello, Claude! How are you doing today?"

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

data = {
    "prompt": prompt,
    "model": "claude-v1",
    "max_tokens_to_sample": 100
}

response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["completion"])
else:
    print(f"Request failed with status code: {response.status_code}")
import os, requests

def chat(system, user):
    base = os.environ['AI_BASE_URL'].rstrip('/')
    url = base if base.endswith('/chat/completions') else base + '/chat/completions'
    response = requests.post(url, headers={'Authorization': f"Bearer {os.environ['AI_API_KEY']}", 'Content-Type': 'application/json'}, json={'model': os.environ['AI_MODEL'], 'temperature': 0.1, 'messages': [{'role':'system','content':system},{'role':'user','content':user}]}, timeout=180)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

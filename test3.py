import requests

# Configuration
base_url = "http://185.127.204.58:8000/v1"
api_key = "tom"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Initial system message
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. If you do not know the answer, reply I don't know, don't make things up."
    }
]


# Function to get a response from the LLaMa server
def get_response(prompt):
    messages.append({"role": "user", "content": prompt})
    payload = {
        "messages": messages
    }
    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        completion = response.json()
        assistant_message = completion['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message
    else:
        return f"Error: {response.status_code} - {response.text}"


# Main loop for interaction
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    assistant_output = get_response(user_input)
    print(f"Assistant: {assistant_output}")

import requests
import streamlit as st

# Configuration
base_url = "http://185.127.204.58:8000/v1"
api_key = "tom"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """You are a helpful assistant. If you do not know the answer, reply I don't know 
                don't make things up.""",
        }
    ]

# Streamlit UI
st.title("🚀 LLaMa CPP Local OpenAI server")
for message in st.session_state["messages"]:
    st.markdown(f"**{message['role'].capitalize()}:** {message['content']}")

# Input prompt from user
prompt = st.text_input("Pass your input here")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.markdown(f"**User:** {prompt}")

    payload = {
        "messages": st.session_state["messages"]
    }

    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        completion = response.json()
        assistant_message = completion['choices'][0]['message']['content']
        st.session_state["messages"].append({"role": "assistant", "content": assistant_message})
        st.markdown(f"**Assistant:** {assistant_message}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

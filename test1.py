from openai import OpenAI
import streamlit as st

# Set up the OpenAI client
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="tom",
)

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
for message in st.session_state.messages:
    st.markdown(f"**{message['role'].capitalize()}:** {message['content']}")

# Input prompt from user
prompt = st.text_input("Pass your input here")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"**User:** {prompt}")

    response = client.chat_completions.create(
        messages=st.session_state.messages,
    )

    assistant_message = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    st.markdown(f"**Assistant:** {assistant_message}")

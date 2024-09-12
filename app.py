import os
import time
import streamlit as st


st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


def get_chat_response(prompt):
    return prompt
    
def stream_response(response):
    for chunk in response:
        for ch in chunk.text.split(" "):
            yield ch
            time.sleep(0.05)


if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.chat_message(
        "assistant",
    ):
        response = get_chat_response(prompt)
        msg = st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": msg})

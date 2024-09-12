import os
import time
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCGjhOruoVxcmKe_OdAgolfHJRhTupzoG4")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-exp-0827",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat()

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


def get_chat_response(prompt):
    response = chat_session.send_message(prompt)
    return response.text


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
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

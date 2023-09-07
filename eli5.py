import streamlit as st
from octoai.client import Client

client = Client()

def eli5(paragraph):
    llama2_7b_url = "https://llama-2-70b-chat-demo-4jkxk521l3v1.octoai.run/v1/chat/completions"
    llama2_7b_health_url = "https://llama-2-70b-chat-demo-4jkxk521l3v1.octoai.run/v1/models"

    inputs = {
    "model": "llama-2-70b-chat",
    "messages": [
        {
        "role": "system",
        "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request."
        },
        {
        "role": "user",
        "content": "Re-write for a 5 year old to understand: {}".format(paragraph)
        }
    ],
    "stream": False,
    "max_tokens": 2048
    }

    # For llama2, you'll replace the quickstart template endpoint URL.
    if client.health_check(llama2_7b_health_url) == 200:
        outputs = client.infer(endpoint_url=llama2_7b_url, inputs=inputs)

    # Parse Llama2 outputs and print
    text = outputs.get('choices')[0].get("message").get('content')
    st.text_area("Transcription made intelligible to a 5 year old", text)

st.set_page_config(layout="wide", page_title="ELI5")

st.write("## ELI5 - Powered by OctoAI")

paragraph = st.text_area("Explain like I'm five", value="Nuclear Fusion reactions power the Sun and other stars. In a fusion reaction, two light nuclei merge to form a single heavier nucleus. The process releases energy because the total mass of the resulting single nucleus is less than the mass of the two original nuclei. The leftover mass becomes energy. Einstein’s equation (E=mc2), which says in part that mass and energy can be converted into each other, explains why this process occurs. If scientists develop a way to harness energy from fusion in machines on Earth, it could be an important method of energy production.")

if st.button('ELI5!'):
    eli5(paragraph)
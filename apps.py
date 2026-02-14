# Streamlit app for personalized medication adherence assistant
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from huggingface_hub import login
from dotenv import load_dotenv
import os

# Load environment variables and login to Hugging Face
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if hf_token:
    login(token=hf_token)

st.title("Personalized Medication Adherence Assistant")
st.write("Enter your medication details and get a personalized schedule and advice.")

user_input = st.text_area(
    "Describe your medications, doses, and schedule:",
    "I take 10mg Lisinopril once daily for my hypertension, usually in the morning. I've also just started taking 500mg Metformin twice daily for my type 2 diabetes, with breakfast and dinner. What's a good schedule, and what should I do if I miss a dose of either?",
)

if st.button("Generate Schedule & Advice"):
    model_id = "bubun123/smolified-medimind-personalized-medication-adherence-assistant-for-chronic-disease-management"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

    messages = [
        {
            "role": "system",
            "content": "The user is asking for assistance with medication management for a chronic condition. Generate a personalized medication schedule based on their input, and anticipate common follow-up questions regarding missed doses.",
        },
        {"role": "user", "content": user_input},
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    ).removeprefix("<bos>")

    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    streamer = TextStreamer(tokenizer, skip_prompt=True)
    result = model.generate(
        **inputs,
        max_new_tokens=1000,
        temperature=1,
        top_p=0.95,
        top_k=64,
        streamer=streamer,
    )
    output = tokenizer.decode(result[0], skip_special_tokens=True)
    st.subheader("Personalized Schedule & Advice:")
    st.write(output)

import streamlit as st
from openai import OpenAI

# Groq-compatible client (modern OpenAI Python SDK)
client = OpenAI(
    api_key="YOUR_API_KEY_HERE",  
    base_url="https://api.groq.com/openai/v1"  # Required for Groq
)

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Or: llama3-70b-8192, mixtral-8x7b-32768
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"❌ Groq API Error: {str(e)}")
        return "[ERROR] Could not generate email response."

import streamlit as st
import openai
import os

st.set_page_config(page_title="DevOps Error Analyzer", layout="centered")
st.title("🔍 DevOps Error Analyzer")
st.write("Paste your error logs below and get AI-powered insights.")

openai.api_key = os.getenv("OPENAI_API_KEY")

log_input = st.text_area("Paste your error log here", height=300)

if st.button("Analyze Error"):
    if not openai.api_key:
        st.error("OpenAI API key is not set. Please configure it in the environment.")
    elif not log_input.strip():
        st.warning("Please paste a log before analyzing.")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"""
You are a DevOps engineer.

Analyze this log and answer:
1. Root cause
2. Suggested fix
3. What tool/service is involved
4. Share 2-3 relevant reference links

Log:
{log_input}
"""
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.markdown("### 🧠 Analysis Result")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error calling OpenAI API: {e}")
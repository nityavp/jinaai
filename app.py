import streamlit as st
import requests

# Function to analyze a URL with Jina
def analyze_with_jina(url):
    api_url = f"https://r.jina.ai/{url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Jina Error: {response.status_code}")
        return None

# Streamlit app
st.title("URL Content Analyzer with Jina")

# User inputs
url = st.text_input("Enter the URL to analyze")

if st.button("Analyze URL"):
    if url:
        # Analyze URL with Jina
        result = analyze_with_jina(url)
        if result:
            # Display results as JSON
            st.write("Analysis Results:")
            st.json(result)
    else:
        st.error("Please provide the URL.")

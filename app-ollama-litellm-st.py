import requests
from bs4 import BeautifulSoup
from litellm import completion
import os
import streamlit as st

st.title("Talks list from various DevFests")
def call_llm(query):
    response = completion(
        model="ollama/gemma2:9b",
        messages=[{ "content": query, "role": "user"}],
        api_base=os.environ['OLLAMA_GEMMA2_9B_BASE_URL']
    )

    return response["choices"][0]["message"]["content"]

def llm_function(url, query):
    st.subheader("Talks from : "+ url)
    response_text = call_llm(query)
    st.markdown(response_text)

def read_input():
    urls = [
        "https://gdg.community.dev/events/details/google-gdg-adelaide-presents-gdg-adelaide-devfest-2024/",
        "https://devfest.istanbul/schedule",
        "https://sessionize.com/api/v2/za23h4xc/view/GridSmart",  # devfest London
        "https://devfest.gdgauckland.nz",
        "https://gdg.community.dev/events/details/google-gdg-nyc-presents-devfest-nyc-2024-responsible-ai-for-the-future-of-tech/",
        "https://devfestlagos.com/schedule",
        "https://devfest.gdgparis.fr/agenda", # has titles in French
    ]
    for url in urls:
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.text
        prompt = """ from the provided html please pick out all the talk tiles and speakers, 
               if any of the talk title is not in English language please translate them to English, 
               remove any duplicates if you find any and then render it as a table and do not add anything else"""

        query = data + prompt
        llm_function(url, query)

if __name__ == "__main__":
    read_input()

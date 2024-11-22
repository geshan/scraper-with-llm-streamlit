import requests
from bs4 import BeautifulSoup
from litellm import completion
import os

def call_llm(query):
    response = completion(
        model="ollama/gemma2:9b",
        messages=[{ "content": query, "role": "user"}],
        api_base=os.environ['OLLAMA_GEMMA2_BASE_URL'],
        temprature=0.1
    )

    return response["choices"][0]["message"]["content"]

def llm_function(url, query):
    #st.subheader("Talks from : "+ url)
    response_text = call_llm(query)
    #st.markdown(response.text)
    print(response_text)

def read_input():
    url = "https://gdg.community.dev/events/details/google-gdg-adelaide-presents-gdg-adelaide-devfest-2024/"
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.text
    prompt = """ from the provided html please pick out the talk tiles and speakers, 
           if the talks or names are not in English language please translate them to english, 
           remove any duplicates if you find any and then render it as a table and do not add anything else"""

    query = data + prompt
    llm_function(url, query)

if __name__ == "__main__":
    read_input()

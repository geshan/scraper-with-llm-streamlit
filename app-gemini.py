import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
import google.generativeai as genai

genai.configure(api_key = os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

st.title("Talks list")
def read_input():
   links = [
       "https://gdg.community.dev/events/details/google-gdg-adelaide-presents-gdg-adelaide-devfest-2024/",
       "https://gdg.community.dev/events/details/google-gdg-brisbane-presents-brisbane-devfest-ai-conference-1/",
       "https://gdg.community.dev/events/details/google-gdg-brisbane-presents-devfest-brisbane-android/",
       "https://gdg-sydney-devfest-2024.sessionize.com/api/schedule",
       "https://gdg-melbourne-devfest-2024.sessionize.com/api/schedule",
       "https://gdg.community.dev/events/details/google-gdg-perth-presents-devfest-perth-ai-mobile-cloud-amp-navigating-your-career/",
       "https://gdg.community.dev/events/details/google-gdg-canberra-presents-devfest-canberra-ai-web-cloud-amp-navigating-your-career/",
       "https://gdg.community.dev/events/details/google-gdg-darwin-presents-devfest-darwin/",
       "https://gdg.community.dev/events/details/google-gdg-hobart-presents-gdg-hobart-devfest-2024/",
       "https://devfest.gdgauckland.nz",
       "https://gdg.community.dev/events/details/google-gdg-singapore-presents-devfest-singapore-2024-gemini-conference/",
       "https://gdg.community.dev/events/details/google-gdg-manila-presents-gdg-devfest-manila-2024/",
       "https://gdg.community.dev/events/details/google-gdg-cloud-da-nang-presents-gdg-cloud-da-nang-devfest-2024/",
       "https://gdg.community.dev/events/details/google-gdg-bangalore-presents-devfest-bangalore-2024/",
       "https://devfest.istanbul/schedule",
       "https://sessionize.com/api/v2/za23h4xc/view/GridSmart", #devfest London
       "https://devfest.gdgparis.fr/agenda",
       "https://www.devfesthr.com/agenda",
       "https://sessionize.com/api/v2/kbguy4wm/view/GridSmart", #ireland - Json
       "https://gdg.community.dev/events/details/google-gdg-munich-presents-gdg-munich-devfest-2024/",
       #"https://gdg.community.dev/events/details/google-gdg-sydney-presents-gdg-sydney-devfest-2024/cohost-gdg-sydney" //use dry scape
   ]

   for url in links:
       print(url)
       response = requests.get(url)
       soup = BeautifulSoup(response.text, 'html.parser')
       data = soup.text
       prompt = """ from the provided html please pick out the talk tiles and speakers, 
       if the talks or names are not in English language please translate them to english, 
       remove any duplicates if you find any and then render it as a table"""

       query = data + prompt
       llm_function(url, query)
def llm_function(url, query):
    st.subheader("Talks from : "+ url)
    response = model.generate_content(query)
    st.markdown(response.text)

if __name__ == "__main__":
    read_input()

import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def scrape_page():
    url_to_scrape="https://gdg.community.dev/events/details/google-gdg-bangalore-presents-devfest-bangalore-2024"
    response = requests.get(url_to_scrape)
    if (response.status_code != 200):
        logging.warning("URL did not respond with a 200")
        return
    soup = BeautifulSoup(response.content, "html.parser")
    talks = soup.find_all("tr", class_="agenda-item")
    print(f'Talks from {soup.find("h1").text}\n')
    for talk in talks:
        title = talk.find("td", class_="activity")
        speaker = talk.find("td", class_="description")
        if title.text and speaker.text:
            speaker_name = speaker.text.split("|")[0]
            print(f'* {title.text} by {speaker_name}')

if __name__ == "__main__":
    scrape_page()

import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h3')

        print("\nTop News Headlines:\n")
        for idx, headline in enumerate(headlines[:10], start=1):  
            print(f"{idx}. {headline.get_text()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the news: {e}")

# Example URL of the news website
url = "https://www.bbc.com/news"
scrape_news_headlines(url)

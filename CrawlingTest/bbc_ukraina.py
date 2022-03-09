import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/news/world-60525350")

html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".gs-c-promo-heading")

for title in titles:
    print(title.text.strip())


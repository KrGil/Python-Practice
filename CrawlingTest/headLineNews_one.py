import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/news/world-60525350")

html = response.text

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one(".gs-c-promo-heading")

print(title.text)


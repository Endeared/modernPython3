import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
print(articles)


for article in articles:
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("time")['datetime']
    print(title, url, date)
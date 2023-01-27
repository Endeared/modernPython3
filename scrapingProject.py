import requests
from bs4 import BeautifulSoup
import csv
import random

response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_='quote')
quoteList = []
authorList = []



for div in quotes:
    inner = div.find_all('span')
    quoteList.append(inner[0].text)
    words = (inner[1].text).split(" ")
    removeBreak = words[2].split("\n")
    authorList.append(words[1] + " " + removeBreak[0])

randomIndex = random.randint(0, len(quoteList) - 1)

print(quoteList[randomIndex])
print(authorList[randomIndex])

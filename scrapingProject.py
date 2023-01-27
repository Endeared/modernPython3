import requests
from bs4 import BeautifulSoup
import csv
import random

def get_quote():
    response = requests.get("http://quotes.toscrape.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_='quote')
    count = 4
    correct = False
    playAgain = ''

    objectList = []



    for div in quotes:
        objectList.append({
            "quote": div.find(class_='text').get_text(),
            "author": div.find(class_='author').get_text(),
            'href': div.find('a')['href']
        })

    randomIndex = random.randint(0, len(objectList) - 1)

    while count > 0 and correct == False:
        toGuess = objectList[randomIndex]['author']
        print(objectList[randomIndex]['quote'])
        guess = input(f'Who said this quote? {str(count)} guesses remaining.\n')
        if guess.lower() == toGuess.lower():
            playAgain = input('Correct! Would you like to play again? (y/n)\n')
            while playAgain != 'y' or playAgain != 'n':
                if playAgain == "y":
                    get_quote()
                elif playAgain == "n":
                    print("Thanks for playing!")
                    return
                else:
                    playAgain = input("Invalid input. Try again.\n")
        else:
            print('Incorrect.')
            count -= 1

    playAgain = input('Out of guesses! Would you like to play again? (y/n)\n')
    while playAgain != 'y' or playAgain != 'n':
        if playAgain == "y":
            get_quote()
        elif playAgain == "n":
            print("Thanks for playing!\n")
            return
        else:
            playAgain = input("Invalid input. Try again.\n")
        


get_quote()
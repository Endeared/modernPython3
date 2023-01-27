import requests
from bs4 import BeautifulSoup
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
        href = objectList[randomIndex]['href']
        nameList = toGuess.split(" ")
        if count == 4:
            print(objectList[randomIndex]['quote'])
            guess = input(f'Who said this quote? {str(count)} guesses remaining.\n')
        else:
            guess = input(f'{str(count)} guesses remaining.\n')
        if guess.lower() == toGuess.lower():
            playAgain = input('Correct! Would you like to play again? (y/n)\n')
            while playAgain != 'y' or playAgain != 'n':
                if playAgain == "y":
                    get_quote()
                elif playAgain == "n":
                    print("Thanks for playing!")
                    count = 0
                    correct = True
                    quit()
                else:
                    playAgain = input("Invalid input. Try again.\n")
        else:
            count -= 1
            if count == 3:
                responseBio = requests.get(f'http://quotes.toscrape.com{href}')
                soupBio = BeautifulSoup(responseBio.text, 'html.parser')
                born = soupBio.find('span', class_='author-born-date').get_text()
                location = soupBio.find('span', class_='author-born-location').get_text()
                print(f'Incorrect! This person was born {born} {location}.')
            elif count == 2:
                print(f'Incorrect! First letter of first name is {nameList[0][0]}.')
            elif count == 1:
                print(f'Incorrect! First letter of last name is {nameList[len(nameList) - 1][0]}.')

    playAgain = input('Out of guesses! Would you like to play again? (y/n)\n')
    while playAgain != 'y' or playAgain != 'n':
        if playAgain == "y":
            get_quote()
        elif playAgain == "n":
            print("Thanks for playing!")
            count = 0
            correct = True
            quit()
        else:
            playAgain = input("Invalid input. Try again.\n")
        
get_quote()
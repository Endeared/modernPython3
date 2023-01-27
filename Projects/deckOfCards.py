from pprintpp import pprint
import random

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:

    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            j = i
            if j == 1:
                j = "A"
            elif j == 11:
                j = "J"
            elif j == 12:
                j = "Q"
            elif j == 13:
                j = "K"
            self.cards.append(Card("Hearts", str(j)))
            self.cards.append(Card("Clubs", str(j)))
            self.cards.append(Card("Diamonds", str(j)))
            self.cards.append(Card("Spades", str(j)))
        self.num = len(self.cards)
        

    def count(self):
        return self.num

    def __repr__(self):
        return(f'Deck of {self.num} cards')

    def _deal(self, toDeal):
        i = 0
        hand = []

        while i <= toDeal and self.num > 0:
            hand.append(self.cards.pop())
            i += 1
            self.num -= 1

        if self.num == 0:
            raise ValueError("All cards have been dealt.")
        else:
            return hand

    def shuffle(self):
        if self.num < 52:
            raise ValueError("Only full decks can be shuffled.")
        else:
            random.shuffle(self.cards)

    def deal_card(self):
        if self.num > 0:
            randomCard = random.choice(self.cards)
            self.cards.remove(randomCard)
            self.num -= 1
            return(randomCard)
    
    def deal_hand(self, cardNum):
        return(self._deal(cardNum))
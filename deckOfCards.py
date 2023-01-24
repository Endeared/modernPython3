from pprintpp import pprint

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return(f'{self.value} of {self.suit}')


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

    def deal(self, toDeal):
        i = 0
        while i <= toDeal and self.num > 0:
            self.cards.pop()
            i += 1
            self.num -= 1
        if self.num == 0:
            raise ValueError("All cards have been dealt.")
    

cards = Deck()

pprint(cards.cards)
cards.deal(54)
pprint(cards.cards)
pprint(cards.num)
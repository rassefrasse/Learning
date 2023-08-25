import random

class Card:


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.rank, self.suit))


class Dealer:


    def __init__(self):
        pass


class Deck:

    def __init__(self):
        self.deck = []

    def build(self):
        for s in ("Hearts", "Spades", "Clubs", "Diamonds"):
            for r in range(2, 12):
                self.deck.append(Card(r, s))

    def show(self):
        for card in self.deck:
            card.show()
        

class Game:
    def __init__(self):
        pass

    def rules(self):
        pass

cards = Deck()
cards.build()
cards.show()

import random #Will be using soon

class Card:


    def __init__(self, rank, suit): #defining the rank and the suit of the cards
        self.rank = rank
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.rank, self.suit)) #prints the card i.e. "2 of Spades"


class Dealer:


    def __init__(self):
        pass


class Deck:

    def __init__(self): 
        self.deck = [] #The deck where the cards are stored

    def build(self):
        for s in ("Hearts", "Spades", "Clubs", "Diamonds"): #The method that builds the deck by running suit and rank in a f loop
            for r in range(2, 12):
                self.deck.append(Card(r, s)) #Sends the value of the cards to the deck above

    def show(self):
        for card in self.deck: #Method to show the card
            card.show()
        

class Game:
    def __init__(self): #WIP
        pass

    def rules(self):
        pass

cards = Deck()
cards.build() #Run the creation of the cards>>
cards.show() #Just displaying the cards

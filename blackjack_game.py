import random

class Hand:

    hand_c = []


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Dealer:
    two_c = 2
    three_c = 3
    four_c = 4
    five_c = 5
    six_c = 6
    seven_c = 7
    eight_c = 8 
    nine_c = 9 
    face_c = 10
    ace_c = 11

    def __init__(self, ):
        pass


class Deck:

    deck_c = []

    def __init__(self, card_deck, draw_card):
        self.card_deck = card_deck
        self.draw_card = draw_card

    def deck():
        pass

    def draw(self, draw_card):
        pass
        

class Game:
    def __init__(self):
        pass

    def rules(self):
        pass



hit_or_stand = input("H/S: ")

if hit_or_stand == "H":
  #  Deck.deck_c.pop(random.randrange)
    pass
elif hit_or_stand == "S":
    pass
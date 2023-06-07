# Erin Blackjack
# A game of blackjack against the computer
# 07/06/2023

# Create a card object
class Card():
    """ A playing card object """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]
    NUMBER_VALUE = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                    "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = f"{self.rank}:{self.suit}"
        return rep

    # def return_card_value(self):
    #     """ Get the value of the playing card """
    #     value = Card.RANKS.index(self.rank) + 1
    #     if value > 10:
    #         value = 10

    #     return value
    def return_card_value(self):
        value = Card.NUMBER_VALUE[self.rank]
        return value


card1 = Card(Card.RANKS[1], Card.SUITS[3])
print(card1)
print(card1.return_card_value())

card2 = Card(Card.RANKS[0], Card.SUITS[0])
print(card2)
print(card2.return_card_value())

card3 = Card(Card.RANKS[4], Card.SUITS[2])
print(card3)
print(card3.return_card_value())

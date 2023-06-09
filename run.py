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
    ACE_VALUE = 11

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
        try:
            value = Card.NUMBER_VALUE[self.rank]
            return value
        except:
            print("<Value not in cards>")


# card1 = Card(Card.RANKS[1], Card.SUITS[3])
# print(card1)
# print(card1.return_card_value())

# card2 = Card(Card.RANKS[0], Card.SUITS[0])
# print(card2)
# print(card2.return_card_value())

# card3 = Card(Card.RANKS[4], Card.SUITS[2])
# print(card3)
# print(card3.return_card_value())
class Hand():
    """
    A hand of playing cards
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += f"{str(card)} \t"
        else:
            rep = "<EMPTY>"
        return rep

    def clear(self):
        """
        Emptying every hand and deck when initially called
        """
        self.cards = []

    def add(self, card):
        """
        Give card to hand when game begins
        """
        self.cards.append(card)

    def give(self, card, other_hand):
        """
        Give cards to both players
        """
        self.cards.remove(card)
        other_hand.add(card)

    def hand_total(self):
        """
        Return the total value of cards in the hand
        """
        total = 0
        for card in self.cards:
            total += card.return_card_value()

        # Determine if there is an ACE in the hand of cards
        contains_ace = False
        for card in self.cards:
            if card.return_card_value() == Card.ACE_VALUE:
                contains_ace = True

        # If the hand contains an ace and the total goes over 21 treat the ace card as a 1
        if contains_ace and total > 21:
            total -= 10

        # return the total
        return total


class Deck(Hand):
    """
    This class creates a full deck of playing cards
    """

    def create_deck(self):
        """
        Loop through the suits and ranks, create cards and add them to the deck
        """
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """
        Use the random module and built in shuffle method to shuffle the deck
        """
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        """
        Deal cards
        """
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't deal anymore. Out of cards")


# card1 = Card(Card.RANKS[1], Card.SUITS[1])
# print(card1)
# value1 = card1.return_card_value()
# print(value1)
# card2 = Card(Card.RANKS[2], Card.SUITS[0])
# print(card2)
# value2 = card2.return_card_value()
# print(value2)

# my_hand = Hand()
# my_hand.add(card1)
# my_hand.add(card2)
# print(my_hand)
# hand_value = my_hand.hand_total()
# print(hand_value)

# deck = Deck()
# deck.create_deck()
# print(deck)
# deck.shuffle()
# print(deck)

def compare_score(score1, score2):
    """ Compare the score value of each hand and determine a winner """
    if score1 == score2:
        return "It's a draw!"
    elif score2 == 21:
        return "Computer wins! Blackjack!!!"
    elif score1 == 21:
        return "Player wins! Blackjack!!!"
    elif score1 > 21:
        return "Player went bust! Player loses! Computer Wins!!!"
    elif score2 > 21:
        return "Computer went bust! Computer loses! Player Wins!!!"
    elif score1 > score2:
        return "Player closest to 21. Player wins!!!"
    else:
        return "Computer closest to 21. Computer Wins!!!"


def ask_yes_no(question):
    """ A function that only allows the user to answer 'y' or 'n' """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def play_game():
    """ A Function that allows the user to play a game of Blackjack against the computer """
    # Create a deck of cards for the game + shuffle them
    blackjack_deck = Deck()
    blackjack_deck.create_deck()
    blackjack_deck.shuffle()

    # Flag to end the game
    is_game_over = False

    # Create Player hand + computer hand for the game
    player_hand = Hand()
    computer_hand = Hand()

    players = []
    players.append(player_hand)
    players.append(computer_hand)

    # Deal cards to the player + the computer
    blackjack_deck.deal(players, 2)

    # YOU CAN DELETE THE BELOW CODE

    # print(player_hand)
    # print(computer_hand)

    # get player + computer hand totals
    # user_score = player_hand.hand_total()
    # computer_score = computer_hand.hand_total()

    # print(user_score)
    # print(computer_score)

    # if user_score > 21:
    #     is_game_over = True
    # else:
    #     # user_hit = input("Type 'y' to hit or 'n' to stand: ").lower()
    #     user_hit = ask_yes_no("Type 'y' to hit or 'n' to stand: ")
    #     if user_hit == 'y':
    #         blackjack_deck.deal([player_hand])
    #     else:
    #         is_game_over = True

    # print(player_hand)
    # user_score = player_hand.hand_total()
    # print(user_score)

    # Test computer hand
    # blackjack_deck.deal([computer_hand])
    # computer_score = computer_hand.hand_total()
    # print(computer_hand)
    # print(computer_score)

    # DO NOT DELETE PAST HERE

    while not is_game_over:
        user_score = player_hand.hand_total()
        computer_score = computer_hand.hand_total()

        print(player_hand)
        print(user_score)

        print(computer_hand)
        print(computer_score)

        if user_score > 21:
            is_game_over = True
        else:
            # user_hit = input("Type 'y' to hit or 'n' to stand: ").lower()
            user_hit = ask_yes_no("Type 'y' to hit or 'n' to stand: ")
            if user_hit == 'y':
                blackjack_deck.deal([player_hand])
            else:
                is_game_over = True

    while computer_score < 17:
        blackjack_deck.deal([computer_hand])
        computer_score = computer_hand.hand_total()

    print(f"Player Cards: {player_hand}")
    print(f"Player Hand total: {user_score}")
    print(f"Computer Cards: {computer_hand}")
    print(f"Computer Hand total: {computer_score}")

    result = compare_score(user_score, computer_score)
    print(result)

    # Clear the hands + deck for the next round
    blackjack_deck.clear()
    player_hand.clear()
    computer_hand.clear()


def display_menu():
    # Create user Menu allowing the user to interact with the game
    choice = None
    while choice != "0":
        print("Press 1 to view the rules.")
        print("Press 2 to play the game.")
        print("Press 0 to quit the game.")
        choice = input("Make a choice: ")

        if choice == "0":
            print("thanks for playing.")
        elif choice == "1":
            print("Rules")
        elif choice == "2":
            play_again = True
            play_game()
            while play_again:
                play = input(
                    "Would you like to play again 'y' or 'n': ").lower()
                if play == 'y':
                    play_game()
                else:
                    play_again = False
        else:
            print("sorry that is not a valid choice.")


display_menu()

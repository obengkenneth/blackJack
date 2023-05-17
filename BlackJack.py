# importing necessary functions
from random import randint

# create blackjack class
class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ("Spades", "Hearts", "Diamonds", "Clubs")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

# a method that creates a deck of 52 cards, each card being a tuple of a value and suit
    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    # take in a tuple and append it to the hand
    def addCard(self, card):
        self.hand.append(card)

    # if not dealer's turn then only show one of his cards, otherwise show all
    def showHand(self, dealer_start = True):
        print(f"\n{self.name}")
        print("=" * 7)
        for i in range(len(self.hand)):
            if self.name == "Dealer" and i == 0 and dealer_start:
                print(" - of -")
            else:
                card = self.hand[i]
                print(f"{card[0]} of {card[1]}")
                
# instantiate game, dealer and player
game = Blackjack()
game.makeDeck()
dealer = Player("Dealer")
name = input("What is your name? ")
player = Player(name)

# add two cards to the dealer and player hand
for i in range(2):
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())

# show both hands using method
player.showHand()
dealer.showHand()
# Python code to play Blackjack
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value()
        
    def assign_value(self):
        if self.rank == 'A':
            return 11
        elif self.rank in ['K', 'Q', 'J']:
            return 10
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()
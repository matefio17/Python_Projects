# BLACKJACK

import random





class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank}{self.suit}"
        
class Deck:
    def __init__(self):
        self.suits = ['♥', '♦', '♣', '♠']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def generate_deck(self):
        self.cards = []
        
        for rank in self.ranks:
            for suit in self.suits:
                self.cards.append(Card(rank, suit))
                
        return self.cards
        
       
deck = Deck()
deck.generate_deck()

for card in deck.cards:
    print(card, end=" ")                
                        
                                        


         
        



        

        
        
        
        





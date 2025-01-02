import random

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_values = {"A" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10}

def generateDeck():
    deck = [ ]
    for suit in suits:
        for card in cards: 
            deck.append((card,suit))
    random.shuffle(deck)
    return deck

def getCardValues(card):
    key = card[0]
    value = card_values[key]
    return value
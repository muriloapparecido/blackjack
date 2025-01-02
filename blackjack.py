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

def turn(deck, current_score):
    card = deck.pop(0)
    print(">> ", card)
    current_score += getCardValues(card)
    print("Score: ", current_score)
    return current_score

def playGame():
    deck = generateDeck()
    dealerScore = 0
    playerScore = 0

    print("-------------------------Dealers Hand-------------------------")
    dealerScore = turn(deck, dealerScore)
    dealerScore = turn(deck, dealerScore)
    print("Dealers score: ", dealerScore)

    print("-------------------------Players Hand-------------------------")
    playerScore = turn(deck, playerScore)
    playerScore = turn(deck, playerScore)
    print("Your score: ", playerScore)

    print("-------------------------Begin Game-------------------------")
    while True: 
        userChoice = input("HIT or STAND: ").strip().upper()
        if (userChoice == "HIT"):
            playerScore = turn(deck, playerScore)
            print("Your total: ", playerScore)
            print("Dealer total: ", dealerScore)
            if (playerScore > 21): 
                print("-------------------------You bust, dealer wins!-------------------------")
                return
        elif (userChoice == "STAND"):
            print("-------------------------Dealers Hand-------------------------")
            dealerScore = turn(deck, dealerScore)
            print("Your Total: ", playerScore)
            print("Dealer Total: ", dealerScore)
            if(dealerScore > 21):
                print("-------------------------Dealer busts, you win!-------------------------")
                return
            elif (dealerScore == playerScore):
                 print("-------------------------Tie!-------------------------")
                 return
            elif (dealerScore > playerScore):
                print("-------------------------You lose, dealer wins!-------------------------")
                return
            else:
                print("-------------------------Dealer loses, you wins!-------------------------")
                return
        else: 
            print("Please enter a valid input: 'HIT' or 'STAND'")

playGame()
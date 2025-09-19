class Card:
    def __init__(self, suit, value, intValue):
        self.suit = suit
        self.value = value
        self.intValue = intValue

def printCardArray(cards):
    for car in cards:
        print(car.suit + car.value + "(" + car.intValue + ")")

cards = []
cards.append(Card("♣", "A", "1"))
cards.append(Card("♦", "K", "13"))
cards.append(Card("♥", "Q", "12"))
cards.append(Card("♠", "J", "11"))

printCardArray(cards)


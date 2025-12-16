class Card:
    def __init__(self, suit, value, intValue):
        self.suit = suit
        self.value = value
        self.intValue = intValue
    
    # __str__はPythonが内部的に呼ぶ
    def __str__(self):
        return f"{self.suit}{self.value}({self.intValue})"

# リスト作成:4枚のカードインスタンスを作ってリストにまとめている
cards = [
    Card("♣", "A", 1),
    Card("♦", "K", 13),
    Card("♥", "Q", 12),
    Card("♠", "J", 11)
]

for card in cards:
    print(card)
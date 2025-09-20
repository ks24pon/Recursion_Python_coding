class Card:
    def __init__(self, suit, value, intValue):
        self.suit = suit
        self.value = value
        self.intValue = intValue

    # 文字列、定義
    def __str__(self):
        return f"{self.suit}{self.value}({self.intValue})"

# カードのリスト作成
cards = [
    Card("♣", "A", 1),
    Card("♦", "K", 13),
    Card("♥", "Q", 12),
    Card("♠", "J", 11)
]

# 作成カードを1枚ずつ出力
for card in cards:
    print(card)
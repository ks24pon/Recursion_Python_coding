def winnerBlackjack(playerCards,houseCards):
    numArr = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # 合計点を計算(内包表記+sum)
    def score(cards, values):
        return sum(values.index(card[1:]) + 1 for card in cards)

    # スコア計算
    playerScore = score(playerCards, numArr)
    houseScore = score(houseCards, numArr)

    return not (playerScore > 21 or (houseScore < 22 and houseScore >= playerScore))
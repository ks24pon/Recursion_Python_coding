def winnerBlackjack(playerCards,houseCards):
    numArr = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # 手札のカード配列から合計値を計算
    def score(cards, values):
        total = 0
        for card in cards:
            # 1文字目以降を取り出す
            val = card[1:]
            # インデックス　+ 1が得点
            total += values .index(val) + 1
        return total

    # プレイヤーとディーラーのスコアを計算
    playerScore = score(playerCards, numArr)
    houseScore = score(houseCards, numArr)

    # 勝利判定ルール
    if playerScore > 21:
        return False
    elif houseScore < 22 and houseScore >= playerScore:
        return False
    else:
        return True


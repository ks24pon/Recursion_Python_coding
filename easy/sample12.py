def whoIsWinner(hisCard):
    # 引き分けの場合draw
    if hisCard == 10:
        return "draw"
    # 負けた場合、you lose
    elif hisCard == 1 or hisCard == 2 or hisCard == 11 or hisCard == 12 or hisCard == 13:
        return "you lose"
    elif 10 > hisCard:
        return "you win"
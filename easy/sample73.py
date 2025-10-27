def whoIsWinner(hisCard):
    # 大富豪[2,1,13,12,11,10,9,8,7,6,5,4,3]
    if hisCard == 10:
        return "draw"
    elif hisCard == 2 or hisCard == 1:
        return "you lose"
    elif hisCard >= 10:
        return "you lose"
    elif hisCard <= 10:
        return "you win"

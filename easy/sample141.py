def whoIsWinner(hisCard):
    if hisCard == 10: return "draw"
    elif hisCard == 2 or hisCard == 1: return  "you lose"
    elif hisCard <= 10: return "you win"
    return "you lose"
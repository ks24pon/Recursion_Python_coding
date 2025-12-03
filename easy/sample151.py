import math

def vacationRental(people,day):
    # 清掃費：12%加算
    CLEAN = 1.12
    # 宿泊値段の初期値
    perDay = 0
    # 全体の金額に8%の税金加算
    TAX = 1.08

    # 宿泊期間によって変動
    if day <= 3:
        perDay = 80
    elif day >= 10: 
        perDay = 50
    else:
        perDay = 60

    return math.floor(perDay * people * day * CLEAN * TAX)

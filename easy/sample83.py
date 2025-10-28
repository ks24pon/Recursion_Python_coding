import math

def vacationRental(people,day):
    if day >= 10:
        perDay = 50
    elif day >= 4:
        perDay = 60
    else:
        perDay = 80

    # 1泊の宿泊料金
    stay = people * day * perDay
    # 清掃費
    clean = stay * 1.12
    # 全体の金額
    total = clean * 1.08
    totalScore = math.floor(total)
    return totalScore

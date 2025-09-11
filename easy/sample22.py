import math

def vacationRental(people,day):
    # 1泊の料金
    if day <= 3:
        rate = 80
    elif day >= 10:
        rate = 50
    elif day >= 4:
        rate = 60
    # 宿泊料金
    hotel = rate * people * day

    # 清掃費(12%加算)
    clean = hotel * 1.12

    # 税金(8%加算)
    total = clean * 1.08

    # 切り捨てて返す
    return math.floor(total)

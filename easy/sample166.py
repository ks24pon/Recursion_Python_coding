def infectedPeople(day):
    # ベースケース：0以下なら1を返す
    if day <= 0:
        return 1

    return 2 * infectedPeople(day-1)
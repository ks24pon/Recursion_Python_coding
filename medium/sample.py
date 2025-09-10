def getCentury(year):
    # 年から世紀を求める(例：2001 → 21世紀)
    # 99を足して100で割ると、切り上げのような処理
    century = (year + 99) // 100

    if 11 <= century % 100 <= 13:
        suffix = "th"
    else:
        # 世紀の末尾1桁を取り出す
        last_digit = century % 10

        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    # 文字列返す
    return f"{century}{suffix} century"
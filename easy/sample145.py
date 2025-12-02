def isThereSchool(day, isHoliday):
    # 祝日または土日の場合、学校なし
    if day == "Saturday" or day == "Sunday" or isHoliday:
        return False
    return True

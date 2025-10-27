def isThereSchool(day,isHoliday):
    # 祝日ならTrue,そうでないならFalse
    if day == "Saturday" or day == "Sunday" or isHoliday:
        return False
    else: return True
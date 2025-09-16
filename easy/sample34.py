def infectedPeople(day):
    if day == 0:
        return 1
    return infectedPeople(day-1) * 2
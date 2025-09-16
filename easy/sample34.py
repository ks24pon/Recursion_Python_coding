def infectedPeople(day):
    if day == 0:
        return 1
    return 2*infectedPeople(day-1)
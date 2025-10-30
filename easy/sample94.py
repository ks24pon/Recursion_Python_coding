import math
def infectedPeople(day):
    virus = math.pow(2,day)
    return math.floor(virus)
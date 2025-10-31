def maximumPeople(x,y):
    if y == 0:
        return x
    return maximumPeople(y,x % y)
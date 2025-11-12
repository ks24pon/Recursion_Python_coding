def addEveryOtherElement(intArr):
    elementList = []

    for index, value in enumerate(intArr):
        if index % 2 == 0:
            elementList.append(value)
    return sum(elementList)
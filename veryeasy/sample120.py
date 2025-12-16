def minAndMax(intArr):
    minNum = maxNum = intArr[0]
    total = 0

    for x in intArr:
        total += x
        if x < minNum:
            minNum = x
        if x > maxNum:
            maxNum = x
    return [total - maxNum, total - minNum]

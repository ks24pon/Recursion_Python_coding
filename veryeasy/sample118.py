def evenRange(a, b):
    evenList = []
    for i in range(a, b+1):
        if i % 2 == 0:
            evenList.append(i)
    return evenList
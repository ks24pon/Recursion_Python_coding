def quadraticEquation(a, b, c):
    discriminat = b ** 2 - 4 * a * c

    if a == 0:
        return 0
    elif discriminat == 0:
        return 1
    elif discriminat > 0:
        return 2
    else:
        return -2

def quadraticEquation(a, b, c):
    d = b ** 2 - 4 * a * c

    if a == 0:
        return 0
    elif d == 0:
        return 1
    elif d > 0:
        return 2
    else:
        return -2

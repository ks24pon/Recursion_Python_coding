def getGCD(x, y):
    x, y = abs(x), abs(y)
    if y == 0:
        return x
    return getGCD(y, x % y)


def irreducibleFraction(x, y):
    gcd = getGCD(x, y)
    numerator = int(x / gcd)
    denominator = int(y / gcd)

    # 分母が1なら整数で返す
    if denominator == 1:
        return str(numerator)

    if denominator < 0:
        numerator *= -1
        denominator *= -1

    return f"{numerator}/{denominator}"

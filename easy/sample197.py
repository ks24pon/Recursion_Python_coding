import math

# 素数判定
def isPrime(num):
    # 素数は2以上の整数
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 素数の総和関数
def sumOfAllPrimes(n):
    return sum(i for i in range(2, n + 1) if isPrime(i))

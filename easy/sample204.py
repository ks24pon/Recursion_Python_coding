def primeArray(n):
    primeList = []
    for i in range(2,n+1):
        if isPrime(i):
            primeList.append(i)
    return primeList


def isPrime(number):
    for d in range(2, number):
        if number % d == 0:
            return False
    return number > 1
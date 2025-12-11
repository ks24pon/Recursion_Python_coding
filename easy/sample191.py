def isPrime(number):
    # 1は素数ではない
    if number == 1:
        return False
    # 2は素数
    elif number == 2:
        return True
    # 2からnumber1までの数を割り切れるか調べる
    for i in range(2, number):
        # 割り切れたら素数ではないFalse
        if number % i == 0:
            return False
    # どちらでも割り切れなければTrue
    return True
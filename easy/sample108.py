def countDivisibleByK(n,k):
    # ベースケース
    if n % k != 0: return 0
    else: return 1 + countDivisibleByK(n//k,k)
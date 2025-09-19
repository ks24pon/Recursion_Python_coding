def countCharactersAfterN(arr):
    return sum(1 for s in arr for ch in s if ord(ch) >= ord("n"))
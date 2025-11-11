def countAllChars(arr):
    count = 0
    for s in arr:
        for char in s:
            count += 1
    return count

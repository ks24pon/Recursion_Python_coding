def sumOfOddElement(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            count += arr[i]
    return count
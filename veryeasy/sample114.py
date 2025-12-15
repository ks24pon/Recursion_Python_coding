# 奇数チェック
def is0dd(arr):
    return arr % 2 != 0

def sumOfOddElement(arr):
    # 奇数の合計値
    count = 0
    # 配列要素を1つずつ取り出す
    for i in arr:
        if is0dd(i):
            # 要素が奇数なら合計に足す
            count += i
    return count
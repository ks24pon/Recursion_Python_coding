# 奇数チェック
def isOdd(arr):
  return arr % 2 != 0

def sumOfOddElement(arr):
  # 初期値
  count = 0

  for i in arr:
    if isOdd(i):
      count += i
  return count
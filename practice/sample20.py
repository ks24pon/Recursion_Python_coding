def isEven(n):
  return n % 2 == 0

# 偶数が何個あるかチェック
def countEven(listOfInts):
  # 初期値
  count = 0

  for i in range(len(listOfInts)):
    if isEven(listOfInts[i]):
        count += 1
  return count

list1 = [3,43,5,4,2,100,6]
print(countEven(list1))

def fizzBuzz(x):
  fizzBuzzList = []
  for i in range(1,x):
    if i % 3 == 0 and i % 5 == 0:
      fizzBuzzList.append("fizzBuzz")
    elif i % 3 == 0:
      fizzBuzzList.append("fizz")
    elif i % 5 == 0:
      fizzBuzzList.append("buzz")
    else:
      fizzBuzzList.append("-" + str(i) + "-")
  return fizzBuzzList

# 1つずつ表示
def printList(arr):
  for i in range(len(arr)):
    print(arr[i])

# 出力
printList(fizzBuzz(45))
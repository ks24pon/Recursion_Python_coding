def printArray(arr):
  for value in arr:
    # end = " "は改行なしで同じ行に出力
    print(value, end = " ")
  print()

doubleArr = [34,5,34,4,23,54,3]
charArr = ['h','e','l','l','o']
stringArr = ["The race is starting.", "A dog just escaped", "The company ran out of business"]

printArray(doubleArr)
printArray(charArr)
printArray(stringArr)
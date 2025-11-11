def printArray(intArr):
  for value in intArr:
    print(value, end ="")
  print()

# 初期配列を2つの項目に設定
dArr = [2,3]
printArray(dArr)

# 配列の末尾に要素を追加
dArr.append(30)
dArr.append(645)
dArr.append(23)
dArr.append(-35)
dArr.append(325)
dArr.append(1425)
dArr.append(0)
dArr.append(98)

printArray(dArr)

# 配列の値を複数追加
dArr.extend([3,34,3542,10,202,34,203,-75,-56,45,0,43,1132])
printArray(dArr)
def cubeRange(a, b):
  cubeList = []
  # 3~10までループ
  for i in range(a, b + 1):
    # iの3乗をリストに追加
    cubeList.append(i ** 3)
  return cubeList

def printList(arr):
  # 配列の長さを取得
  for i in range(len(arr)):
    # iの回数分だけループ
    print(arr[i])
printList(cubeRange(3,10))
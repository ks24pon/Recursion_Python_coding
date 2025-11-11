def cubeRange(a, b):
  cubeList = []
  for i in range(a, b + 1):
    cubeList.append(i ** 3)
  return cubeList

def printList(arr):
  for i in range(len(arr)):
    print(arr[i])

printList(cubeRange(3,10))
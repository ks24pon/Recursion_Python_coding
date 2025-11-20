class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class SingLinkedList:
  # 配列を受け取り、連結リストを作成
  def __init__(self, arr):
    # 先頭を初期化
    self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

    currentNode = self.head;
    for i in range(1,len(arr)):
      currentNode.next = Node(arr[i])
      currentNode = currentNode.next
  
  def at(self, index):
    iterator = self.head;
    for i in range(0, index):
      iterator = iterator.next
      if iterator == None: return None
    
    return iterator
  
  def printList(self):
    iterator = self.head;
    while iterator is not None:
      print(iterator.data, end =" ")
      iterator = iterator.next
    print()


numList = SingLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
numList.printList()
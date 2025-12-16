class Item:
    def __init__(self,data):
        # 実際のデータ
        self.data = data
        # 次のノード
        self.next = None

class SinglyLinkedList:
    def __init__(self,node):
        self.head = node

# ノードを3つ作成
item1 = Item(7)
item2 = Item(99)
item3 = Item(45)

# リストを作成
numList = SinglyLinkedList(item1)

# ノードを繋ぐ
numList.head.next = item2
numList.head.next.next = item3

# リストを順番に読む
currentNode = numList.head

while currentNode is not None:
    print(currentNode.data)
    currentNode = currentNode.next
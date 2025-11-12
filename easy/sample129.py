class Item:
    def __init__(self,data):
        # 実際のデータ
        self.data = data
        # 次のノード
        self.next = None

class SinglyLinkedList:
    def __init__(self, node):
        self.head = node

# ノードを作成
item1 = Item(7)
item2 = Item(99)
item3 = Item(45)

# 新しいリストを作成、item1指定
numList = SinglyLinkedList(item1)

numList.head.next = item2
numList.head.next.next = item3

currentNode = numList.head
while currentNode is not None:
    print(currentNode.data)
    # 次のNodeに更新
    currentNode = currentNode.next

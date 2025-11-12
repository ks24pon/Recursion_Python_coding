class Node:
    def __init__(self, data):
        self.data = data
        # 次のノード
        self.next = None


class SinglyLinkedList:
    def __init__(self, node):
        # リストの先頭
        self.head = node
arr = [35,23,546,67,86,234,56,767,34,1,98,78,555]
numList = SinglyLinkedList(Node(arr[0]))
# ノード作成後、リストの先頭35
currentNode = numList.head;
for i in range(1,len(arr)):
    # 次のノードに繋ぐ
    currentNode.next = Node(arr[i])
    # .nextで次のノード
    currentNode = currentNode.next

currentNode = numList.head
while currentNode is not None:
    print(currentNode.data)
    currentNode = currentNode.next
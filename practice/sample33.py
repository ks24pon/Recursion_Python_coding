class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, arr):
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        # リストの初めのノードを作成
        self.head = Node(arr[0])
        currentNode = self.head

        # 残りの要素に前のノードとリンク
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            # 次のノードのprevフィールドを現在のノードにリンクさせる
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        # 末尾のノードを追跡します
        self.tail = currentNode

        # リストの内容を表示するメソッド
        def printList(self):
            iterator = self.head
            while (iterator != None):
                print(iterator.data, end=" ")
                iterator = iterator.next
            print()


numList = DoublyLinkedList(
    [35, 23, 546, 67, 86, 234, 56, 767, 34, 1, 98, 78, 555])

# リストの内容を表示
numList.printList()

# リストの先頭とその次のノードのデータを表示します。
print(numList.head.data)
print(numList.head.next.data)

# リストの末尾とその前のノードのデータ表示
print(numList.tail.data)
print(numList.tail.prev.data)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    # リストは配列を受け取り、その要素を使ってリストを初期化します。
    def __init__(self,arr):
        # リストの先頭のノードを作成。配列が空なら、Noneを含むノードを作成。
        self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

        # 各配列の要素に対してノードを作成し、それを現在のノードのnext属性としてリンクします。
        currentNode = self.head
        for i in range(1,len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next
        
    # 指定したインデックスのノードを返すメソッド
    def at(self, index):
        iterator = self.head
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        # インデックスで指定されたノードを返却
        return iterator


# 配列を使って新しい片方向リストを作成
numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
# atメソッドを使用して、指定されたインデックスのノードのデータを出力
print(numList.at(0).data) # 配列の最初の要素を表示

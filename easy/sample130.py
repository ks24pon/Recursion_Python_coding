class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLinkedList(arr):
    # 最初のノードを作成
    head = SinglyLinkedListNode(arr[0])
    # 作業中のポインター
    current = head
    # 2番以降の要素を繋ぐ
    for i in range(1, len(arr)):
        # 新しいノードを作成
        current.next = SinglyLinkedListNode(arr[i])
        current = current.next
    # リスト入口
    return head

# 出力
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end="-")
        current = current.next
    print("END")
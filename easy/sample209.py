class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedListに変換
def getLinkedList(arr):
    # 配列の先頭要素でノード作成
    head = SinglyLinkedListNode(arr[0])
    # 作業用ポインタ用意
    current = head
    # すでにarr[0]は使っているため1から
    for i in range(1, len(arr)):
        # 現在のノードにnext接続
        current.next = SinglyLinkedListNode(arr[i])
        current = current.next
    return head

# LinkeListを出力
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end="-")
        current = current.next
    print("END")




class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def getIndexValue(head, index):
    current = head
    pos = 1
    while current is not None:
        if pos == index:
            return current.data
        current = current.next
        pos += 1
    return None  # 範囲外

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def doubleEvenNumber(head):
    # 空リストの場合
    if head is None:
        return None
    
    index = 0
    current = head
    
    while current is not None:
        # 偶数番目のとき
        if index % 2 == 0:
            newNode = SinglyLinkedListNode(current.data * 2)
            newNode.next = current.next
            current.next = newNode
            # 新しく挿入したノードをスキップして進む
            current = newNode.next
        else:
            current = current.next
        index += 1
    
    return head

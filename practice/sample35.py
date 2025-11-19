# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class


class Queue:
    def __init__(self):
        # キュー先頭
        self.head = None
        # キュー末尾
        self.tail = None

    # キュー先頭を参照(キューが空の場合はNoneを返す)
    def peekFront(self):
        if self.head is None:
            return None
        return self.head.data

    # キューの末尾を参照(キューが空の場合は先頭を参照)
    def peekBack(self):
        if self.tail is None:
            return self.peekFront()
        return self.tail.data

    # 末尾に追加
    def enqueue(self, data):
        # キューの末尾に追加
        if self.head is None:
            # キュー空の場合ノードを作成し、先頭と末尾に設定
            self.head = Node(data)
            self.tail = self.head
        else:
            # ノードを末尾に追加
            self.tail.next = Node(data)
            self.tail = self.tail.next

    # 先頭のデータ取り出し
    def dequeue(self):
        # キューの先頭のデータを取り出し(空の場合はNoneを返す)
        if self.head is None:
            return None

        # 先頭のノードを一時的に保存
        temp = self.head
        # 先頭を次のノードに移す
        self.head = self.head.next
        # もしキューが空になった場合は末尾もNone設定
        if self.head is None:
            self.tail = None

        # 先頭から取り出したデータを返します
        return temp.data


# キュー作成
q = Queue()
# キューの先頭と末尾を表示
print(q.peekFront())
print(q.peekBack())

# 以下キューの先頭と末尾を追加
q.enqueue(4)
print(q.peekFront())
print(q.peekBack())

q.enqueue(50)
print(q.peekFront())
print(q.peekBack())

q.enqueue(64)
print(q.peekFront())
print(q.peekBack())

# キューからデータを取り出し、取り出したデータを表示
print("dequeued :" + str(q.dequeue()))
# キューの先頭と末尾を表示
print(q.peekFront())
print(q.peekBack())

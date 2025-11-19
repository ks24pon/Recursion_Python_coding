# Node class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Stack class
class Stack:
  # インスタンス作成ヘッドは存在しない初期値
  def __init__(self):
    self.head = None
  
  # 新しい要素をスタックの一番上の要素を追加する関数
  def push(self,data):
    # 現在のヘッドを一時的に保存
    temp = self.head
    # 新しいNode作成し、新しいヘッドとする
    self.head = Node(data)
    # 元のヘッドを設定
    self.head.next = temp

  # スタックの一番上の要素を取り出すための関数
  def pop(self):
    # スタックが空の場合、何も取り出せないNoneを返す
    if self.head == None: return None
    # 現在のヘッドを一時的に保存
    temp = self.head
    # ヘッドの次の要素を新しいヘッドにする
    self.head = self.head.next
    # 保存しておいた元のヘッドのデータを返します
    return temp.data
  
  # 一番上のスタック要素を確認する
  def peek(self):
    # スタックが空の場合、Noneを返す
    if self.head is None: return None
    # 現在のヘッドデータを返す
    return self.head.data
  
# 新しいスタック作成
s = Stack()

# スタックに2を追加
s.push(2)
# スタックの一番上の要素を確認
print(s.peek())

# スタックに4を追加
s.push(4)
# スタックに3を追加
s.push(3)
# スタックに1を追加
s.push(1)

# スタックの一番上の要素を取り出す
s.pop()
# スタックの一番上の要素を確認

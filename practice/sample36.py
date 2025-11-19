# Node class:
class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

# Deque class:
class Deque:
  def __init__(self):
    self.head = None
    self.tail = None

  def peekFront(self):
    if self.head is None: return None
    return self.head.data
  
  def peekBack(self):
    if self.tail is None: return None
    return self.tail.data
  
  def enqueueFront(self,data):
    if self.head is None:
      self.head = Node(data)
      self.tail = self.head
    else:
      self.head.prev = Node(data)
      self.head.prev.next = self.head
      self.head = self.head.prev
  
  def enqueueBack(self,data):
    if self.head is None:
      self.head = Node(data)
      self.tail = self.head
    else:
      self.tail.next = Node(data)
      self.tail.next.prev = self.tail
      self.tail = self.tail.next
  
  def dequeueFront(self):
    if self.head is None: return None

    temp = self.head
    self.head = self.head.next
    if self.head is None: self.tail = None
    else: self.head.prev = None

    return temp.data
  
  def dequeueBack(self):
    if self.tail is None: return None

    temp = self.tail
    self.tail = self.tail.prev

    if self.tail is None: self.head = None
    else: self.tail.next = None
    return temp.data
  
def getMax(arr):
  deque = Deque()
  deque.enqueueFront(arr[0])

  # 最大値は両端キューの先頭へ、その他の値は末尾へ
  for i in arr[1:]:
    if i > deque.peekFront(): deque.enqueueFront(i)
    else: deque.enqueueBack(i)

  return deque.peekFront()

print(getMax([34,35,64,34,10,2,14,5,353,23,35,63,23]))



  
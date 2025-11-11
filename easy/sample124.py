class Book:
  def __init__(self, author, title, year):
    self.author = author
    self.title = title
    self.year = year

def printBookArray(books):
  for s in books:
    print(s.author + s.title + str(s.year))

books = []
books.append(Book("How Did It All Begin?", "2021"))
books.append(Book("The Theory of Everything", "2010"))
books.append(Book("God Created the Integers", "2006"))

# 出力
printBookArray(books)

class Book:
    def __init__(self, title, year):
        self.author = "Stephen Hawkings"
        self.title = title
        self.year = year

# 本を表示する関数
def printBookArray(books):
    for book in books:
        print(book.title + " written by " + book.author + " in " + book.year)

# リスト作成
books = []
books.append(Book("How Did It All Begin?", "2021"))
books.append(Book("The Theory of Everything", "2010"))
books.append(Book("God Created the Integers", "2006"))

# 出力
printBookArray(books)   
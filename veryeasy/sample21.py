class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title}\n{self.price}"

# テストケース
product1 = Product("shampoo", 10)
print(product1)

product2 = Product("conditioner", 5)
print(product2)

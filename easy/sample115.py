class Vehicle:
    # コンストラクタ
    # init関数は、初期値
    def __init__(self, kart, tire, glider):
        self.kart = kart
        self.tire = tire
        self.glider = glider

# インスタンス
car1 = Vehicle("Standard Kart", "Leaf Tires", "Toy Glider")
print(car1.kart)

car2 = Vehicle("Banana Kart", "Wood Tires", "Ghost Wing")
print(car2.tire)

car3 = Vehicle("Yellow Falcon", "Touring Tires", "Hang Glider")
print(car3.glider)
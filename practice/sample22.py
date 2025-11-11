class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year



def printCarArray(carArray):
  # arrの長さまでループ
  for i in range(0, len(carArray)):
    print(carArray[i].make + " - " + carArray[i].model + " Year " + str(carArray[i].year))

def printCarArraySimple(carArray):
  # ループ
  for car in carArray:
    print(car.make + " - " + car.model + " Year " + str(car.year))

# list
cars = []
cars.append(Car("Toyota","Camry", 2000))
cars.append(Car("BMW", "X1 Sports", 2019))
cars.append(Car("Nissan", "GT-R", 2020))

print("First model: " + cars[0].make + "-" + cars[0].model + "-" + str(cars[0].year))

printCarArray(cars)
print("Simple version...")
printCarArraySimple(cars)
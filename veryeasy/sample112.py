import math

class Line:
    def __init__(self,startPoint,endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    # 線の長さを返す
    def getLength(self):
        dx = self.endPoint.x - self.startPoint.x
        dy = self.endPoint.y - self.startPoint.y
        # 最後に四捨五入
        return round(math.sqrt(dx ** 2 + dy ** 2))

class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

p1 = Point(3,1)
p2 = Point(3,6)
lineAB = Line(p1, p2)
print(lineAB.getLength())

p3 = Point(1,3)
p4 = Point(6,15)
lineCD = Line(p3, p4)
print(lineCD.getLength())


# 立方体の体積
def boxVolume(long,width,height):
  return long * width * height
print(boxVolume(2,3,5))

# 円柱の体積
def cylinderVolume(radius, height):
  return radius * radius * height * 3
print(cylinderVolume(2,5))

# 台形の面積
def trapezoidArea(top,bottom,height):
  return (top+bottom) + height / 2
print(trapezoidArea(3,5,6))

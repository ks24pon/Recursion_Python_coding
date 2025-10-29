import math

def fallingDistance(planet,time):
    meter = 0.5 * planetGravityMpss(planet) * time ** 2
    return math.floor(metersToMiles(meter))

# 重力加速度を求める関数
def planetGravityMpss(planet):
    if planet == "Earth": return 9.8
    elif planet == "Jupiter": return 24.79
    elif planet == "Mercury": return 3.7
    else: return 0


# メートルを受け取り、マイルへ変換する
def metersToMiles(meter):
    return meter * 0.000621371
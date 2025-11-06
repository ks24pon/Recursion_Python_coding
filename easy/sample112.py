import math

def fallingDistance(planet, time):
    # メートル先に計算
    meter = 0.5 * planetGravityMpss(planet) * time ** 2
    return math.floor(metersToMiles(meter))


# 重力加速度を返す関数
def planetGravityMpss(planet):
    if planet == "Earth":
        return 9.8
    elif planet == "Jupiter":
        return 24.79
    elif planet == "Mercury":
        return 3.7
    else:
        return 0

# マイル変換する関数
def metersToMiles(time):
    return time * 0.000621371

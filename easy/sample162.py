import math


def fallingDistance(planet, time):
    meter = 0.5 * planetGravityMpss(planet) * time ** 2
    return math.floor(metersToMiles(meter))


# 惑星名受け取り、重力加速度を返す関数
def planetGravityMpss(planet):

    if planet == "Earth":
        return 9.8
    if planet == "Jupiter":
        return 24.79
    if planet == "Mercury":
        return 3.7
    return 0

# メートルを受け取り、マイルへ変換する関数


def metersToMiles(meter):
    return meter * 0.000621371

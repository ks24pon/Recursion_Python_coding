import math

def fallingDistance(planet,time):
    # メートルを先に計算
    meter = (planetGravityMpss(planet) * time ** 2) * 0.5
    # マイル変換して、小数点ん切り捨て
    return math.floor(metersToMiles(meter))

# 惑星名を受け取り重力加速度を返す関数
def planetGravityMpss(planet):
    if planet == "Earth":
        return 9.8
    if planet == "Jupiter":
        return 24.79
    if planet == "Mercury":
        return 3.7
    else:
        return 0

# メートル受け取り、マイルへ変換
def metersToMiles(meter):
    return meter *  0.000621371


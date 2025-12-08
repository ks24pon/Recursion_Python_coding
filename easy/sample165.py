import math

# 惑星名を受け取り、重力加速度を返す関数
def planetGravityMpss(planet):
    gravityList = {
        "Earth": 9.8,
        "Jupiter": 24.79,
        "Mars": 3.71,
        "Pluto": 0.58,
        "Moon": 1.62,
    }
    return gravityList.get(planet, 0)

# 地面直線の速度を取得する関数
def getVelocity(g,h):
    return math.sqrt(2 * g * h)

# 怖さレベルを文字列で返す関数
def emotionLevel(v):
    if v >= 80:
        return "terrified"
    if v >= 60:
        return "frighten"
    if v >= 40:
        return "scared"
    else:
        return "afraid"

def getEmotion(height,planet):
    g = planetGravityMpss(planet)
    # 重力加速度が定義されてない場合
    if g == 0: return "no data"
    v = getVelocity(g,height)
    return  emotionLevel(v)


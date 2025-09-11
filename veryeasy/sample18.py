def calculateLocation(latitude,longitude):
    lat = getLatitudeDirection(latitude)
    lon = getLongitudeDirectio(longitude)
    return lat + "/" + lon


# 緯度を受け取り、文字列を返す関数
def getLatitudeDirection(latitude):
    if latitude > 0: return "north"
    if latitude < 0: return "south"
    return "equator"


# 経度を受け取り文字列を返す関数
def getLongitudeDirectio(longitude):
    if longitude > 0: return "east"
    if longitude < 0: return "west"
    return "prime meridian"

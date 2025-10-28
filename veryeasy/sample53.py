def getLatitudeDirection(latitude):
    if latitude > 0: return "north"
    if latitude < 0: return "south"
    return "equator"

def getLongitudeDirection(longitude):
    if longitude > 0: return "east"
    if longitude < 0: return "west"
    return "prime meridian"

def calculateLocation(latitude, longitude):
    latPosition = getLatitudeDirection(latitude)
    longPosition = getLongitudeDirection(longitude)
    return latPosition + "/" + longPosition
def calculateLocation(latitude, longitude):

    return getLatitudeDirection(latitude) + "/" + getLongitudeDirection(longitude)


def getLatitudeDirection(latitude):
    if latitude > 0:
        return "north"
    elif latitude < 0:
        return "south"
    else:
        return "equator"


def getLongitudeDirection(longitude):
    if longitude > 0:
        return "east"
    elif longitude < 0:
        return "west"
    else:
        return "prime meridian"

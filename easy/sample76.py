def getBootstrapClass(screenWidth):
    if screenWidth < 768:
        return "xs"
    elif screenWidth < 992:
        return "sm"
    elif screenWidth < 1200:
        return "md"
    else: return "lg"
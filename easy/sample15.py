def getBootstrapClass(screenWidth):

    # 768未満
    if screenWidth < 768: return "xs"
    elif screenWidth >= 1200: return "lg"
    elif screenWidth >= 992: return "md"
    elif screenWidth >= 768: return "sm"
def checkLastDigits(x,y,z):
    # x*yの下一桁とzの1桁の比較
    strXy = str(x * y)
    return strXy[-1] == str(z)[-1]
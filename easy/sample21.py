def getAtLocation(email):
    mark = email.find("@")
    if mark != -1:
        return mark + 1
    return -1
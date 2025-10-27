def getAtLocation(email):
    word = email.find("@")
    if not word == -1:
        return word + 1
    return -1
def lenString(string):
    if string == "":
        return 0
    return 1 + lenString(string[1:])
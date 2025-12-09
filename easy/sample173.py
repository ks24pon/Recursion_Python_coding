def swapPosition(s):
    
    if len(s) <= 1:
        return s
    
    return s[1] + s[0] + swapPosition(s[2:])
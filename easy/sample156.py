def insertUnderscoreAt(s,i):
    front = s[:i]
    back = s[i:]

    if len(s) <= i: return s
    else:
        return front + "_" + back

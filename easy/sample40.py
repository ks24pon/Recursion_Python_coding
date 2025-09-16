def mergeString(s1, s2):
    if not s1 or not s2:
        return ""
    return s1[0] + s2[0] + mergeString(s1[1:], s2[1:])
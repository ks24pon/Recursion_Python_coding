def mergeString(s1,s2):
    if s1 == "" and s2 == "":
        return ""
    # 再帰
    return s1[0] + s2[0] + mergeString(s1[1:], s2[1:])
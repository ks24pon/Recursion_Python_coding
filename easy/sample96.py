def lenString(string):
    # ベースケースで無限ループ阻止
    if string == "":
        return 0

    return lenString(string[:-1]) + 1



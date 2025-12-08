def lenString(string):
    # 空文字になった時に0を返す
    if string == "":
        return 0

    return lenString(string[:-1]) + 1
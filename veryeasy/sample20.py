def hammingDistanceInString(string1, string2):
    # 初期値
    count = 0
    # 文字比較
    for i in range(len(string1)):
        if string1[i] != string2[i]: count += 1
    return count
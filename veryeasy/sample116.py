def countAllChars(arr):
    count = 0

    # 配列内の全ての文字数カウント
    for lists in arr:
        count += len(lists)

    return count

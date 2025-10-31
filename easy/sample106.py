def sheeps(count):
    # ベースケース
    if count == 0:
        return ""
    # 再帰
    return sheeps(count - 1) + f"{count} sheep ~ "
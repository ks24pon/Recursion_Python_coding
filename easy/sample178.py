def sheeps(count):
    # ベースケース
    if count == 0:
        return ""

    return sheeps(count - 1) + f"{count} sheep ~ "

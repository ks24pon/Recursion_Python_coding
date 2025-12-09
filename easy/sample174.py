def product(x, y):
    if y == 0:
        return 0

    # 負の場合は、符号を反転して計算
    if y < 0:
        return -product(x, -y)
    
    return x + product(x, y - 1)
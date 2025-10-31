def product(x,y):
    # ベースケース
    if y == 0:
        return 0
    if y > 0:
        return x + product(x,y-1)
    if y < 0:
        return - product(x,-y)
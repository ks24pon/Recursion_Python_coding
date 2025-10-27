# 例題 1
# 式　3 * 4 / 5 の結果に対して小数点以下の切り捨てを行い、出力してください (2)
# 式 3 * 4 / 5 の結果に対して小数点以下の切り上げを行い、出力してください (3)
print(math.floor(3 * 4 / 5))
print(math.ceil(3 * 4 / 5))

# 例題 2
# 直角三角形において、横、縦の長さを受け取って、斜辺の長さを返す、hypotenuse という関数を sqrt 関数を使って、定義してください
# 横 4、高さ 3 を関数に入力して、コンソールに結果を出力してください (5.0)
def hypotenuse(width, height):
    return math.sqrt(width*width + height*height)

print(hypotenuse(4,3))

# 例題 3
# ある整数を受け取って、2^x を計算する、exponentialOfTwo という関数を pow 関数を使って作成してください
# 3 を関数に入力して、コンソールに結果を出力してください (8.0)
# 10 を関数に入力して、コンソールに結果を出力してください (1024.0)
def exponentialOfTwo(num):
    return math.pow(2,num)

print(exponentialOfTwo(3))
print(exponentialOfTwo(10))
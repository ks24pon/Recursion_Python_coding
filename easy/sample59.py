# アルファベットをすべて含むかどうか判定
def isPangram(string):
    # アルファベット26文字をセットに格納
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # 入力文字列を小文字に変換し、1文字ずつチェック
    for char in string.lower():
        # もしアルファベットに含まれる文字ならセットから削除
        if char in alphabet:
            alphabet.remove(char)

    # セットが空になれば、全ての合うファベットが使われたということ
    return len(alphabet) == 0
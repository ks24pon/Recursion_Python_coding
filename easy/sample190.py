def caesarCipher(message, n):
    # 暗号化した文字追加
    result = ""

    for char in message:
        # 空白無視
        if char == " ":
            continue
        # ordで文字コードで返してアルファベット数26で割る
        shifted = (ord(char) - ord('a') + n) % 26
        # 文字列に戻す
        result += chr(ord('a') + shifted)
    
    return result
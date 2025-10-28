# 練習 1
mail = "recursion@info.com"

# 1.メソッドチェーンを使って、COM という大文字を出力してください。
# ヒント:upperCase, subStringの組み合わせ
print(mail[15:len(mail)].upper())


# 2.メソッドチェーンを使って、%INFO.COM を出力してください。
# ヒント:replace, upperCaseの組み合わせ
print(mail[9:len(mail)].replace("@", "%").upper())

# 3.メソッドチェーンを使って、RecuRsion を出力してください。
# ヒント:subString, replaceの組み合わせ
print(mail[0:9].replace("r","R"))
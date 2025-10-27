# 例題 1
# recursion@info.com の @ のインデックスの位置を調べましょう
email = "recursion@info.com"
# print で出力してください
print(email.find("@"))


# 例題 2
# 例題 1 で求めたインデックスを @ の位置として変数 atLocation に入れましょう
# 変数 atLocation を使って、recursion@info.com の @ より後ろを切り取りましょう
# print で出力してください
atLocation = email.find("@")

word = email[atLocation+1:len(email)]
print(word)
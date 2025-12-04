def upperCaseDomain(email):
    # find関数で@の位置を取得
    domain = email.find("@")
    # @以降をupper()で大文字
    return email[domain+1].upper()

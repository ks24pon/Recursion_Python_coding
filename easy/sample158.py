def isValidEmail(email):
    # @の位置を探す
    atIndex = email.find("@")
    # @以降の切り取り
    domain = email[atIndex + 1:len(email)]

    # pから始まらない
    if atIndex <= 0:
        return False

    # スペースがないこと
    hasNoSpace = " " not in email
    # @を1つのみ含んでいる
    hasOnlyOneAt = email.count("@") == 1
    # @の後に。が含まれている
    domainHasHost = "." in domain

    return hasNoSpace and hasOnlyOneAt and domainHasHost

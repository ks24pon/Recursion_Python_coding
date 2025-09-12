def upperCaseDomain(email):
    # @の位置探す
    pos = email.find("@")
    # @の次から末尾までにして大文字
    after_at = email[pos+1:].upper()
    return after_at
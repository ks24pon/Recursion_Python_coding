def isValidEmail(email):
    # @の後のインデックス
    indexOfAt = email.find("@")

    # @の後のアドレス
    domain = email[indexOfAt + 1:len(email)]

    if indexOfAt > 0 and email.find(" ") == -1 and domain.find("@") == -1 and not domain.find(".") == -1:
        return True
    else:
        return False
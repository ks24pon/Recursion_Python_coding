def isValidEmail(email):
    atIndex = email.find("@")
    domain = email[atIndex + 1:len(email)]

    if atIndex > 0 and email.find(" ") == -1 and domain.find("@") == -1 and not domain.find(".") == -1:
        return True
    else:
        return False

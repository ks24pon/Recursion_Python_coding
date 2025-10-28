def upperCaseDomain(email):
    atIndex = email.find("@")
    return email[atIndex + 1:len(email)].upper()

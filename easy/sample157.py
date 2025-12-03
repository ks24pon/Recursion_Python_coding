def lastFourHint(stringInput):

    if len(stringInput) < 6: return "There is no Hint"
    else:
        return "Hint is:" + stringInput[-4:]

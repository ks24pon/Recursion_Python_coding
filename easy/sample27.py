def lastFourHint(stringInput):
    # 6文字未満の場合
    if len(stringInput) < 6:
        return "There is no Hint"
    # 最後の4文字
    last_four = stringInput[-4:]
    return f"Hint is:{last_four}"
def hasPenalty(records):
    # 2番目の要素から最後までループ
    for i in range(1, len(records)):
        # もし現在の要素が1つ前の要素より小さい場合、減少
        if records[i] < records[i -1]:
            return True # ペナあり

    # 最後まで現象がなければFalse
    return False
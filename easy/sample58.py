def videosToWatch(time,dailyGoal):
    # 累計の視聴時間
    total = 0

    # 見た動画の本数
    count = 0

    # time配列の中の各動画を1つずつループ
    for t in time:
        total += t # 累計時間に追加
        count += 1 # 動画本数を1本追加

        # 累計時間が目標に達成したら、その時点で本数を返す
        if total >= dailyGoal:
            return count
    # 最後まで見ても目標に届かなかった場合は-1を返す
    return -1




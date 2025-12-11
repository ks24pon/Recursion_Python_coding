def fizzBuzz(n):
    # 初期値
    count = []

    # 1からnまでの数を処理
    for i in range(1, n + 1):
        # 3と5の両方で割り切れる場合は"FizzBuzz"
        if i % 3 == 0 and i % 5 == 0:
            count.append("FizzBuzz")
        # 3で割り切れる場合は"Fizz"
        elif i % 3 == 0:
            count.append("Fizz")
        # 5で割り切れる場合は"Buzz"
        elif i % 5 == 0:
            count.append("Buzz")
        # どちらでも割り切れない場合は文字列として追加
        else:
            count.append(str(i))
    
    # 結果リストをハイフンで繋いで返す
    return "-".join(count)


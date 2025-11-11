def totalFoundInSentence(sentences, c):
  count = 0

  # 配列の各文字列にアクセス
  for sentence in sentences:
    # 文字列の各文字にアクセス
    for character in sentence:
      # 文字が一致するかどうかチェック
      if character.lower() == c.lower():
        count = count + 1
        break
  return count

list2 = ["The wood", "Pecked peckers", "At the inn", "Tomorrowland"]
print(totalFoundInSentence(list2, "a"))
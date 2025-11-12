def charInBagOfWordsCount(bagOfWords,keyCharacter):
  # 初期値
  total = 0

  # ループ処理
  for word in bagOfWords:
    for char in word:
      if char == keyCharacter:
        total += 1
  return total


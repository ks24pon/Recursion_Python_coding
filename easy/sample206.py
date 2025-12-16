def charInBagOfWordsCount(bagOfWords, keyCharacter):
    count = 0

    for i in range(len(bagOfWords)):
        for j in range(len(bagOfWords[i])):
            if bagOfWords[i][j] == keyCharacter:
                count += 1
    return count




def countCharactersAfterN(arr):
  count = 0
  for s in arr:
    for char in s:
      if ord("n") <= ord(char):
        count += 1
  return count
def isFirstStringLarger(s1,s2):
  asc1 = sum(ord(c) for c in s1.lower())
  asc2 = sum(ord(c) for c in s2.lower())

  return asc1 > asc2
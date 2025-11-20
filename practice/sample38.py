def linearSearch(key, haystack):
  for i in range(len(haystack)):
    if haystack[i] == key:
      return i
  return -1


l1 = [3,4,2,5,46,23,3,55,67,24,65]
print(linearSearch(5,l1))
print(linearSearch(24,l1))

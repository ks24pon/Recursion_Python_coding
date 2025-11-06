def findLetter(sentence, letter):
  found = False
  message = "Will we find ["+ letter + "] in our message? "

  for i in range(0, len(sentence)):
    if(sentence[i] == letter[0]):
      found = True
      break

  return message + "It looks like we found it!" if found else message + "Sadly, we did not find it."


print(findLetter("It is a sunny day.", "a"))
print(findLetter("It is a sunny day.", "o"))
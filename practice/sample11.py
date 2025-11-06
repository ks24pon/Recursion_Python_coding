def message(inputMessage):
  inputMessage = inputMessage + " - is the message."
  return inputMessage

def myFun():
  subject = "It will rain tomorrow"
  print(subject)

  newMessage = message(subject)

  print(subject)
  print(newMessage)

# 呼び出し
myFun()
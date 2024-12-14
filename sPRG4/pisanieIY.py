import random

def enterCorrectIY():
  userSentence = input("Enter a word or a sentence with i/y: ")

  print(userSentence.replace('i', '_').replace('y', '_').replace('I', '_').replace('Y', '_'))

  senctencetoBeEvaluated = input("Enter again the sentence with i/y: ")

  if senctencetoBeEvaluated == userSentence:
    print("Correct")
  else:
    print("Incorrect")

enterCorrectIY()
print("")


# BONUS:
listOfWords = ['kybel', 'figel', 'dikobraz', 'bicykel', 'kyjak', 'vlky']

def correctIYquestionnaire(words):
  random.shuffle(words)
  correctCount = 0
  incorrectCount = 0

  for word in words:
    print(word.replace('i', '_').replace('y', '_'))
    userInput = input("Enter the corrected version of the word: ")
    if userInput == word:
      correctCount += 1
      print("Correct")
      print("")
    else:
      incorrectCount += 1
      print("Incorrect")
      print("")

  print("Corrected words: ", correctCount)
  print("Incorrected words: ", incorrectCount)

correctIYquestionnaire(listOfWords)
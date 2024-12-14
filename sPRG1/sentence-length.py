sentence = input("Give me a sentence: ")

sentenceWithoutSpaces = ""

if sentence != "":
  words = sentence.split(" ")
  if words[0] != "" and words[1] !="":
    wordCount = len(words)
    print("Your sentence has " + str(wordCount) + " words.")

    for word in words:
      sentenceWithoutSpaces += word
    print("Your sentence without space is " + str(sentenceWithoutSpaces.lower()))

  elif words[0] == "" and words[1] == "":
    print("Please enter a sentence.")

elif sentence == "":
  print("Please enter a sentence.")
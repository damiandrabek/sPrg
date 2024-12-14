word1 = input("Word: ")

def toUpperCase(word):
  upperWord = ""
  for char in word:
    upperChar = chr(ord(char) - 32)
    upperWord += upperChar
  return upperWord

print(toUpperCase(word1))
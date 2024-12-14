userInput = input("Enter a word you wish to encrypt: ")

encryptedChars = ''

for char in userInput:
  asciiValue = ord(char)
  encryptedChar = chr(asciiValue + 2)
  encryptedChars += encryptedChar
  
print(encryptedChars)
userInput = input("Enter your word to be evaluated if it is a palindrome: ")

def isPalindrome(word):
  word = lower(word)
  reversedWord = word[::-1]
  if word == reversedWord:
    return True
  else:
    return False

print(isPalindrome(userInput))
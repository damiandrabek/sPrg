import random
import string

# Function to generate a random password
def generate_random_password(passwordLength):
  # Define the characters to be used in the password
  characters = string.ascii_letters + string.digits + string.punctuation

  result = ''
  for i in range(passwordLength):
    randomChar = random.choice(characters)
    result += randomChar

  return result

print(generate_random_password(8))
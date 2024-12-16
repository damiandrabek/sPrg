import re

# 53/2
def remove_vowels(word):
  pattern = r'[aeiouAEIOU]'
  return re.sub(pattern, '', word)
print(remove_vowels("fajnsmeker"))

# 53/4
def returnLonger(word1, word2):
  if len(word1) > len(word2):
    return word1
  else:
    return word2

print(returnLonger("fajnsmeker", "kajnsmentke"))

# 53/5
userMail = "fajnsmeker@1sg.sk"
def is_email(mail):
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if re.match(pattern, mail):
    return True
  else:
    return False
print(is_email(userMail))


########################################################################


# predposledny
def write_into_single_text(text1, text2):

  with open(text1, "r") as file1:
    lines1 = file1.readlines()

  with open(text2, "r") as file2:
    lines2 = file2.readlines()

  with open("output.txt", "w") as output_file:
    for line in lines1:
      output_file.write(line.strip()+ "\n")
    for line in lines2:
      output_file.write(line.strip()+ "\n")

write_into_single_text("article1.txt", "article2.txt")

## bonus
def BONUS_write_into_single_text(text1, text2):

  with open(text1, "r") as file1:
    lines1 = file1.readlines()

  with open(text2, "r") as file2:
    lines2 = file2.readlines()

  max_len = max(len(lines1), len(lines2))

  with open("output.txt", "w") as BONUS_output_file:
    for i in range(max_len):
      if i < len(lines1):
        BONUS_output_file.write(lines1[i].strip()+ "\n")
      if i < len(lines2):
        BONUS_output_file.write(lines2[i].strip()+ "\n")

BONUS_write_into_single_text("article1.txt", "article2.txt")

########################################################################

# posledny
wordie = input("Enter a word to by consonanted: ")
def subVowel(word):
  pattern = r'[aeiouAEIOU]'
  print(re.sub(pattern, "-", word))
subVowel(wordie)
def subConsonant(word):
  pattern = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
  print(re.sub(pattern, "-", word))
subConsonant(wordie)
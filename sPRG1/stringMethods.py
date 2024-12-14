word1 = 'Servus'
word2 = 'Cau'

finalWord = ''

for i in range(len(word1)):
  if i <= len(word2)-1:
    finalWord += word1[i] + word2[i]
  elif i > len(word2)-1:
    finalWord += word1[i]

print(finalWord)
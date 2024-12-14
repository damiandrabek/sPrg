def analyzeText(filePath, fileEncoding):
  with open(filePath, "r", encoding= fileEncoding) as file:
    lines = file.readlines()

  wordCount = 0
  wordLengths = {}

  for line in lines:
    words = line.split()
    wordCount += len(words)
    for word in words:
      length = len(word)
      if length not in wordLengths:
        wordLengths[length] = 0
      wordLengths[length] += 1

  print(f"Pocet slov: {wordCount}")
  for length in sorted(wordLengths):
    print(f"Pocet slov s {length} pismenom/nami: {wordLengths[length]}")

  # reversed file
  reversedFilePath = filePath.replace('.txt','_reversed.txt')

  with open(reversedFilePath, "w", encoding=fileEncoding) as reversed_file:
    reversed_file.writelines(lines[::-1])

  print(f"Prehodeny obsah bol ulozeny do suboru: {reversedFilePath}")


file_path = "clanok.txt"
file_encoding = "cp1250"
analyzeText(file_path, file_encoding)
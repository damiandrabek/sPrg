import random

word1 = input('Word to shuffle: ')

def shuffle(wordToShuffle):
  # Convert the string to a list of characters
    wordList = list(wordToShuffle)
    
    # Implementing the Fisher-Yates Shuffle
    for i in range(len(wordList) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap wordList[i] with wordList[j]
        wordList[i], wordList[j] = wordList[j], wordList[i]
    
    # Convert the list back to a string
    return ''.join(wordList)


print(shuffle(word1))
#ÚLOHA 1

#1. Vytvorte program, ktorý si vypyta vstup od používateľa a ten následne preloží do Morseovej abecedy ✅
#2. Program využije už definovanú funkciu translate(letter) pričom jej vstupný parameter je písmeno, ktoré chceme preložiť a vracia dané písmeno preložené ako string vo forme "." a "-" ✅
#3. Ak nerobíte na bonusovej úlohe funkciu translate neupravujte 
#4. Program prekladá len malé písmená a ostatné znaky nechá nezmenené (nechá rovnaké písmená/čísla/symboly ako boli na vstupe) 
#5. Napr. "Ahoj jozo!" vypíše "A / .... / --- / .--- /   / .--- / --- / --.. / --- / !" ✅
#6. Každé písmeno morseovej abecedy(prípadne symbol ktorý sa neprekladá) je kvôli lepšej čitatelnosti oddelené " / "(medzera lomítko medzera)✅
#7. Za posledným písmenom už oddelovač nieje ✅
#8. BONUS: upravte funkciu translate tak aby vedela preložiť aj veľké aj malé písmená abecedy(anglickej)✅

morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
'-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']


def translate(letter):
    index = ord((letter))-97

    if 0 <= index <= 25:
      return morse_code[index]

    elif -32 <= index < 0:
      index += 32
      return morse_code[index]

    else:
      return letter



def translate_words(userInput):
    translated_words = []
    words = userInput.split()

    for word in words:
        translated_word = ''

        for letter in word:
          if len(word) == 1:
            translated_word += translate(letter)
            break

          if letter == word[-1]:
            translated_word += translate(letter)
            break

          translated_word += translate(letter) + ' / '
            
        translated_words.append(translated_word.rstrip())

    return ' '.join(translated_words)

user_input1 = input('Enter words to be translated as morse code: ')
print(translate_words(user_input1))


#ÚLOHA 2

#Napíšte program, v ktorom používateľ zadá platnú URL adresu. Program následne vypíše:
# a) protokol použitej služby, - text v url po znaky "://", môže mať premenlivú dĺžku ✅
# b) doménovú adresu servera. - text za "://" až po ďalší znak "/" ✅
# c) doménu najvyššej úrovne, - časť doménovej adresy od poslednej bodky po koniec ✅

#pre adresu https://1sg.sk/vyucovanie/projekty/ vypíše:
# a) https
# b) 1sg.sk
# c) sk


user_input2 = input("Enter a website URL: ")

def website_params (inputURL):
  protocol = inputURL[:inputURL.find("://")]
  domain = inputURL[inputURL.find("://")+3:inputURL.find("/", inputURL.find("://")+3)]
  domain_level = domain[domain.rfind(".")+1:]
  print(protocol)
  print(domain)
  print(domain_level)

website_params(user_input2)
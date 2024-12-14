birthNum1 = "860615/0000"
birthNum2 = "245707/1111"
birthNum3 = "070317/1111"

def birthNumTest(birthNum):
  split_pairs = [birthNum[i:i+2] for i in range(0, len(birthNum)-6, 2)]

  if int(split_pairs[1]) >= 50:
    split_pairs[1] = "0" + str(int(split_pairs[1])-50)

  century = ""
  if int(split_pairs[0]) >= 25:
    century = "19"
  else:
    century = "20"

  dateOfBirth = ""
  dateOfBirth = str(split_pairs[2]) + "." + str(split_pairs[1]) + "." + century  + str(split_pairs[0])
  print(dateOfBirth)

  


birthNumTest(birthNum1)

birthNumTest(birthNum2)

birthNumTest(birthNum3)


a = 'a'

print(ord(a))
print(chr(ord(a)))
with open("sutaz_vbehu.txt", "r") as file:
  lines = file.readlines()

sportovci = []
for line in lines:
  priezvisko, cas = line.split()
  sportovci.append((priezvisko, int(cas)))

print("Počet zúčastnených športovcov:", len(sportovci))

for priezvisko, cas in sportovci:
  print(f"Súťažiaci {priezvisko} dobehol do cieľa za {cas} sekúnd")

najlepsi_sportovec = sportovci[0]
for sportovec in sportovci:
  if sportovec[1] < najlepsi_sportovec[1]:
    najlepsi_sportovec = sportovec

najlepsi_priezvisko, najlepsi_cas = najlepsi_sportovec
minuty = najlepsi_cas // 60
sekundy = najlepsi_cas % 60

print(f"Víťaz je {najlepsi_priezvisko} s časom {minuty} min. {sekundy} sek.")
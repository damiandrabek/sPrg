#program rozhovor
from random import *

meno = input ('Ako sa voláš? ')
print('Ahoj '+meno+' rád Ťa spoznávam :)')

roknarodenia = input (meno+', v ktorom roku si sa narodil? ')

vek = 2024 - int(roknarodenia)
meno2 = choice (('Alena', 'Barbora', 'Eva','Sofia'))

print('Á spomínam si, v roku '+roknarodenia+' sa narodila aj '+meno2 +',')
print('to znamená ze mas ' + str(vek) + ' rokov.')

if vek < 100:
  doSto = 100 - vek
  print('Do dovŕšenia sto rokov ti chýba '+str(doSto))

elif vek >= 100:
  print('Uz mas cez sto rokov.')
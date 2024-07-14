"""Marchewka w pudełku, autor: Al Sweigart, al@inventwithpython.com
Prosta, zabawna gra na blefowanie dla dwóch graczy.
Oparta na grze z brytyjskiego programu telewizyjnego '8 Out of 10 Cats'.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, dla początkujących, gra, dla dwóch graczy"""

import random

print('''Marchewka w pudełku, autor: Al Sweigart, al@inventwithpython.com

To jest gra na blefowanie dla dwóch graczy. Każdy gracz ma pudełko.
W jednym pudełku jest marchewka.
Aby wygrać, w swoim pudełku musisz mieć marchewkę.

To bardzo prosta i zabawna gra.

Pierwszy gracz zagląda do swojego pudełka.(Drugi gracz w tym czasie
zamyka oczy). Pierwszy gracz mówi: "W moim pudełku jest marchewka"
lub "W moim pudełku nie ma marchewki". Drugi gracz musi zdecydować,
czy chce zamienić się pudełkami.
''')
input('Naciśnij przycisk, aby rozpocząć...')

p1Name = input('Gracz 1, podaj swoje imię: ')
p2Name = input('Gracz 2, podaj swoje imię: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''OTO DWA PUDEŁKA:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|CZERWONE | |  |ZŁOTE    | |
|PUDEŁKO  | /  |PUDEŁKO  | /
+---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', masz przed sobą CZERWONE pudełko.')
print(p2Name + ', masz przed sobą ZŁOTE pudełko.')
print()
print(p1Name + ', zajrzyj do swojego pudełka.')
print(p2Name.upper() + ', zamknij oczy i nie podglądaj!!!')
input('Gdy ' + p2Name + ' zamknie oczy, naciśnij Enter...')
print()

print(p1Name + ', w Twoim pudełku:')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|CZERWONE | |  |ZŁOTE    | |
| PUDEŁKO | /  |PUDEŁKO  | /
+---------+/   +---------+/
 (jest marchewka!)''')
    print(playerNames)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|CZERWONE | |  |ZŁOTE    | |
|PUDEŁKO  | /  |PUDEŁKO  | /
+---------+/   +---------+/
(nie ma marchewki!)''')
    print(playerNames)

input('Naciśnij Enter, aby kontynuować...')

print('\n' * 100)  # Wyczyść ekran przez wyświetlenie 100 znaków nowej linii.
print(p1Name + ',' + p2Name + ' może otworzyć oczy.')
input('Naciśnij Enter, aby kontynuować...')

print()
print(p1Name + ', powiedz jedno z dwóch zdań.')
print('  1) W moim pudełku jest marchewka.')
print('  2) W moim pudełku nie ma marchewki.')
print()
input('Naciśnij Enter, aby kontynuować...')

print()
print(p2Name + ', czy chcesz zamienić się pudełkami? TAK/NIE')
while True:
    response = input('> ').upper()
    if not (response.startswith('T') or response.startswith('N')):
        print(p2Name + ', wpisz "TAK" lub "NIE".')
    else:
        break

firstBox = 'CZERWONE'  
secondBox = 'ZŁOTE   ' # Zauważ, że po "E" są 3 spacje.

if response.startswith('T'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''OTO DWA PUDEŁKA:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|{} | |  |{} | |
|PUDEŁKO  | /  |PUDEŁKO  | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Naciśnij Enter, by zobaczyć, kto wygrał...')
print()

if carrotInFirstBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|{} | |  |{} | |
|PUDEŁKO  | /  |PUDEŁKO  | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|{} | |  |{} | |
|PUDEŁKO  | /  |PUDEŁKO  | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)

# Ogłoszenie zwycięzcy jest możliwe dzięki zmiennej carrotInFirstBox.
if carrotInFirstBox:
    print(p1Name + ' wygrał(a)!')
else:
    print(p2Name + ' wygrał(a)!')

print('Dziękujemy za grę!')

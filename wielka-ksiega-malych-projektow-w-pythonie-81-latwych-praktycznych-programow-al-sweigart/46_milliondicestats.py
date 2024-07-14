"""Symulator miliona rzutów kostką
Autorstwa Ala Sweigarta al@inventwithpython.com
Symulacja miliona rzutów kostką.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, matematyka, symulacja"""

import random, time

print('''Symulator miliona rzutów kostką
autor: Al Sweigart, al@inventwithpython.com

Podaj, iloma kostkami chciałbyś rzucić:''')
numberOfDice = int(input('> '))

# Deklaracja słownika do zapisywania wyników każdego rzutu kostką:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Rzuć kostką:
print('Symulacja 1000000 rzutów kostką nr: {} ...'.format(numberOfDice))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% rzutów wykonanych...'.format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Wyświetl wyniki:
print('SUMA - RZUTY - PROCENT')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print('  {} - {} rzutów - {}%'.format(i, roll, percentage))

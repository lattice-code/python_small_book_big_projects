"""Rozkład na czynniki, autor: Al Sweigart, al@inventwithpython.com
Znajduje wszystkie czynniki danej liczby.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, matematyka"""

import math, sys

print('''Rozkład na czynniki, autor: Al Sweigart, al@inventwithpython.com

Czynniki danej liczby to dwie liczby, które pomnożone przez siebie dają tę liczbę.
Na przykład 2 x 13 = 26, więc czynnikami liczby 26 są 2 i 13.
Co więcej, 1 x 26 = 26, więc 1 i 26 są również czynnikami 26.  
Zatem liczba 26 ma cztery czynniki: 1, 2, 13 i 26.

Jeśli liczba ma tylko dwa czynniki (1 i samą siebie), to taką liczbę nazywamy pierwszą, 
w przeciwnym razie jest to liczba złożona.

Czy odkryjesz jakieś liczby pierwsze?
''')

while True:  # Główna pętla programu.
    print('Wpisz dodatnią liczbę całkowitą, którą chcesz rozłożyć na czynniki (lub KONIEC):')
    response = input('> ')
    if response.upper() == 'KONIEC':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Znajdź czynniki podanej liczby:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # Jeśli nie ma reszty, to jest to czynnik.
            factors.append(i)
            factors.append(number // i)

    # Przekształć na zestaw, by pozbyć się tych samych czynników:
    factors = list(set(factors))
    factors.sort()

    # Wyświetl wyniki:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))

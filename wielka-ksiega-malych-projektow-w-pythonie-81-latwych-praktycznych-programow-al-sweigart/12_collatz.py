"""Problem Collatza, autorstwa Al Sweigart al@inventwithpython.com
Generuje liczby dla ciągu Collatza na podstawie podanej liczby początkowej.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Problem_Collatza.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, matematyka"""

import sys, time

print('''Problem Collatza lub problem 3n + 1
autor: Al Sweigart, al@inventwithpython.com

Problem Collatza to ciąg liczb wygenerowany na podstawie 
liczby początkowej n z zastosowaniem trzech zasad:

1) Jeśli liczba n jest parzysta, kolejna liczba n to n : 2.
2) Jeśli liczba n jest nieparzysta, kolejna liczba n to n * 3c + 1.
3) Jeśli liczba n to 1, zatrzymaj. W przeciwnym razie, powtórz.

To ogólne sformułowanie, ale jak dotąd nieudowodnione matematycznie -,
każda liczba początkowa wcześniej czy później będzie miała wartość 1
''')

print('Podaj liczbę początkową (większą niż 0) lub KONIEC:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('Musisz podać liczbę całkowitą większą od 0.')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:  # Jeśli n jest parzyste...
        n = n // 2
    else:  # W innym przypadku n jest nieparzyste...
        n = 3 * n + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()

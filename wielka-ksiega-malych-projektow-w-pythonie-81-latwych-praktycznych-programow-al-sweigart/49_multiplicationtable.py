"""Tabliczka mnożenia, autor: Al Sweigart, al@inventwithpython.com
Wyświetla tabliczkę mnożenia.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip
Etykiety: króciutki, dla początkujących, matematyka"""

print('Tabliczka mnożenia, autor: Al Sweigart, al@inventwithpython.com')

# Wyświetl oznaczenia kolumn:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# Wyświetl wynik mnożenie w każdym wierszu:
for number1 in range(0, 13):

    # Wyświetl oznaczenia wierszy:
    print(str(number1).rjust(2), end='')

    # Wyświetl kreskę oddzielającą:
    print('|', end='')

    for number2 in range(0, 13):
        # Wyświetl wynik mnożenia, a za nim spację:
        print(str(number1 * number2).rjust(3), end=' ')

    print()  # Wyświetl znak nowej linii na końcu wiersza.

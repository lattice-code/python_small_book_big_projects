"""Tęcza, autor: Al Sweigart, al@inventwithpython.com
Wyświetla prostą animację tęczy. Naciśnij Ctrl+C, by zatrzymać program.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, artystyczny, bext, dla początkujących, przewijanie"""

import time, sys

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować zgodnie z instrukcjami ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

print('Tęcza, autor: Al Sweigart, al@inventwithpython.com')
print('Naciśnij Ctrl+C, by zatrzymać program.')
time.sleep(3)

indent = 0  # Liczba spacji wcięcia.
indentIncreasing = True  # Czy wcięcie się powiększa, czy nie.

try:
    while True:  # Główna pętla programu.
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            # Zwiększ liczbę spacji:
            indent = indent + 1
            if indent == 60:  # (!) Spróbuj zmienić tę wartość na 10 lub 30.
                # Zmień kierunek:
                indentIncreasing = False
        else:
            # Zmniejsz liczbę spacji:
            indent = indent - 1
            if indent == 0:
                # Zmień kierunek:
                indentIncreasing = True

        time.sleep(0.02)  # Dodaj krótką pauzę.
except KeyboardInterrupt:
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

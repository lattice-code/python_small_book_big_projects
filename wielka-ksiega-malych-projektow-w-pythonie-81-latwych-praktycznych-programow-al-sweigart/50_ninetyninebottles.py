"""99 butelek mleka na półce
Autrostwa Ala Sweigarta al@inventwithpython.com
Wyświetla wszystkie zwrotki jednej z najdłuższych piosenek, jakie kiedykolwiek powstały!
Naciśnij Ctrl+C, by zatrzymać program.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, przewijanie"""

import sys, time

print('99 butelek, autor: Al Sweigart, al@inventwithpython.com')
print()
print('(Naciśnij Ctrl+C, by zatrzymać program.)')

time.sleep(2)

bottles = 99  # To jest początkowa liczba butelek.
PAUSE = 2  # (!) Spróbuj zmienić tę wartość na 0 , by zobaczyć od razu całą piosenkę.

try:
    while bottles > 1:  # Wyświetlaj zwrotki za pomocą pętli.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # Zatrzymaj program na liczbę sekund zapisaną w stałej PAUSE.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1  # Zmniejsz liczbę butelek o jeden.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()  # Wyświetl znak nowej linii.

    # Wyświetl ostatnią zwrotkę:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # Po naciśnięciu klawiszy Ctrl+C zakończ program.

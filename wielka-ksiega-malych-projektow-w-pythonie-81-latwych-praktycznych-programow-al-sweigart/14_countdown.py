"""Odliczanie, autorstwa Al Sweigart al@inventwithpython.com
Animacja odliczania do zera za pomocą cyfr w stylu wyświetlacza 7-segmentowego.
Naciśnij Ctrl+C, by zatrzymać.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Wy%C5%9Bwietlacz_siedmiosegmentowy.
Moduł sevseg.py musi być w tym samym folderze.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, artystyczny"""

import sys, time
import sevseg  # Zaimportuj nasz program sevseg.py.

# (!) Zmień wartość na dowolną liczbę sekund:
secondsLeft = 30

try:
    while True:  # Główna pętla programu.
        # Wyczyść ekran przez wyświetlenie wielu znaków nowej linii:
        print('\n' * 60)

        # Oblicz godziny/minuty/sekundy na podstawie zmiennej secondsLeft:
        # Na przykład: 7265 to 2 godziny, 1 minuta, 5 sekund.
        # Zatem 7265 // 3600 to 2 godziny:
        hours = str(secondsLeft // 3600)
        # A 7265 % 3600 to 65, natomiast 65 // 60 to 1 minuta:
        minutes = str((secondsLeft % 3600) // 60)
        # I 7265 % 60 to 5 sekund:
        seconds = str(secondsLeft % 60)

        # Pobierz łańcuchy znaków będące graficzną reprezentacją cyfr z modułu sevseg:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Wyświetl cyfry:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('    * * * * BUM * * * *')
            break

        print()
        print('Naciśnij Ctrl+C, by zatrzymać program.')

        time.sleep(1)  # Zrób jednosekundową pauzę.
        secondsLeft -= 1
except KeyboardInterrupt:
    print('Odliczanie, autor: Al Sweigart, al@inventwithpython.com')
    sys.exit()  # Po naciśnięciu Ctrl+C, zatrzymaj program.

"""Zegar cyfrowy, autor: Al Sweigart, al@inventwithpython.com
Wyświetla zegar cyfrowy pokazujący aktualny czas za pomocą cyfr
w stylu wyświetlacza siedmiosegmentowego. Naciśnij Ctrl+C, by zatrzymać program.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Wy%C5%9Bwietlacz_siedmiosegmentowy.
Plik sevseg.py musi być w tym samym folderze.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, artystyczny"""

import sys, time
import sevseg  # Importuje nasz program sevseg.py .

try:
    while True:  # Główna pętla programu.
        # Wyczyść ekran poprzez wyświetlenie wielu znaków nowej linii:
        print('\n' * 60)

        # Pobierz aktualny czas z zegara systemowego:
        currentTime = time.localtime()
        # Używamy operacji % 12, więc nasz zegar będzie miał format 12-godzinny, a nie 24-godzinny:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # Zegar w formacie 12-godzinnym pokazuje 12:00, a nie 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Pobierz łańcuch znaków reprezentujących grafikę cyfry z modułu sevseg:
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
        print()
        print('Naciśnij Ctrl+C, by wyjść.')

        # Wykonuj pętle, dopóki zmieniają się sekundy:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Zegar cyfrowy, autor: Al Sweigart, al@inventwithpython.com')
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

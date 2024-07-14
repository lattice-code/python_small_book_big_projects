"""Szybki strzał, autor: Al Sweigart, al@inventwithpython.com
Sprawdź swój refleks, by zobaczyć czy jesteś najszybszym strzelcem na Dzikim Zachodzie.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, gra"""

import random, sys, time

print('Szybki strzał, autor: Al Sweigart, al@inventwithpython.com')
print()
print('Czas sprawdzić swój refleks, by zobaczyć, czy jesteś najszybszym')
print('strzelcem na Dzikim Zachodzie!')
print('Gdy zobaczysz "STRZAŁ", masz 0.3 sekundy, by nacisnąć ENTER.')
print('Jednak przegrasz, jeśli naciśniesz Enter, zanim pojawi się "STRZAŁ".')
print()
input('Naciśnij Enter, by rozpocząć...')

while True:
    print()
    print('Samo południe...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('STRZAŁ!')
    drawTime = time.time()
    input()  # Program nie wychodzi z tej funkcji, dopóki nie naciśniesz Enter.
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        # Jeśli gracz nacisnął Enter przed pojawieniem się STRZAŁ!, funkcja input()
        # kończy się niemal natychmiast.
        print('Strzeliłeś przed pojawieniem się słowa "STRZAŁ"! Przegrałeś.')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('Zajęło Ci', timeElapsed, 'sekundy, by strzelić. Za wolno!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('Zajęło Ci', timeElapsed, 'sekundy, by strzelić.')
        print('Jesteś najszybszym strzelcem na Dzikim Zachodzie! Wygrałeś!')

    print('Wpisz KONIEC, by zakończyć program, lub naciśnij Enter, by zagrać jeszcze raz.')
    response = input('> ').upper()
    if response == 'KONIEC':
        print('Dziękujemy za grę!')
        sys.exit()

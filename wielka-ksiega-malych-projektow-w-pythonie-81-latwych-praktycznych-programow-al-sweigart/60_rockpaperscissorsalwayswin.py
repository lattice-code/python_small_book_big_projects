"""Papier, kamień, nożyce (wersja zwycięzcy), 
autor: Al Sweigart, al@inventwithpython.com
Klasyczna gra z użyciem dłoni, w której zwycięstwo zależy od szczęścia, tylko że w tej wersji zawsze wygrywasz.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, gra, zabawny"""

import time, sys

print('''Papier, kamień, nożyce, autor: Al Sweigart, al@inventwithpython.com
- Kamień wygrywa z nożycami.
- Papier wygrywa z kamieniem.
- Nożyce wygrywają z papierem.
''')

# W tej zmiennej zapisana jest liczba zwycięstw.
wins = 0

while True:  # Główna pętla programu.
    while True:  # Pytaj, dopóki gracz nie wpisze K, P, N lub Z.
        print('Wygrane: {}, Przegrane: 0, Remisy: 0'.format(wins))
        print('Podaj swój ruch: (K)amień (P)apier (N)ożyce lub (Z)akończ')
        playerMove = input('> ').upper()
        if playerMove == 'Z':
            print('Dziękujemy za grę!')
            sys.exit()

        if playerMove == 'K' or playerMove == 'P' or playerMove == 'N':
            break
        else:
            print('Podaj jedną z następujących liter: K, P, N lub Z.')

    # Wyświetl wybór gracza:
    if playerMove == 'K':
        print('KAMIEŃ kontra...')
    elif playerMove == 'P':
        print('PAPIER kontra...')
    elif playerMove == 'N':
        print('NOŻYCE kontra...')

    # Policz do trzech, robiąc trzymające w napięciu pauzy:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Wyświetl wybór komputera:
    if playerMove == 'K':
        print('NOŻYCE')
    elif playerMove == 'P':
        print('KAMIEŃ')
    elif playerMove == 'N':
        print('PAPIER')

    time.sleep(0.5)

    print('Wygrałeś!')
    wins = wins + 1

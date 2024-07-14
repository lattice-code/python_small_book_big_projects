"""Papier, kamień, nożyce, autor: Al Sweigart, al@inventwithpython.com
Klasyczna gra z użyciem dłoni, w której zwycięstwo zależy od szczęścia.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, gra"""

import random, time, sys

print('''Papier, kamień, nożyce, autor: Al Sweigart, al@inventwithpython.com
- Kamień wygrywa z nożycami.
- Papier wygrywa z kamieniem.
- Nożyce wygrywają z papierem.
''')

# W tych zmiennych zapisana jest liczba zwycięstw, przegranych i remisów.
wins = 0
losses = 0
ties = 0

while True:  # Główna pętla programu.
    while True:  # Pytaj, dopóki gracz nie wpisze K, P, N lub Z.
        print('Wygrane: {}, Przegrane: {}, Remisy: {}'.format(wins, losses, ties))
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
        playerMove = 'KAMIEŃ'
    elif playerMove == 'P':
        print('PAPIER kontra...')
        playerMove = 'PAPIER'
    elif playerMove == 'N':
        print('NOŻYCE kontra...')
        playerMove = 'NOŻYCE'

    # Policz do trzech, robiąc trzymające w napięciu pauzy:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Wyświetl wybór komputera:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'KAMIEŃ'
    elif randomNumber == 2:
        computerMove = 'PAPIER'
    elif randomNumber == 3:
        computerMove = 'NOŻYCE'
    print(computerMove)
    time.sleep(0.5)

    # Wyświetl i zapisz wygraną/przegraną/remis:
    if playerMove == computerMove:
        print('Jest remis!')
        ties = ties + 1
    elif playerMove == 'KAMIEŃ' and computerMove == 'NOŻYCE':
        print('Wygrałeś!')
        wins = wins + 1
    elif playerMove == 'PAPIER' and computerMove == 'KAMIEŃ':
        print('Wygrałeś!')
        wins = wins + 1
    elif playerMove == 'NOŻYCE' and computerMove == 'PAPIER':
        print('Wygrałeś!')
        wins = wins + 1
    elif playerMove == 'KAMIEŃ' and computerMove == 'PAPIER':
        print('Przegrałeś!')
        losses = losses + 1
    elif playerMove == 'PAPIER' and computerMove == 'NOŻYCE':
        print('Przegrałeś!')
        losses = losses + 1
    elif playerMove == 'NOŻYCE' and computerMove == 'KAMIEŃ':
        print('Przegrałeś!')
        losses = losses + 1

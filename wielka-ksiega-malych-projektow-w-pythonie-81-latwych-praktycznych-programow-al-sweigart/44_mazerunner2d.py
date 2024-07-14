"""Labirynt 2D, autor: Al Sweigart, al@inventwithpython.com
Poruszaj się po labiryncie starając się z niego wydostać. 
Pliki z labiryntami są generowane przez skrypt mazemakerrec.py.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, labirynt"""

import sys, os

# Stałe pliku z labiryntem:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'  # (!) Spróbuj zmienić tę wartość na '+' lub 'o'.
BLOCK = chr(9617)  # Znak 9617 to '░'.


def displayMaze(maze):
    # Wyświetl labirynt:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (exitx, exity):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()  # Wyświetl znak nowej linii po wyświetleniu danego wiersza.


print('''Labirynt 2D, autor: Al Sweigart, al@inventwithpython.com

(Pliki z labiryntami są generowane przez skrypt mazemakerrec.py)''')

# Pobierz od użytkownika nazwę pliku z labiryntem:
while True:
    print('Wpisz nazwę pliku z labiryntem (albo LISTA, albo KONIEC):')
    filename = input('> ')

    # Wyświetl listę wszystkich plików z labiryntami w bieżącym folderze:
    if filename.upper() == 'LISTA':
        print('Znalezione pliki z labiryntami:', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze') and
            fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'KONIEC':
        sys.exit()

    if os.path.exists(filename):
        break
    print('Nie znaleziono pliku o takiej nazwie', filename)

# Wgraj labirynt z pliku:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Błędny znak w kolumnie {}, wiersz {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None, 'W pliku z labiryntem nie ma startu.'
assert exitx != None and exity != None, 'W pliku z labiryntem nie ma wyjścia.'

while True:  # Główna pętla gry.
    displayMaze(maze)

    while True:  # Pobierz ruch gracza.
        print('                           W')
        print('Podaj kierunek lub KONIEC: ASD')
        move = input('> ').upper()

        if move == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        if move not in ['W', 'A', 'S', 'D']:
            print('Niepoprawny kierunek. Naciśnij jeden z następujących klawiszy:  W, A, S lub D.')
            continue

        # Sprawdź, czy gracz może ruszyć się w tym kierunku:
        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break

        print('Nie możesz ruszyć się w tym kierunku.')

    # Idź w tym kierunku, dopóki nie dojdziesz do rozwidlenia.
    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break  # Wyjdź z pętli, jeśli gracz uderzy w ścianę.
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break  # Wyjdź z pętli, jeśli gracz dojdzie do rozwidlenia.
    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break  # Wyjdź z pętli, jeśli gracz uderzy w ścianę.
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break  # Wyjdź z pętli, jeśli gracz dojdzie do rozwidlenia.
    elif move == 'A':
        while True:
            playerx -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx - 1, playery)] == WALL:
                break  # Wyjdź z pętli, jeśli gracz uderzy w ścianę.
            if (maze[(playerx, playery - 1)] == EMPTY
                or maze[(playerx, playery + 1)] == EMPTY):
                break  # Wyjdź z pętli, jeśli gracz dojdzie do rozwidlenia.
    elif move == 'D':
        while True:
            playerx += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx + 1, playery)] == WALL:
                break  # Wyjdź z pętli, jeśli gracz uderzy w ścianę.
            if (maze[(playerx, playery - 1)] == EMPTY
                or maze[(playerx, playery + 1)] == EMPTY):
                break  # Wyjdź z pętli, jeśli gracz dojdzie do rozwidlenia.

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print('Dotarłeś do wyjścia! Gratulacje!')
        print('Dziękujemy za grę!')
        sys.exit()

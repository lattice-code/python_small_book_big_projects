"""Labirynt 3D, autor: Al Sweigart, al@inventwithpython.com
Poruszaj się po labiryncie i spróbuj się z niego wydostać... w 3D!
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: bardzo długi, artystyczny, labirynt, gra"""

import copy, sys, os

# Deklaracja stałych:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # Znak 9617 to '░'.
NORTH = 'PÓŁNOC'
SOUTH = 'POŁUDNIE'
EAST = 'WSCHÓD'
WEST = 'ZACHÓD'


def wallStrToWallDict(wallStr):
    """Pobiera łańcuch znaków reprezentujący ścianę (taki jak ten zapisany 
    w słowniku ALL_OPEN lub CLOSED) i zwraca słownik
    z krotkami (x, y) jako kluczami i pojedynczymi znakami, które mają
    być narysowane w pozycji x, y."""
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wallDict[(x, y)] = character
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

# Łańcuchy znaków, które są wyświetlane na ekranie, to przekonwertowane obrazy
# zapisane w słownikach za pomocą funkcji wallStrToWallDict().
# Następnie tworzymy ścianę dla położenia gracza i strony, w którą gracz jest zwrócony,
# przez "wklejanie" słowników ściany do zsłowników CLOSED na słownik ścian
# w ALL_OPEN.

ALL_OPEN = wallStrToWallDict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
# Wywołanie funkcji strip() usuwa znak nowej linii
# na początku wielolinijkowego łańcucha znaków.

CLOSED = {}
CLOSED['A'] = wallStrToWallDict(r'''
_____
.....
.....
.....
_____'''.strip()) # Wklej do 6, 4.

CLOSED['B'] = wallStrToWallDict(r'''
.\.
..\
...
...
...
../
./.'''.strip()) # Wklej do 4, 3.

CLOSED['C'] = wallStrToWallDict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip()) # Wklej do 3, 1.

CLOSED['D'] = wallStrToWallDict(r'''
./.
/..
...
...
...
\..
.\.'''.strip()) # Wklej do 10, 3.

CLOSED['E'] = wallStrToWallDict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip()) # Wklej do 0, 0.

CLOSED['F'] = wallStrToWallDict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip()) # Wklej do 12, 0.

def displayWallDict(wallDict):
    """Wyświetla na ekranie słownik ściany,
    który został zwrócony przez funkcję wallStrToWallDict()."""
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK, end='')
        for x in range(wallDict['width']):
            wall = wallDict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)  # Wyświetl blok w nowej linii.
    print(BLOCK * (wallDict['width'] + 2))


def pasteWallDict(srcWallDict, dstWallDict, left, top):
    """Kopiuje słownik srcWallDict reprezentujący ścianę i wkleja na ścianę ze słownika dstWallDict,
     z przesunięciem na położenie zapisane w zmiennych left, top."""
    dstWallDict = copy.copy(dstWallDict)
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left, y + top)] = srcWallDict[(x, y)]
    return dstWallDict


def makeWallDict(maze, playerx, playery, playerDirection, exitx, exity):
    """Tworzy słownik przedstawiający ścianę na podstawie pozycji i kierunku gracza w labiryncie
    (który ma wyjście w pozycji exitx, exity) przez wklejenie
    słowników ścian na górze słownika ALL_OPEN, a następnie go zwraca."""

    # "Sekcje" A-F (które odpowiadają kierunkowi gracza)
    # określają, które ściany labiryntu sprawdzamy, by dowiedzieć się,
    # czy muszą być wklejone do tworzonego przez nas słownika przedstawiającego ściany.

    if playerDirection == NORTH:
        # Mapa sekcji do gracza @: 	       A 
        # (Gracz zwrócony na północ)       BCD 
        #                                  E@F
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if playerDirection == SOUTH:
        # Mapa sekcji względem gracza @:   F@E 
        # (Gracz zwrócony na południe)     DCB 
        #                                  A
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if playerDirection == EAST:
        # Mapa sekcji względem gracza @:   EB
        # (Gracz zwrócony na wschód)       @CA 
        #                                  FD
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if playerDirection == WEST:
        # Mapa sekcji względem gracza @:   DF
        # (Gracz zwrócony na zachód)       AC@ 
        #                                  BE
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, xOff, yOff in offsets:
        section[sec] = maze.get((playerx + xOff, playery + yOff), WALL)
        if (playerx + xOff, playery + yOff) == (exitx, exity):
            section[sec] = EXIT

    wallDict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wallDict = pasteWallDict(CLOSED[sec], wallDict,
                PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    # Jeśli trzeba, narysuj znak wyjścia:
    if section['C'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 7, 9)
    if section['E'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 0, 11)
    if section['F'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 13, 11)

    return wallDict


print('Labirynt 3D, autor: Al Sweigart, al@inventwithpython.com')
print('(Pliki z labiryntami są generowane przez skrypt mazemakerrec.py)')

# Pobierz od użytkownika nazwę pliku z labiryntem:
while True:
    print('Wpisz nazwę pliku z labiryntem (albo LISTA, albo KONIEC):')
    filename = input('> ')

    # List all the maze files in the current folder:
    if filename.upper() == 'LISTA':
        print('Znalezione pliki z labiryntami:', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze')
            and fileInCurrentFolder.endswith('.txt')):
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
px = None
py = None
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
            px, py = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert px != None and py != None, 'W pliku z labiryntem nie ma startu.'
assert exitx != None and exity != None, 'W pliku z labiryntem nie ma wyjścia.'
pDir = NORTH


while True:  # Główna pętla gry.
    displayWallDict(makeWallDict(maze, px, py, pDir, exitx, exity))

    while True: # Pobierz ruch gracza.
        print('Położenie ({}, {})  Kierunek: {}'.format(px, py, pDir))
        print('                   (W)')
        print('Podaj kierunek: (A) (D)  lub KONIEC.')
        move = input('> ').upper()

        if move == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
            and not move.startswith('T')):
            print('Niepoprawny kierunek. Naciśnij jeden z następujących klawiszy: F, L lub R (lub W, A, D).')
            continue

        # Przesuń gracza zgodnie z podanym ruchem:
        if move == 'F' or move == 'W':
            if pDir == NORTH and maze[(px, py - 1)] == EMPTY:
                py -= 1
                break
            if pDir == SOUTH and maze[(px, py + 1)] == EMPTY:
                py += 1
                break
            if pDir == EAST and maze[(px + 1, py)] == EMPTY:
                px += 1
                break
            if pDir == WEST and maze[(px - 1, py)] == EMPTY:
                px -= 1
                break
        elif move == 'L' or move == 'A':
            pDir = {NORTH: WEST, WEST: SOUTH,
                    SOUTH: EAST, EAST: NORTH}[pDir]
            break
        elif move == 'R' or move == 'D':
            pDir = {NORTH: EAST, EAST: SOUTH,
                    SOUTH: WEST, WEST: NORTH}[pDir]
            break
        elif move.startswith('T'):  # Kod ułatwiający wygraną: 'T x,y'.
            px, py = move.split()[1].split(',')
            px = int(px)
            py = int(py)
            break
        else:
            print('Nie możesz ruszyć się w tym kierunku.')

    if (px, py) == (exitx, exity):
        print('Dotarłeś do wyjścia! Gratulacje!')
        print('Dziękujemy za grę!')
        sys.exit()

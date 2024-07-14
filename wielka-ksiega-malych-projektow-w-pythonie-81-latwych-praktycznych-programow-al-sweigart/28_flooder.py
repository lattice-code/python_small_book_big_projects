"""Flooder, autor: Al Sweigart, al@inventwithpython.com
Kolorowa gra, w której starasz się wypełnić planszę jednym kolorem.
Ma tryb dla osób nierozróżniających kolorów.
Gra zainspirowana grą Flood It!.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, bext, gra"""

import random, sys

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować według instrukcji ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

# Deklaracja stałych:
BOARD_WIDTH = 16  # (!) Spróbuj zmienić tę wartość na 4 lub 40.
BOARD_HEIGHT = 14  # (!) Spróbuj zmienić tę wartość na 4 lub 20.
MOVES_PER_GAME = 20  # (!) Spróbuj zmienić tę wartość na 3 lub 300.

# Stałe dla różnych kształtów używanych w wersji dla osób z zaburzeniem rozpoznawania barw:
HEART     = chr(9829)  # Znak 9829 to '♥'.
DIAMOND   = chr(9830)  # Znak 9830 to '♦'.
SPADE     = chr(9824)  # Znak 9824 to '♠'.
CLUB      = chr(9827)  # Znak 9827 to '♣'.
BALL      = chr(9679)  # Znak 9679 to '●'.
TRIANGLE  = chr(9650)  # Znak 9650 to '▲'.

BLOCK     = chr(9608)  # Znak 9608 to '█'.
LEFTRIGHT = chr(9472)  # Znak 9472 to '─'.
UPDOWN    = chr(9474)  # Znak 9474 to '│'.
DOWNRIGHT = chr(9484)  # Znak 9484 to '┌'.
DOWNLEFT  = chr(9488)  # Znak 9488 to '┐'.
UPRIGHT   = chr(9492)  # Znak 9492 to '└'.
UPLEFT    = chr(9496)  # Znak 9496 to '┘'.
# Lista kodów chr() jest dostępna na stronie https://inventwithpython.com/chr.

# Wszystkie kolory/kształty używane na planszy:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
              3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'tryb kolorów'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'tryb kształtów'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, autor: Al Sweigart, al@inventwithpython.com

Ustaw kolor/kształt płytki znajdującej się w lewym górnym rogu,
która wypełnia wszystkie przylegające płytki o tym samym kolorze/tego samego kształtu.
Postaraj się, by plansza była wypełniona tym samym kolorem/kształtem.''')

    print('Czy chcesz zagrać w trybie z kształtami? T/N')
    response = input('> ')
    if response.upper().startswith('T'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:  # Główna pętla programu.
        displayBoard(gameBoard, displayMode)

        print('Ruchy w lewo:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('Wygrałeś!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('Nie masz już więcej ruchów!')
            break


def getNewBoard():
    """Zwróć słownik nowej planszy Flood It."""

    # Klucze to krotki (x, y), wartości to płytki w tej pozycji.
    board = {}

    # Wypełnij planszę losowymi kolorami:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # Zmień kolor kilku płytek na ten sam kolor, jaki mają co ich sąsiedzi.
    # To tworzy grupę tego samego koloru/kształtu.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def displayBoard(board, displayMode):
    """Wyświetl planszę na ekranie."""
    bext.fg('white')
    # Wyświetl górną krawędź planszy:
    print(DOWNRIGHT + (LEFTRIGHT * BOARD_WIDTH) + DOWNLEFT)

    # Wyświetl każdy wiersz:
    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        if y == 0:  # Pierwszy wiersz zaczyna się od '>'.
            print('>', end='')
        else:  # Później wiersze zaczynają się od białej pionowej linii.
            print(UPDOWN, end='')

        # Wyświetl każdą płytkę w tym wierszu:
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if displayMode == COLOR_MODE:
                print(BLOCK, end='')
            elif displayMode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UPDOWN)  # Wiersze kończą się białą pionową linią.
    # Wyświetl dolną krawędź planszy:
    print(UPRIGHT + (LEFTRIGHT * BOARD_WIDTH) + UPLEFT)


def askForPlayerMove(displayMode):
    """Pozwól graczowi wybrać kolor płytki w lewym górnym rogu."""
    while True:
        bext.fg('white')
        print('Wybierz jeden kolor ', end='')

        if displayMode == COLOR_MODE:
            bext.fg('red')
            print('(C)zerwony ', end='')
            bext.fg('green')
            print('(Z)ielony ', end='')
            bext.fg('blue')
            print('(N)iebieski ', end='')
            bext.fg('yellow')
            print('(Ż)ółty ', end='')
            bext.fg('cyan')
            print('(T)urkusowy ', end='')
            bext.fg('purple')
            print('(F)ioletowy ', end='')
        elif displayMode == SHAPE_MODE:
            bext.fg('red')
            print('(S)erce, ', end='')
            bext.fg('green')
            print('(T)rójkąt, ', end='')
            bext.fg('blue')
            print('(D)iament, ', end='')
            bext.fg('yellow')
            print('(P)iłka, ', end='')
            bext.fg('cyan')
            print('(K)oniczyna, ', end='')
            bext.fg('purple')
            print('(L)istek, ', end='')
        bext.fg('white')
        print('lub KONIEC:')
        response = input('> ').upper()
        if response == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()
        if displayMode == COLOR_MODE and response in tuple('CZNŻTF'):
            # Zwróć numer typu płytki w zależności od odpowiedzi:
            return {'C': 0, 'Z': 1, 'N': 2,
                'Ż': 3, 'T': 4, 'F': 5}[response]
        if displayMode == SHAPE_MODE and response in tuple('STDPKL'):
            # Zwróć numer typu płytki w zależności od odpowiedzi:
            return {'S': 0, 'T': 1, 'D':2,
                'P': 3, 'K': 4, 'L': 5}[response]


def changeTile(tileType, board, x, y, charToChange=None):
    """Zmień kolor/kształt płytki za pomocą rekurencyjnego algorytmu 
    flood fill."""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return  # Przypadek podstawowy : Już ta sama płytka.

    board[(x, y)] = tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        # Przypadek rekurencyjny zmień płytkę sąsiadującą z lewej strony:
        changeTile(tileType, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        # Przypadek rekurencyjny: zmień płytkę sąsiadującą z góry:
        changeTile(tileType, board, x, y - 1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        # Przypadek rekurencyjny: zmień płytkę sąsiadującą z prawej strony:
        changeTile(tileType, board, x + 1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        # Przypadek rekurencyjny: zmień płytkę sąsiadującą z dołu:
        changeTile(tileType, board, x, y + 1, charToChange)


def hasWon(board):
    """Zwróć wartość True, jeśli cała plansza jest wypełniona jednym kolorem/kształtem."""
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()

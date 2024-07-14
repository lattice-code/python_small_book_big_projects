"""Przesuwanka, autor: Al Sweigart, al@inventwithpython.com
Przesuwaj numerowane płytki, aż ułożysz je w kolejności.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, łamigłówka"""

import random, sys

BLANK = '  '  # Uwaga: Ten łańcuch znaków to dwie spacje, nie jedna.


def main():
    print('''Przesuwanka, autor: Al Sweigart, al@inventwithpython.com

    Przesuwaj płytki za pomocą klawiszy WASD,
    tak by ułożyć je w kolejności:
           1  2  3  4
           5  6  7  8
           9 10 11 12
          13 14 15   ''')
    input('Naciśnij Enter, aby kontynuować...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('Wygrałeś!')
            sys.exit()


def getNewBoard():
    """Zwraca listę list, która przedstawia nową układankę."""
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
            ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]


def displayBoard(board):
    """Wyświetla daną planszę na ekranie."""
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    boardToDraw = """
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
""".format(*labels)
    print(boardToDraw)


def findBlankSpace(board):
    """Zwraca krotkę (x, y) z pozycją pustego miejsca."""
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)


def askForPlayerMove(board):
    """Poproś gracza o wybranie płytki, którą chce przesunąć."""
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blanky != 3 else ' '
    a = 'A' if blankx != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print('                          ({})'.format(w))
        print('Wpisz WASD (lub KONIEC): ({}) ({}) ({})'.format(a, s, d))

        response = input('> ').upper()
        if response == 'KONIEC':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response


def makeMove(board, move):
    """Wykonaj dany ruch na danej planszy."""
    # Uwaga: Ta funkcja zakłada, że podany ruch jest odpowiedni.
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]


def makeRandomMove(board):
    """Wykonuje ruch w losowym kierunku."""
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 3:
        validMoves.append('W')
    if blankx != 3:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))


def getNewPuzzle(moves=200):
    """Utwórz nową planszę przez wykonanie losowych przesunięć na ułożonej planszy."""
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


# Jeśli program został uruchomiony (a nie zaimportowany), uruchom grę:
if __name__ == '__main__':
    main()

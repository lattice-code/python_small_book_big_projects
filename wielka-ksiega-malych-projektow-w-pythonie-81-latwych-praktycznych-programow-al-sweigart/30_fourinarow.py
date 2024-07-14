"""Czwórki, autor: Al Sweigart, al@inventwithpython.com
Program podobny do gry planszowej Czwórki, w której celem każdego gracza jest ułożenie 4 żetonów w rzędzie.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, gra planszowa, dla dwóch graczy"""

import sys

# Stałe do wyświetlania planszy:
EMPTY_SPACE = '.'  # Kropkę łatwiej policzyć niż spację.
PLAYER_X = 'X'
PLAYER_O = 'O'

# Uwaga: Zaktualizuj funkcję displayBoard() i stałą COLUMN_LABELS, jeśli stała BOARD_WIDTH zostanie zmieniona.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    print("""Czwórki, autor: Al Sweigart, al@inventwithpython.com

Dwóch graczy umieszcza żetony w jednej z siedmiu kolumn,
próbując ustawić cztery żetony w rzędzie: poziomo, pionowo lub po skosie.
""")

    # Ustawienie nowej gry:
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:  # Kolej danego gracza.
        # Wyświetl planszę i pobierz ruch gracza:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # Sprawdź, czy gracz wygrał lub czy jest remis:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # Wyświetl planszę po raz ostatni.
            print('Gracz ' + playerTurn + ' wygrał!')
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)  # Wyświetl planszę po raz ostatni.
            print('Remis!')
            sys.exit()

        # Zmień na drugiego gracza:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


def getNewBoard():
    """Zwraca słownik, który przedstawia planszę gry.

    Klucze to krotki (columnIndex, rowIndex) dwóch liczb całkowitych,
    a wartości to łańcuchy znaków 'X', 'O' lub '.' (puste pola)."""
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board


def displayBoard(board):
    """Wyświetla planszę i żetony na ekranie."""

    '''Przygotuj listę, by przekazać ją do metody format() dla
    szablonu planszy. Ta lista przechowuje wszystkie żetony na planszy(i puste pola)
    od lewej do prawej, od góry do dołu.'''
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # Wyświetl planszę:
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tileChars))


def askForPlayerMove(playerTile, board):
    """Pozwala graczowi wybrać kolumnę na planszy i umieścić w niej żeton.

    Zwraca krotkę (column, row), gdzie zostanie umieszczony żeton."""
    while True:  # Pytaj cały czas gracza, dopóki nie poda odpowiedniego ruchu.
        print('Gracz {}, podaje numer kolumny lub KONIEC:'.format(playerTile))
        response = input('> ').upper().strip()

        if response == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Wpisz liczbę od 1 do {}.'.format(BOARD_WIDTH))
            continue  # Ponownie poproś gracza o podanie ruchu.

        columnIndex = int(response) - 1  # -1 dla indeksów zaczynających się od 0.

        # Jeśli kolumna jest pełna, zapytaj gracza o ruch jeszcze raz:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('Ta kolumna jest pełna, wybierz inną.')
            continue  # Ponownie poproś gracza o podanie ruchu.

        # Zaczynając od dołu, znajdź pierwsze puste pole.
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    """Zwraca wartość True, jeśli na planszy nie ma już wolnych pól,
    w przeciwnym razie zwraca wartość False."""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # Znaleziono puste pole, więc zwróć False.
    return True  # Wszystkie pola są pełne.


def isWinner(playerTile, board):
    """Zwraca wartość True, jeśli dany gracz ma cztery żetony w rzędzie,
    w przeciwnym razie zwraca wartość False."""

    # Przejdź przez całą planszę, aby sprawdzić czy są cztery żetony w rzędzie:
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # Sprawdź pod kątem czterech żetonów ułożonych poziomo, idąc w prawo:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Sprawdź pod kątem czterech żetonów ułożonych pionowo, idąc w dół:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Sprawdź pod kątem czterech żetonów ułożonych po skosie, od prawej do dołu:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            # Sprawdź pod kątem czterech żetonów ułożonych po skosie, od lewej do dołu:
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()

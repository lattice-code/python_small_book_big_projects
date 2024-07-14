"""Kółko i krzyżyk, autor: Al Sweigart, al@inventwithpython.com
Klasyczna gra planszowa.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, gra planszowa, gra, dla dwóch graczy"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # Stałe łańcuchy znaków.


def main():
    print('Witaj w grze kółko i krzyżyk!')
    gameBoard = getBlankBoard()  # Stwórz słownik z planszą.
    currentPlayer, nextPlayer = X, O  # X zaczyna, a potem O.

    while True:  # Główna pętla gry.
        # Wyświetl planszę na ekranie:
        print(getBoardStr(gameBoard))

        # Pytaj gracza, dopóki nie poda liczby od 1 do 9:
        move = None
        while not isValidSpace(gameBoard, move):
            print('Gdzie wpisać {}? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)  # Wykonaj ruch.

        # Sprawdź, czy gra się skończyła:
        if isWinner(gameBoard, currentPlayer):  # Sprawdź kto wygrał.
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' wygrał grę!')
            break
        elif isBoardFull(gameBoard):  # Sprawdź, czy jest remis.
            print(getBoardStr(gameBoard))
            print('Gra kończy się remisem!')
            break
        # Teraz kolej na drugiego gracza:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Dziękujemy za grę!')


def getBlankBoard():
    """Tworzy nową, czystą planszę do gry kółko i krzyżyk."""
    # Ponumerowane pola planszy: 1|2|3
    #                            -+-+-
    #                            4|5|6
    #                            -+-+-
    #                            7|8|9
    # Klucze słownika to liczby od 1 do 9, a jego wartości to X, O lub BLANK (puste):
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # Na początku wszystkie pola są puste.
    return board


def getBoardStr(board):
    """Zwraca planszę w postaci łańcucha znaków."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    """Zwraca wartość True, jeśli podana liczba podana przez jest poprawna,
    a pole o tym numerze jest puste."""
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    """Zwraca wartość True, jeśli jeden z graczy wygrał."""
    # Użyto tutaj krótszych nazw zmiennych, by kod był czytelniejszy:
    b, p = board, player
    # Sprawdź 3 symbole we wszystkich 3 rzędach, 3 kolumnach i 2 przekątnych.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Górny wiersz
            (b['4'] == b['5'] == b['6'] == p) or  # Środkowy wiersz
            (b['7'] == b['8'] == b['9'] == p) or  # Dolny wiersz
            (b['1'] == b['4'] == b['7'] == p) or  # Lewa kolumna
            (b['2'] == b['5'] == b['8'] == p) or  # Środkowa kolumna
            (b['3'] == b['6'] == b['9'] == p) or  # Prawa kolumna
            (b['3'] == b['5'] == b['7'] == p) or  # Przekątna
            (b['1'] == b['5'] == b['9'] == p))    # Przekątna

def isBoardFull(board):
    """Zwraca wartość True, jeśli każde pole na planszy zostało już wypełnione."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # Jeśli któreś z pól jest puste, zwróć wartość False.
    return True  # Żadne pole nie jest puste, więc zwróć wartość True.


def updateBoard(board, space, mark):
    """Wstawia podany symbol w danym polu na planszy."""
    board[space] = mark


if __name__ == '__main__':
    main()  # Wywołaj funkcję main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.

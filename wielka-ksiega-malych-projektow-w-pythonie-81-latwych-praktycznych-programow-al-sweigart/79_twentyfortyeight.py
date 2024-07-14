"""2048, autor: Al Sweigart, al@inventwithpython.com
Przesuwanka, która polega na łączeniu ze sobą liczb, tak by dawały większą wartość.
Program zainspirowany grą 2048 autorstwa Gabriele'a Cirulli, która jest wersją gry 1024 
stworzonej przez Veewo Studios, która z kolei jest inspirowana grą Threes!.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/2048_(gra_komputerowa).
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, łamigłówka"""

import random, sys

# Deklaracja stałych:
BLANK = ''  # Wartość przedstawiająca puste miejsce na planszy.


def main():
    print('''2048, autor: Al Sweigart, al@inventwithpython.com

Przesuwaj płytki na planszy we wszystkich czterech kierunkach.
Płytki z takimi samymi liczbami połączą się w jedną większą liczbę. 
Po każdym ruchu zostanie dodana nowa płytka z liczbą 2. Wygrasz, jeśli uda Ci się stworzyć płytkę z liczbą 2048.
Przegrasz, jeśli plansza się zapełni, zanim uzyskasz liczbę 2048.''')
    input('Naciśnij Enter, aby rozpocząć...')

    gameBoard = getNewBoard()

    while True:  # Główna pętla gry.
        drawBoard(gameBoard)
        print('Wynik:', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Koniec - Dziękujemy za grę!')
            sys.exit()


def getNewBoard():
    """Zwraca nową strukturę danych, która przedstawia planszę.

    Jest to słownik z kluczami w postaci krotek (x, y), wartością jest liczba
    na płytce w tym miejscu. Płytka to albo potęga dwójki, albo BLANK (pusta).
    Współrzędne rozkładają się w następujący sposób:
       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""

    newBoard = {}  # Zawiera dane planszy, które zostaną zwrócone przez tę funkcję.
    # Przejdź przez każde miejsce na planszy i ustaw wszystkie płytki na puste:
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # Wybierz dwa losowe miejsca dla dwóch początkowych płytek z 2:
    startingTwosPlaced = 0  # Liczba wybranych płytek początkowych.
    while startingTwosPlaced < 2:  # Powtórz w przypadku powtórzenia się miejsca.
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # Upewnij się, że losowo wybrane miejsce nie jest już zajęte:
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1

    return newBoard


def drawBoard(board):
    """Rysuje planszę na ekranie."""

    # Przejdź przez każde możliwe miejsce, od lewej do prawej, z góry na dół
    # i stwórz listę oznaczeń każdego miejsca.
    labels = []  # Lista łańcuchów znaków dla pustej płytki lub płytki z listą.
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]  # Pobierz płytkę w tym miejscu.
            # Upewnij się, że oznaczenie ma 5 znaków:
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    # Zastąp nawiasy klamrowe {} oznaczeniem danej płytki:
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def getScore(board):
    """Zwraca sumę wszystkich płytek na planszy."""
    score = 0
    # Przejdź przez każde miejsce na planszy i zsumuj płytki:
    for x in range(4):
        for y in range(4):
            # Dodawaj tylko płytki, które nie są puste:
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combineTilesInColumn(column):
    """Kolumna jest listą czterech płytek. Pierwszy element listy (indeks 0) to płytka
    znajdująca się na samym dole kolumny. Płytki są ściągane i łączone, 
    jeśli mają takie same liczby. Na przykład wyrażenie combineTilesInColumn([2, BLANK, 2, BLANK])
    zwraca [4, BLANK, BLANK, BLANK]."""

    # Skopiuj tylko liczby (pomiń puste) z kolumn do listy combinedTiles.
    combinedTiles = []  # Lista niepustych płytek w kolumnie.
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])

    # Dodawaj puste płytki, dopóki nie będzie 4 płytek:
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    # Połącz płytki, jeśli płytka u góry ma taką samą liczbę, i podwój tę liczbę:
    for i in range(3):  # Pomiń indeks 3: to miejsce u samej góry.
        if combinedTiles[i] == combinedTiles[i + 1]:
            combinedTiles[i] *= 2  # Podwój liczbę na płytce.
            # Przesuń płytki z góry w dół o jedno miejsce:
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK  # Miejsce na samej górze jest zawsze puste.
    return combinedTiles


def makeMove(board, move):
    """Obsługuje ruchy na planszy.

    Argument move to ruch 'W', 'A', 'S' lub 'D'.
    Funkcja zwraca planszę po wykonanym ruchu."""

    # Plansza jest podzielona na cztery kolumny, 
    # które różnią się w zależności od kierunku ruchu:
    if move == 'W':
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]

    # Struktura danych planszy po wykonaniu ruchu:
    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:  # Przejdź w pętli przez wszystkie 4 kolumny.
        # Pobierz płytki z tej kolumny (Pierwsza płytka w liście
        # to płytka znajdująca się na dole kolumny):
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]

        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        # Utwórz kolumnę i połącz w niej płytki:
        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)

        # Ustaw nową strukturę danych planszy z połączonymi płytkami:
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove


def askForPlayerMove():
    """Prosi gracza o podanie kierunku następnego ruchu (lub zakończenie gry).

    Upewnia się, że gracz podał poprawny ruch: 'W', 'A', 'S' lub 'D'."""
    print('Podaj ruch: (WASD lub K to koniec)')
    while True:  # Pytaj gracza, dopóki nie poda poprawnego ruchu.
        move = input('> ').upper()
        if move == 'K':
            # Zakończ program:
            print('Dziękujemy za grę!')
            sys.exit()

        # Albo zwróć poprawny ruch, albo zapytaj gracza jeszcze raz:
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Wpisz jedną z następujących liter: "W", "A", "S", "D" lub "K".')


def addTwoToBoard(board):
    """Dodaje losowo 2 nowe płytki na planszy."""
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return  # Wyjdź po odnalezieniu jednej pustej płytki.


def isFull(board):
    """Zwraca True, jeśli struktura danych planszy nie ma pustych miejsc."""
    # Przejdź przez każde miejsce na planszy:
    for x in range(4):
        for y in range(4):
            # Jeśli miejsce jest puste, zwróć False:
            if board[(x, y)] == BLANK:
                return False
    return True  # Żadne pole nie jest puste, więc zwróć True.


# Jeśli ten program został uruchomiony (a nie zaimportowany), uruchom grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

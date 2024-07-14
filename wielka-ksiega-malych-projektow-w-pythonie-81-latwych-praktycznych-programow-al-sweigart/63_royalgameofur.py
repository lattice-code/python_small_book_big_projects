"""Królewska gra z Ur, autor: Al Sweigart, al@inventwithpython.com
Ta gra planszowa ma 5000 lat i pochodzi z Mezopotamii. Dwóch graczy próbuje
strącić pionki swojego przeciwnika, pokonując drogę do celu.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Kr%C3%B3lewska_gra_z_Ur.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra planszowa, gra, dla dwóch graczy
"""

import random, sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

# Deklaracja stałych dla oznaczeń pól:
X_HOME = 'x_baza'
O_HOME = 'o_baza'
X_GOAL = 'x_meta'
O_GOAL = 'o_meta'

# Pola od lewej do prawej, od góry do dołu:
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'BefghijklmnopstM'  # (B to Baza, M to Meta).
O_TRACK = 'BabcdijklmnopqrM'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = """
                   {}           {}
                   Baza              Meta
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Baza              Meta
                   {}           {}
"""


def main():
    print('''Królewska gra z Ur, autor: Al Sweigart

Gra, która ma 5000 lat. Dwóch graczy musi przeprowadzić swoje pionki
z bazy do celu. W swojej rundzie rzucasz czterema monetami
i przesuwasz swój pionek o tyle pól, ile wypadło reszek. 

Gra to wyścigi; gracz, który jako pierwszy doprowadzi wszystkie siedem pionków
do bazy, wygrywa. W tym celu pionki muszą pokonać drogę między startem
a metą:

            X Baza      X Meta
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Baza      O Meta

Jeśli wylądujesz na polu znajdującym się w środkowej części, na którym stoi już pionek przeciwnika,
pionek przeciwnika wraca do bazy. Pola z kwiatkami dają dodatkowy rzut monetami. Pionki stojące
na środkowym polu z kwiatkiem są bezpieczne i nie mogą być odesłane do bazy.''')
    input('Naciśnij Enter, aby rozpocząć...')

    gameBoard = getNewBoard()
    turn = O_PLAYER
    while True:  # Główna pętla gry.
        # Przypisywanie wartości kilku zmiennym dla bieżącej rundy:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponentHome = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponentHome = X_HOME

        displayBoard(gameBoard)

        input('Teraz kolej: ' + turn + '. Naciśnij Enter, by rzucić monetami...')

        flipTally = 0
        print('Wyrzucono: ', end='')
        for i in range(4):  # Rzuć czterema monetami.
            result = random.randint(0, 1)
            if result == 0:
                print('T', end='')  # Orzeł.
            else:
                print('H', end='')  # Reszka.
            if i != 3:
                print('-', end='')  # Wyświetl separator.
            flipTally += result
        print('  ', end='')

        if flipTally == 0:
            input('Tracisz kolejkę. Naciśnij Enter, by kontynuować...')
            turn = opponent  # Zmień kolejkę na drugiego gracza.
            continue

        # Poproś gracza o podanie swojego ruchu:
        validMoves = getValidMoves(gameBoard, turn, flipTally)

        if validMoves == []:
            print('Nie ma możliwości ruchu, więc tracisz kolejkę.')
            input('Naciśnij Enter, by kontynuować...')
            turn = opponent  # Zmień kolejkę na drugiego gracza.
            continue

        while True:
            print('Wybierz', flipTally, 'pola: ', end='')
            print(' '.join(validMoves) + ' koniec')
            move = input('> ').lower()

            if move == 'koniec':
                print('Dziękujemy za grę!')
                sys.exit()
            if move in validMoves:
                break  # Wyjdź z pętli, gdy gracz poda poprawny ruch.

            print('Ten ruch jest niepoprawny.')

        # Wykonaj wybrany ruch na planszy:
        if move == 'baza':
            # Odejmij pionki od liczby pionków w bazie, jeśli grasz pionkiem z bazy:
            gameBoard[home] -= 1
            nextTrackSpaceIndex = flipTally
        else:
            gameBoard[move] = EMPTY  # Ustaw pole, z którego rusza pionek, na puste.
            nextTrackSpaceIndex = track.index(move) + flipTally

        movingOntoGoal = nextTrackSpaceIndex == len(track) - 1
        if movingOntoGoal:
            gameBoard[goal] += 1
            # Sprawdź, czy gracz wygrał:
            if gameBoard[goal] == 7:
                displayBoard(gameBoard)
                print(turn, 'wygrał grę!')
                print('Dziękujemy za grę!')
                sys.exit()
        else:
            nextBoardSpace = track[nextTrackSpaceIndex]
            # Sprawdź, czy na danym polu stoi pionek przeciwnika:
            if gameBoard[nextBoardSpace] == opponent:
                gameBoard[opponentHome] += 1

            # Ustaw pionek na polu docelowym:
            gameBoard[nextBoardSpace] = turn

        # Sprawdź, czy gracz wylądował na polu z kwiatkiem i może rzucać jeszcze raz:
        if nextBoardSpace in FLOWER_SPACES:
            print(turn, 'wylądował na polu z kwiatkiem i otrzymuje dodatkowy rzut.')
            input('Naciśnij Enter, by kontynuować...')
        else:
            turn = opponent  # Zmień kolejkę na drugiego gracza.

def getNewBoard():
    """
    Zwraca słownik reprezentujący stan planszy. 
    Klucze to tekstowe oznaczenia pól, a wartości to stałe X_PLAYER,
    O_PLAYER lub EMPTY. Istnieją również zmienne przechowujące liczbę pionków 
     w bazie i na mecie dla obu graczy.
    """
    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    # Na początku gry ustaw wszystkie pola na puste:
    for spaceLabel in ALL_SPACES:
        board[spaceLabel] = EMPTY
    return board


def displayBoard(board):
    """Wyświetla planszę na ekranie."""
    # "Wyczyść" ekran przez wyświetlenie tylu znaków nowej linii,
    # by poprzednia plansza nie była już widoczna:
    print('\n' * 60)

    xHomeTokens = ('X' * board[X_HOME]).ljust(7, '.')
    xGoalTokens = ('X' * board[X_GOAL]).ljust(7, '.')
    oHomeTokens = ('O' * board[O_HOME]).ljust(7, '.')
    oGoalTokens = ('O' * board[O_GOAL]).ljust(7, '.')

    # Dodaj łańcuchy znaków, które powinny wypełnić zmienną BOARD_TEMPLATE,
    # przedstawiającą planszę, idąc od lewej do prawej, z góry na dół.
    spaces = []
    spaces.append(xHomeTokens)
    spaces.append(xGoalTokens)
    for spaceLabel in ALL_SPACES:
        spaces.append(board[spaceLabel])
    spaces.append(oHomeTokens)
    spaces.append(oGoalTokens)

    print(BOARD_TEMPLATE.format(*spaces))


def getValidMoves(board, player, flipTally):
    validMoves = []  # Zawiera pola z pionkami, które mogą wykonać ruch.
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    # Sprawdź, czy gracz może ruszyć pionkiem z bazy:
    if board[home] > 0 and board[track[flipTally]] == EMPTY:
        validMoves.append('baza')

    # Sprawdź, na których polach stoją pionki, które gracz może strącić:
    for trackSpaceIndex, space in enumerate(track):
        if space == 'B' or space == 'M' or board[space] != player:
            continue
        nextTrackSpaceIndex = trackSpaceIndex + flipTally
        if nextTrackSpaceIndex >= len(track):
            # Musisz wyrzucić dokładną liczbę pól dzielących Cię od mety,
            # w przecwinym razie nie możesz tam pójść.
            continue
        else:
            nextBoardSpaceKey = track[nextTrackSpaceIndex]
            if nextBoardSpaceKey == 'M':
                # Ten pionek może zejść z planszy:
                validMoves.append(space)
                continue
        if board[nextBoardSpaceKey] in (EMPTY, opponent):
            # Jeśli następnyme polem jest, to chronione pole z kwiatkiem, 
            # możesz wykonać ruch tylko wtedy, gdy jest puste:
            if nextBoardSpaceKey == 'l' and board['l'] == opponent:
                continue  # Pomiń ten ruch, pole jest chronione.
            validMoves.append(space)

    return validMoves


if __name__ == '__main__':
    main()

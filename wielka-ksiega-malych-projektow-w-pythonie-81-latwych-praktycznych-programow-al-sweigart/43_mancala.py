"""Mankala, autor: Al Sweigart, al@inventwithpython.com
Starożytna gra w sianie ziarna.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra planszowa, gra, dla dwóch graczy"""

import sys

# Krotki z dołkami graczy:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

# Słownik, gdzie klucze to dołki, a wartości to przeciwne do nich dołki:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                   'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                   'K': 'E', 'L': 'F'}

# Słownik, gdzie klucze to dołki, a wartości to kolejny dołek:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# Oznaczenie każdego dołka w kolejności przeciwnej do ruchu wskazówek zegara, zaczynając od A:
PIT_LABELS = 'ABCDEF1LKJIHG2'

# Liczba ziaren na początku nowej gry:
STARTING_NUMBER_OF_SEEDS = 4  # (!) Spróbuj zmienić tę wartość na 1 lub 10.


def main():
    print('''Mankala, autor: Al Sweigart, al@inventwithpython.com

Starożytna gra w sianie ziarna dla dwóch graczy. Weź ziarna z dołka po Twojej stronie planszy 
i umieść po jednym w każdym kolejnym dołku, idąc przeciwnie do ruchu wskazówek zegara, 
i omijając wgłębienia przeciwnika. Jeśli Twoje ostatnie ziarno trafi do Twojej pustej dziury, 
to przenieś tam ziarna z wgłębienia leżącego naprzeciwko. 
Celem gry jest zebranie jak największej liczby ziaren w swoim magazynie (składzie) z boku planszy.
Jeśli umieścisz ostatnie ziarno w swoim magazynie, gdzie są już inne ziarna, zyskujesz dodatkowy ruch.

Gra się kończy w momencie, gdy wszystkie dołki jednego z graczy są puste. 
Drugi gracz zabiera ziarna, które zostały do swojego magazynu.
Wygrywa gracz z większą liczbą ziaren.

Więcej informacji na stronie https://pl.wikipedia.org/wiki/Mankala.
''')
    input('Naciśnij Enter, aby ropocząć...')

    gameBoard = getNewBoard()
    playerTurn = '1'  # Gracz nr 1 zaczyna.

    while True:  # Obsługa ruchu danego gracza.
        # "Wyczyść" ekran przez wyświetlenie wielu znaków nowej linii,
        # by stara plansza nie była już widoczna.
        print('\n' * 60)
        # Wyświetl planszę i pobierz ruch gracza:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)

        # Wykonaj ruch gracza:
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        # Sprawdź, czy gra się skończyła i czy dany gracz wygrał:
        winner = checkForWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)  # Wyświetl planszę ostatni raz.
            print('Gracz ' + winner + ' wygrał!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)  # Wyświetl planszę ostatni raz.
            print('Remis!')
            sys.exit()


def getNewBoard():
    """Zwraca słownik przedstawiający planszę mankali na początku gry:
    4 ziarna w każdym dołku i 0 w magazynach."""

    # Lukier składniowy - użycie krótszej nazwy zmiennej:
    s = STARTING_NUMBER_OF_SEEDS

    # Utworzenie struktury danych dla planszy. W magazynach nie
    # ma ziaren, a w dołkach jest początkowa liczba ziaren:
    return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s,
            'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


def displayBoard(board):
    """Wyświetla planszę gry w postaci grafiki ze znaków ASCII
    w oparciu o słownik, w którym zapisany jest stan planszy."""

    seedAmounts = []
    # Ten łańcuch znaków 'GHIJKL21ABCDEF' to kolejność dołków
    # od lwej do prawej i z góry na dół:
    for pit in 'GHIJKL21ABCDEF':
        numSeedsInThisPit = str(board[pit]).rjust(2)
        seedAmounts.append(numSeedsInThisPit)

    print("""
+------+------+--<<<<<-Gracz 2----+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
K  {}  +------+------+------+------+------+------+  {}  K
Ł      |A     |B     |C     |D     |E     |F     |      Ł
A      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      A
D      |      |      |      |      |      |      |      D
+------+------+------+-Gracz 1->>>>>-----+------+------+

""".format(*seedAmounts))


def askForPlayerMove(playerTurn, board):
    """Pyta gracza o wybór dołka po jego stronie planszy,
    z którego chce wziąć ziarna do rozsiania. Zwraca oznaczenie wybranego dołka
    w postaci wielkiej litery."""

    while True:  # Pytaj gracza, dopóki nie poda ruchu w odpowiednim formacie.
        # Poproś gracza o podanie dołka po jego stronie planszy:
        if playerTurn == '1':
            print('Graczu 1, wybierz: A-F (lub KONIEC)')
        elif playerTurn == '2':
            print('Graczu 2, wybierz: G-L (lub KONIEC)')
        response = input('> ').upper().strip()

        # Sprawdź, czy gracz nie chce zakończyć gry:
        if response == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        # Upewnij się, że został wybrany poprawny dołek:
        if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
            playerTurn == '2' and response not in PLAYER_2_PITS
        ):
            print('Proszę, wybierz literę po Twojej stronie planszy.')
            continue  # Ponownie poproś gracza o podanie ruchu.
        if board.get(response) == 0:
            print('Proszę, wybierz dołek, który nie jest pusty.')
            continue  # Ponownie poproś gracza o podanie ruchu.
        return response


def makeMove(board, playerTurn, pit):
    """Wprowadza zmiany w strukturze danych reprezentujących planszę, by gracz 1 lub 2
    mógł wybrać dołek, z którego chce siać ziarna. Zwraca
    '1' lub '2' w zależności od tego, który gracz ma ruch."""

    seedsToSow = board[pit]  # Pobierz liczbę ziaren z wybranego dołka.
    board[pit] = 0  # Wyczyść wybrany dołek.

    while seedsToSow > 0:  # Siej, dopóki są ziarna.
        pit = NEXT_PIT[pit]  # Przejdź do kolejnego dołka.
        if (playerTurn == '1' and pit == '2') or (
            playerTurn == '2' and pit == '1'
        ):
            continue  # Omiń magazyn przeciwnika.
        board[pit] += 1
        seedsToSow -= 1

    # Jeśli ostatnie ziarno wpadło do magazynu gracza, wykonuje on ruch jeszcze raz.
    if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
        # Ostatnie ziarno wpadło do magazynu; gracz wykonuje ruch jeszcze raz.
        return playerTurn

    # Sprawdź, czy ostatnie ziarno wylądowało w pustym dołku; weź ziarna z dołka naprzeciwko.
    if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['1'] += board[oppositePit]
        board[oppositePit] = 0
    elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['2'] += board[oppositePit]
        board[oppositePit] = 0

    # Zwróć drugiego gracza jako tego, którego kolej będzie teraz :
    if playerTurn == '1':
        return '2'
    elif playerTurn == '2':
        return '1'


def checkForWinner(board):
    """Sprawdza planszę i zwraca '1' albo '2', jeśli jest zwycięzca,
    lub 'remis', lub 'brak zwycięzcy', jeśli nikt nie wygrał. Gra kończy się, 
    gdy dołki jednego z graczy są puste; drugi gracz zabiera pozostałe ziarna
    do swojego magazynu. Wygrywa ten, kto ma najwięcej ziaren."""

    player1Total = board['A'] + board['B'] + board['C']
    player1Total += board['D'] + board['E'] + board['F']
    player2Total = board['G'] + board['H'] + board['I']
    player2Total += board['J'] + board['K'] + board['L']

    if player1Total == 0:
        # Gracz 2 otrzymuje wszystkie pozostałe po jego stronie ziarna:
        board['2'] += player2Total
        for pit in PLAYER_2_PITS:
            board[pit] = 0  # Ustaw wszystkie dołki na 0.
    elif player2Total == 0:
        # Gracz 1 otrzymuje wszystkie pozostałe po jego stronie ziarna:
        board['1'] += player1Total
        for pit in PLAYER_1_PITS:
            board[pit] = 0  # Ustaw wszystkie dołki na 0.
    else:
        return 'brak zwycięzcy'  # Nikt jeszcze nie wygrał.

    # Koniec gry, znajdź gracza z najwyższym wynikiem:
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'remis'


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()

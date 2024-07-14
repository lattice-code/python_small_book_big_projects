"""Głodne roboty, autor: Al Sweigart, al@inventwithpython.com
Ucieka głodnym robotom i sprawiaj, by na siebie wpadały.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra"""

import random, sys

# Deklaracja stałych:
WIDTH = 40           # (!) Spróbuj zmienić tę wartość na 70 lub 10.
HEIGHT = 20          # (!) Spróbuj zmienić tę wartość na 10.
NUM_ROBOTS = 10      # (!) Spróbuj zmienić tę wartość na 1 lub 30.
NUM_TELEPORTS = 2    # (!) Spróbuj zmienić tę wartość na 0 lub 9999.
NUM_DEAD_ROBOTS = 2  # (!) Spróbuj zmienić tę wartość na 0 lub 20.
NUM_WALLS = 100      # (!) Spróbuj zmienić tę wartość na 0 lub 300.

EMPTY_SPACE = ' '    # (!) Spróbuj zmienić tę wartość na '.'.
PLAYER = '@'         # (!) Spróbuj zmienić tę wartość na 'R'.
ROBOT = 'R'          # (!) Spróbuj zmienić tę wartość na '@'.
DEAD_ROBOT = 'X'     # (!) Spróbuj zmienić tę wartość na 'R'.

# (!) Spróbuj zmienić tę wartość na '#' lub 'O', lub ' ':
WALL = chr(9617)  # Znak 9617 to '░'


def main():
    print('''Głodne roboty, autor: Al Sweigart, al@inventwithpython.com

Jesteś uwięziony w labiryncie z głodnymi robotami! Nie wiesz dlaczego roboty muszą jeść,  
jeść, ale nie chcesz się tego dowiedzieć. Roboty są źle zaprogramowane
i będą się poruszać wprost na Ciebie, nawet jeśli blokuje je ściana. 
Musisz tak mylić roboty, by na siebie wpadały (lub na zepsute roboty)
i by nie dać się złapać. Masz swoje własne urządzenie do teleportacji,
ale baterii wystarczy tylko na {} podróże. Pamiętaj, że zarówno ty, jak i roboty możecie
przeciskać się przez kąty utworzone z dwóch ukośnych ścian!
'''.format(NUM_TELEPORTS))

    input('Naciśnij Enter, by rozpocząć...')

    # Ustawienia nowej gry:
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True:  # Główna pętla programu.
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0:  # Sprawdź, czy gracz wygrał.
            print('Wszystkie roboty wpadły na siebie, a Ty przeżyłeś,')
            print(' by opowiedzieć tę historię! Dobra robota!')
            sys.exit()

        # Poruszaj graczem i robotami:
        playerPosition = askForPlayerMove(board, robots, playerPosition)
        robots = moveRobots(board, robots, playerPosition)

        for x, y in robots:  # Sprawdź, czy gracz przegrał.
            if (x, y) == playerPosition:
                displayBoard(board, robots, playerPosition)
                print('Zostałeś złapany przez robota!')
                sys.exit()


def getNewBoard():
    """Zwraca słownik, który przedstawia planszę. Kluczami są krotki liczb całkowitych (x, y),
    które wskazują położenie na planszy. Wartości to:
    WALL, EMPTY_SPACE lub DEAD_ROBOT. Słownik ma również klucz
    'teleports', gdzie zapisywane jest to ile jeszcze razy gracz może wykonać teleportację.
    Żyjące roboty są zapisywane osobno, poza słownikiem."""
    board = {'teleports': NUM_TELEPORTS}

    # Utwórz pustą planszę:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Dodaj ściany na brzegach planszy.
    for x in range(WIDTH):
        board[(x, 0)] = WALL  # Utwórz górną ścianę.
        board[(x, HEIGHT - 1)] = WALL  # Utwórz dolną ścianę.
    for y in range(HEIGHT):
        board[(0, y)] = WALL  # Utwórz lewą ścianę.
        board[(WIDTH - 1, y)] = WALL  # Utwórz prawą ścianę.

    # Dodaj losowe ściany:
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # Dodaj do planszy początkową liczbę zepsutych robotów:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """Zwraca krotkę liczb całkowitych (x, y) pustego miejsca na planszy."""
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """Zwraca wartość True, jeśli miejsce o współrzędnych (x, y) jest puste
    i nie ma tam robota."""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def addRobots(board):
    """Dodaje liczbę zapisaną w stałej NUM_ROBOTS robotów w pustych miejscach na planszy
    i zwraca listę (x, y) tych miejsc, w których teraz znajdują się roboty."""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots


def displayBoard(board, robots, playerPosition):
    """Wyświetla na ekranie planszę, roboty oraz gracza."""
    # Przejdź w pętli przez każde miejsce na planszy:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Narysuj odpowiednią postać:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()  # Wyświetl znak nowej linii.


def askForPlayerMove(board, robots, playerPosition):
    """Zwraca krotkę liczb całkowitych (x, y) miejsca, na które gracz 
    się przesuwa w następnym kroki, na podstawie bieżącej pozycji gracza i ścian."""
    playerX, playerY = playerPosition

    # Sprawdź, które kierunki nie są blokowane przez ściany:
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        # Pobierz ruch gracza:
        print('Pozostało (T)eleportacji: {}'.format(board['teleports']))
        print('                    ({}) ({}) ({})'.format(q, w, e))
        print('                    ({}) (S) ({})'.format(a, d))
        print('Podaj ruch lub KONIEC: ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # Przeteleportuj gracza w losowe miejsce na planszy:
            board['teleports'] -= 1
            return getRandomEmptySpace(board, robots)
        elif move != '' and move in allMoves:
            # Zwróć nową pozycję gracza na podstawiew oparciu o wykonanegoy ruchu:
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)}[move]


def moveRobots(board, robotPositions, playerPosition):
    """Zwraca listę krotek (x, y) nowych pozycji robotów
    po tym jak wykonały ruch w stronę gracza."""
    playerx, playery = playerPosition
    nextRobotPositions = []

    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]

        # Określ kierunek, w którym powinien poruszać się robot.
        if robotx < playerx:
            movex = 1  # Przesuń w prawo.
        elif robotx > playerx:
            movex = -1  # Przesuń w lewo.
        elif robotx == playerx:
            movex = 0  # Nie przesuwaj poziomo.

        if roboty < playery:
            movey = 1  # Przesuń w górę.
        elif roboty > playery:
            movey = -1  # Przesuń w dół.
        elif roboty == playery:
            movey = 0  # Nie przesuwaj pionowo.

        # Sprawdź, czy robot wpadnie na ścianę, i dostosuj odpowiednio ruch:
        if board[(robotx + movex, roboty + movey)] == WALL:
            # Robot wpadnie na ścianę, więc określ nowy ruch:
            if board[(robotx + movex, roboty)] == EMPTY_SPACE:
                movey = 0  # Robot nie może poruszać się poziomo.
            elif board[(robotx, roboty + movey)] == EMPTY_SPACE:
                movex = 0  # Robot nie może poruszać się pionowo.
            else:
                # Robot nie może się poruszyć.
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey

        if (board[(robotx, roboty)] == DEAD_ROBOT
            or board[(newRobotx, newRoboty)] == DEAD_ROBOT):
            # Robot wpadł na zepsutego robota, usuń go.
            del robotPositions[0]
            continue

        # Sprawdź, czy robot zderzył się z innym, a następnie usuń oba roboty:
        if (newRobotx, newRoboty) in nextRobotPositions:
            board[(newRobotx, newRoboty)] = DEAD_ROBOT
            nextRobotPositions.remove((newRobotx, newRoboty))
        else:
            nextRobotPositions.append((newRobotx, newRoboty))

        # Usuń roboty z listy robotPositions, kiedy się poruszają.
        del robotPositions[0]
    return nextRobotPositions


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()

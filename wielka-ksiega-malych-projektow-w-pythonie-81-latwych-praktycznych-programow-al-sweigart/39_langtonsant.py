"""Mrówka Langtona, autor: Al Sweigart, al@inventwithpython.com
Animacja automatu komórkowego. Naciśnij Ctrl+C, by zatryzmać program.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Mr%C3%B3wka_Langtona.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, bext, symulacja"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować za pomocą instrukcji ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

# Deklaracja stałych:
WIDTH, HEIGHT = bext.size()
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania znaku nowej linii, więc zmniejsz szerokość o 1:
WIDTH -= 1
HEIGHT -= 1  # Dostosuj dla instrukcji zatrzymania programu wyświetlanej na dole.

NUMBER_OF_ANTS = 10  # (!) Spróbuj zmienić tę wartość na 1 lub 50.
PAUSE_AMOUNT = 0.1  # (!) Spróbuj zmienić tę wartość na 1.0 lub 0.0.

# (!) Spróbuj zmienić te znaki, by mrówki wyglądały inaczej:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) Spróbuj zmienić te kolory na jeden wybrany z następującej listy: 'black' (czarny), 'red' (czerwony), 'green' (zielony),
# 'yellow' (żółty), 'blue' (niebieski), 'purple' (fioletowy), 'cyan' (niebieskozielony), 'white' (biały).
# (Moduł bext obsługuje tylko te kolory).
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    bext.fg(ANT_COLOR)  # Kolorem mrówki jest kolor pierwszego planu.
    bext.bg(WHITE_TILE)  # Na początku ustaw kolor tła na biały.
    bext.clear()

    # Stwórz strukturę danych dla nowej planszy:
    board = {'width': WIDTH, 'height': HEIGHT}

    # Stwórz struktury danych dla mrówek:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # Zapisuj, które pole się zmieniły i muszą być ponownie narysowane
    # na ekranie:
    changedTiles = []

    while True:  # Główna pętla programu.
        displayBoard(board, ants, changedTiles)
        changedTiles = []

        # Zmienna nextBoard to wygląd planszy w następnym kroku symulacji.
        # Zacznij od skopiowania planszy z bieżącego etapu:
        nextBoard = copy.copy(board)

        # Uruchom pojedynczy krok symulacji dla każdej mrówki:
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # Obróć zgodnie z ruchem wskazówekkami zegara:
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # Obróć przeciwnie do ruchu wskazówek zegara:
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changedTiles.append((ant['x'], ant['y']))

            # Przesuń mrówkę do przodu w kierunku, w którym jest obrócona:
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            if ant['direction'] == SOUTH:
                ant['y'] += 1
            if ant['direction'] == WEST:
                ant['x'] -= 1
            if ant['direction'] == EAST:
                ant['x'] += 1

            # Jeśli mrówka wychodzi poza ekran,
            # powinna pojawić się przy przeciwnej krawędzi.
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.append((ant['x'], ant['y']))

        board = nextBoard


def displayBoard(board, ants, changedTiles):
    """Wyświetla planszę i mrówki na ekranie. Argument changedTiles
    to lista krotek (x, y) dla pól na ekranie,
    które się zmieniły i muszą być ponownie narysowane."""

    # Narysuj strukturę danych przedstawiającą planszę:
    for x, y in changedTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        antIsHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not antIsHere:
            print(' ', end='')

    # Na dole ekranu wyświetl informację jak zatrzymać program:
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print('Naciśnij Ctrl+C, by zatrzymać program.', end='')

    sys.stdout.flush()  # (Wymagane przez programy używające modułu bext).
    time.sleep(PAUSE_AMOUNT)


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Mrówka Langtona, autor: Al Sweigart, al@inventwithpython.com")
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

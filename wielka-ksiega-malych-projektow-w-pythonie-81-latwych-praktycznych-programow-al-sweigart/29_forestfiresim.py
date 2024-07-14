"""Symulacja pożaru lasu, autor: Al Sweigart, al@inventwithpython.com
Symulacja pożaru rozprzestrzeniającego się w lesie. Naciśnij Ctrl+C, by zatrzymać program.
Zainspirowana programem Nicky'ego Case'a ze strony http://ncase.me/simulating/model/. 
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, bext, symulacja"""

import random, sys, time

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować według instrukcji ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

# Deklaracja stałych:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# (!) Spróbuj zmienić te ustawienia na dowolną wartość między 0.0 a 1.0:
INITIAL_TREE_DENSITY = 0.20  # Liczba drzew na początku programu.
GROW_CHANCE = 0.01  # Szansa na wyrośnięcie drzewa w pustym miejscu.
FIRE_CHANCE = 0.01  # Szansa, że drzewo zostanie uderzone przez piorun i spłonie.

# (!) Spróbuj ustawić długość pauzy na 1.0 lub 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Główna pętla programu.
        displayForest(forest)

        # Uruchom pojedynczy krok symulacji:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # Jeśli ustawiłeś już nextForest[(x, y)]
                    # w poprzednim obiegu pętli, to nic nie rób:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Zasadź drzewo w pustym miejscu:
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Piorun podpala drzewo:
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # To drzewo cały czas płonie.
                    # Przejdź przez wszystkie sąsiednie miejsca:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Pożar rozprzestrzenia się na sąsiednie drzewa:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # Drzewo spłonęło, więc je usuń:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Po prostu skopiuj istniejący obiekt:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Zwraca słownik dla nowego lasu."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Zacznij od drzewa.
            else:
                forest[(x, y)] = EMPTY  # Zacznij od pustego miejsca.
    return forest


def displayForest(forest):
    """Wyświetl las na ekranie."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Użyj domyślnego koloru czcionki.
    print('Szansa na drzewo: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Szansa na piorun: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Naciśnij Ctrl+C, by zatrzymać program.')


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

"""Klepsydra, autrostwa Ala Sweigarta al@inventwithpython.com
Animacja klepsydry z spadającym piaskiem. Naciśnij Ctrl+C, by zatrzymać program.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, bext, symulacja"""

import random, sys, time

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować za pomocą instrukcji ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

# Deklaracja stałych:
PAUSE_LENGTH = 0.2  # (!) Spróbuj zmienić tę wartość na 0.0 lub 1.0.
# (!) Spróbuj zmienić tę wartość na liczbę z zakresu od 0 do 100:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0  # Indeks wartości X w krotce (x, y) to 0.
Y = 1  # Indeks wartości Y w krotce (x, y) to 1.
SAND = chr(9617)
WALL = chr(9608)

# Utwórz obudowę klepsydry:
HOURGLASS = set()  # Zestaw obudowy ma krotki (x, y), gdzie zapisane są ściany klepsydry.
# (!) Spróbuj umieścić znaczniki komentarza przed kilkoma wyrażeniami HOURGLASS.add(), by usunąć ścianki:
for i in range(18, 37):
    HOURGLASS.add((i, 1))  # Dodanie ścianek górnej pokrywy obudowy.
    HOURGLASS.add((i, 23))  # Dodanie ścianek dolnej pokrywy obudowy.
for i in range(1, 5):
    HOURGLASS.add((18, i))  # Dodanie górnej lewej prostej ścianki.
    HOURGLASS.add((36, i))  # Dodanie górnej prawej prostej ścianki.
    HOURGLASS.add((18, i + 19))  # Dodanie dolnej lewej prostej ścianki.
    HOURGLASS.add((36, i + 19))  # # Dodanie dolnej prawej prostej ścianki.
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # Dodanie górnej lewej pochylonej ścianki.
    HOURGLASS.add((35 - i, 5 + i))  # Dodanie górnej prawej pochylonej ścianki.
    HOURGLASS.add((25 - i, 13 + i))  # Dodanie dolnej lewej pochylonej ścianki.
    HOURGLASS.add((29 + i, 13 + i))  # Dodanie dolnej prawej pochylonej ścianki.

# Stwórz pierwsze ziarnko piasku na górze klepsydry:
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    # Wyświetl informację, jak wyjść z programu:
    bext.goto(0, 0)
    print('Naciśnij Ctrl+C, by wyjść z programu.', end='')

    # Wyświetl ściany klepsydry:
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:  # Główna pętla programu.
        allSand = list(INITIAL_SAND)

        # Narysuj pierwsze ziarnko:
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        runHourglassSimulation(allSand)


def runHourglassSimulation(allSand):
    """Odtwarzaj symulacje spadającego piasku,
    dopóki ziarnko nie przestanie się ruszać."""
    while True:  # Zapętlaj instrukcje, dopóki ziarnko jest w ruchu.
        random.shuffle(allSand)  # Losowa kolejność symulacji ziarnka.

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # Piasek jest na samym spodzie, więc się nie poruszy:
                continue

            # Jeśli nic nie ma pod ziarnkiem, przesuń je w dół:
            noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # Narysuj ziarnko w jego nowej pozycji, jedną linijkę niżej:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Usuń ziarnko z poprzedniej pozycji.
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # Ustaw ziarnko w jego nowej pozycji, jedną linijkę niżej:
                allSand[i] = (sand[X], sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                # Sprawdź, czy ziarnko może spaść w lewo:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge)

                # Sprawdź, czy ziarnko może spaść w prawo:
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and noWallBelowRight
                    and noWallRight and notOnRightEdge)

                # Ustaw kierunek spadania:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1  # Ustaw ziarnko, by spadało w lewo.
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1  # Ustaw ziarnko, by spadało w prawo.
                elif canFallLeft and canFallRight:
                    # Oba kierunki są możliwe, więc wybierz jeden z nich losowo:
                    fallingDirection = random.choice((-1, 1))

                # Sprawdź, czy ziarnko może spaść w lewo lub w prawo dwie linijki niżej,
                # zamiast tylko jedną linijkę:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge)

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (canFallRight
                        and noSandBelowTwoRight and noWallBelowTwoRight
                        and notOnSecondToRightEdge)

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    # To ziarnko nie może spaść, dlatego idź do początku pętli i wykonaj kolejną iterację.
                    continue

                # Narysuj ziarnko w nowej pozycji:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Usuń stare ziarnko.
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')  # Narysuj nowe ziarnko.

                # Przesuń ziarnko do nowej pozycji:
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        sys.stdout.flush()  # (Wymagane dla programów wykorzystujących moduł bext.)
        time.sleep(PAUSE_LENGTH)  # Zatrzymaj program na chwilę.

        # Jeśli na tym etapie żadne ziarnko się nie poruszyło, obróć klepsydrę:
        if not sandMovedOnThisStep:
            time.sleep(2)
            # Usuń cały piasek:
            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break  # Wyjdź z głównej pętli symulacji.


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

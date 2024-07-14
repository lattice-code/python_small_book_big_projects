"""Animacja logo DVD, autor: Al Sweigart, al@inventwithpython.com
Animacja odbijającego się logo DVD. Musisz być "odpowiednio stary", by to docenić.
Naciśnij Ctrl+C, by zatrzymać program.

UWAGA: Nie zmieniaj rozmiaru okna terminala podczas działania programu.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, artystyczny, bext"""

import sys, random, time

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować według instrukcji ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

# Deklaracja stałych:
WIDTH, HEIGHT = bext.size()
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania nowej linii, więc zmniejsz szerokość o 1:
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # (!) Spróbuj zmienić tę wartość na 1 lub 100.
PAUSE_AMOUNT = 0.2  # (!) Spróbuj zmienić tę wartość na 1.0 lub 0.0.
# (!) Spróbuj zmniejszyć liczbę kolorów:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Klucze słownika logo:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # Wygeneruj kilka logo:
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Upewnij się, że x jest parzyste, by logo mogło uderzyć w róg.
            logos[-1][X] -= 1

    cornerBounces = 0  # Policz, ile razy logo uderzyło w róg.
    while True:  # Główna pętla programu.
        for logo in logos:  # Obsługa każdego logo z listy.
            # Usunięcie logo z bieżącego położenia:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')  # (!) Spróbuj umieścić znacznik komentarza przed tą linią.

            originalDirection = logo[DIR]

            # Sprawdź, czy logo odbiło się od rogu:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # Sprawdź, czy logo odbiło się od lewej krawędzi:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # Sprawdź, czy logo odbiło się od prawej krawędzi:
            # (stała WIDTH - 3, ponieważ słowo 'DVD' ma 3 litery).
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # Sprawdź, czy logo odbiło się od górnej krawędzi:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # Sprawdź, czy logo odbiło się od dolnej krawędzi:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # Zmień kolor logo po odbiciu:
                logo[COLOR] = random.choice(COLORS)

            # Przesuń logo. (Współrzędna X o 2, ponieważ znaki terminala
            # mają wysokość dwa razy większą niż szerokość.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Wyświetlenie liczby uderzeń w róg:
        bext.goto(5, 0)
        bext.fg('white')
        print('Odbicie od rogu:', cornerBounces, end='')

        for logo in logos:
            # Rysuj loga w ich nowym położeniu:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # (Wymagane w programach używających modułu bext).
        time.sleep(PAUSE_AMOUNT)


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Animacja logo DVD, autor: Al Sweigart')
        sys.exit()  # Gdy wciśnięto Ctrl+C, zakończ program.

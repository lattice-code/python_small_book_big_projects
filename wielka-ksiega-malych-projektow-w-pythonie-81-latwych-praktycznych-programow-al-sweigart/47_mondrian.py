"""Generator sztuki Mondriana, autor: Al Sweigart, al@inventwithpython.com
Generuje losowy obraz w stylu Pieta Mondriana.
Więcej informacji na stronie: https://pl.wikipedia.org/wiki/Piet_Mondrian.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, bext"""

import sys, random

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować za pomocą instrukcji ze strony ')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

# Deklaracja stałych:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

# Ustawienie ekranu:
width, height = bext.size()
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania znaku nowej linii, więc zmniejsz szerokość o 1:
width -= 1

height -= 3

while True:  # Główna pętla programu.
    # Przygotuj płótno z pustymi miejscami:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    # Wygeneruj linie pionowe:
    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    # Wygeneruj linie poziome:
    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

    # Wybierz losowo punkty i postaraj się je usunąć.
    for i in range(numberOfSegmentsToDelete):
        while True:  # Wybieraj segmenty, które będziesz starać się usunąć.
            # Pobierz losowy punkt początkowy istniejącego segmentu:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if canvas[(startx, starty)] == WHITE:
                continue

            # Sprawdź, czy zajdziesz się na pionowym czy poziomym segmencie:
            if (canvas[(startx - 1, starty)] == WHITE and
                canvas[(startx + 1, starty)] == WHITE):
                orientation = 'pionowy'
            elif (canvas[(startx, starty - 1)] == WHITE and
                canvas[(startx, starty + 1)] == WHITE):
                orientation = 'poziomy'
            else:
                # Punkt początkowy jest na skrzyżowaniu,
                # więc wybierz nowy losowy punkt początkowy:
                continue

            pointsToDelete = [(startx, starty)]

            canDeleteSegment = True
            if orientation == 'pionowy':
                # Idź o jeden krok do góry od punktu początkowego
                # i zobacz, czy możemy usunąć ten segment:
                for changey in (-1, 1):
                    y = starty
                    while 0 < y < height - 1:
                        y += changey
                        if (canvas[(startx - 1, y)] == BLACK and
                            canvas[(startx + 1, y)] == BLACK):
                            # Znaleziono skrzyżowanie czterokierunkowe:
                            break
                        elif ((canvas[(startx - 1, y)] == WHITE and
                               canvas[(startx + 1, y)] == BLACK) or
                              (canvas[(startx - 1, y)] == BLACK and
                               canvas[(startx + 1, y)] == WHITE)):
                            # Znaleziono skrzyżowanie w kształcie litery T,
                            # nie możemy usunąć tego segmentu:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx, y))

            elif orientation == 'poziomy':
                # Idź o jeden krok do góry od punktu początkowego
                # i zobacz, czy możemy usunąć ten segment:
                for changex in (-1, 1):
                    x = startx
                    while 0 < x < width - 1:
                        x += changex
                        if (canvas[(x, starty - 1)] == BLACK and
                            canvas[(x, starty + 1)] == BLACK):
                            # Znaleziono skrzyżowanie czterokierunkowe:
                            break
                        elif ((canvas[(x, starty - 1)] == WHITE and
                               canvas[(x, starty + 1)] == BLACK) or
                              (canvas[(x, starty - 1)] == BLACK and
                               canvas[(x, starty + 1)] == WHITE)):
                            # Znaleziono skrzyżowanie w kształcie litery T,
                            # nie możemy usunąć tego segmentu:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((x, starty))
            if not canDeleteSegment:
                continue  # Pobierz losowy punkt początkowy.
            break  # Idź dalej, by usunąć dany segment.

        # Jeśli można usunąć ten segment, zmień kolor wszystkich punktów na biały:
        for x, y in pointsToDelete:
            canvas[(x, y)] = WHITE

    # Dodaj obrysy:
    for x in range(width):
        canvas[(x, 0)] = BLACK  # Górny obrys.
        canvas[(x, height - 1)] = BLACK  # Dolny obrys.
    for y in range(height):
        canvas[(0, y)] = BLACK  # Lewy obrys.
        canvas[(width - 1, y)] = BLACK  # Prawy obrys.

    # Maluj prostokąty:
    for i in range(numberOfRectanglesToPaint):
        while True:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)

            if canvas[(startx, starty)] != WHITE:
                continue  # Pobierz nowy punkt początkowy.
            else:
                break

        # Algorytm flood fill:
        colorToPaint = random.choice([RED, YELLOW, BLUE, BLACK])
        pointsToPaint = set([(startx, starty)])
        while len(pointsToPaint) > 0:
            x, y = pointsToPaint.pop()
            canvas[(x, y)] = colorToPaint
            if canvas[(x - 1, y)] == WHITE:
                pointsToPaint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                pointsToPaint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                pointsToPaint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                pointsToPaint.add((x, y + 1))

    # Wyświetl strukturę danych dla płótna:
    for y in range(height):
        for x in range(width):
            bext.bg(canvas[(x, y)])
            print(' ', end='')

        print()

    # Spytaj się użytkownika, czy chce wygenerować kolejny obraz:
    try:
        input('Naciśnij Enter, jeśli chcesz stworzyć następny obraz, lub Ctrl+C, by wyjść z programu.')
    except KeyboardInterrupt:
        sys.exit()

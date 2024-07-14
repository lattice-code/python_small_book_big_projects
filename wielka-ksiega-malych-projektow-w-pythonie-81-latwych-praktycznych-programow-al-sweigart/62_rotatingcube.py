"""Obracający się sześcian, autor: Al Sweigart, al@inventwithpython.com
Animacja obracającego się sześcianu. Naciśnij Ctrl+C, by zatrzymać program.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, matematyka"""

# Ten program MUSI być uruchomiony w oknie terminala/wiersza polecenia.

import math, time, sys, os

# Deklaracja stałych:
PAUSE_AMOUNT = 0.1  # Długość pauzy, jedna dziesiąta sekundy.
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
# Wysokość tekstu jest dwa razy większa niż jego szerokość, zatem taką wartość ma stała scaley:
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

# (!) Spróbuj zmienić tę wartość na '#' lub '*', albo na jeszcze inny znak:
LINE_CHAR = chr(9608)  # Znak 9608 to jednolity blok.

# (!) Spróbuj ustawić dwie z tych wartości na zero,
# by obracać sześcian tylko wokół jednej osi:
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

# Ten program zapisuje współrzędne XYZ w listach, współrzędną X
# na pozycji 0, Y na 1, a Z na 2. Dzięki tym stałym nasz kod
# jest czytelny, pomimo że współrzędne są w listach.
X = 0
Y = 1
Z = 2


def line(x1, y1, x2, y2):
    """Zwraca listę punktów w linii łączącej dane punkty.

    Używa algorytmu Bresenhama. Więcej informacji na stronie
    https://pl.wikipedia.org/wiki/Algorytm_Bresenhama."""
    points = []  # Lista punktów w linii.
    # "Stromy" znaczy, że kąt nachylenia linii jest większy niż 45 stopni lub
    # mniejszy niż -45 stopni.

    # Sprawdź, czy to nie jest szczególny przypadek, gdy czyli punkty początkowe i końcowe
    # określonych sąsiadujących ze sobą punktów, których ta funkcja nie obsługuje poprawnie.
    # W zamian zwróć ustaloną na sztywno listę:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        # Ten algorytm obsługuje tylko niestrome linie, więc zmieńmy
        # nachylenie na niestrome, a następnie przywrócimy pierwotne nachylenie.
        x1, y1 = y1, x1  # Zamień x1 i y1
        x2, y2 = y2, x2  # Zamień x2 i y2
    isReversed = x1 > x2  # Wartość True, jeśli linia biegnie od prawej do lewej.

    if isReversed:  # Pobierz punkty leżące na linii biegnącej od prawej do lewej.
        x1, x2 = x2, x1  # Zamień x1 i x2
        y1, y2 = y2, y1  # Zamień y1 i y2

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Oblicz y dla każdego x w tej linii:
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:  # Zmień y tylko raz, gdy extray <= 0.
                currenty -= ydirection
                extray += deltax
    else:  # Pobierz punkty leżące na linii biegnącej od lewej do prawej.
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # Oblicz y dla każdego x w tej linii:
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0:  # Zmień y tylko raz, gdy extray <= 0.
                currenty += ydirection
                extray += deltax
    return points


def rotatePoint(x, y, z, ax, ay, az):
    """Zwraca krotkę (x, y, z) obróconych argumentów x, y, z.

    Obrót odbywa się wokół punktu 0, 0, 0 o kąty
    ax, ay, az (podane w radianach).
        Kierunek każdej osi:
         -y
          |
          +-- +x
         /
        +z
    """

    # Obracaj wokół osi x:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Obracaj wokół osi y:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Obracaj wokół osi z:
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


def adjustPoint(point):
    """Dostosuj punkt 3D XYZ do punktu 2D XY w celu wyświetlenia go
    na ekranie. Zmiana wielkości punktu 2D według skali zapisanej w stałych SCALEX oraz
    SCALEY, a następnie przesunięcie punktu o wartości stałych TRANSLATEX i TRANSLATEY."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


"""Lista CUBE_CORNERS zawiera współrzędne XYZ wierzchołków sześcianu.
Indeksy każdego wierzchołka zapisanego w CUBE_CORNERS są oznaczone na tym schemacie:
      0---1
     /|  /|
    2---3 |
    | 4-|-5
    |/  |/
    6---7"""
CUBE_CORNERS = [[-1, -1, -1], # Punkt 0
                [ 1, -1, -1], # Punkt 1
                [-1, -1,  1], # Punkt 2
                [ 1, -1,  1], # Punkt 3
                [-1,  1, -1], # Punkt 4
                [ 1,  1, -1], # Punkt 5
                [-1,  1,  1], # Punkt 6
                [ 1,  1,  1]] # Punkt 7
# Lista rotatedCorners zawiera współrzędne XYZ z listy CUBE_CORNERS po
# po obrocie o wartości zmiennych rx, ry i rz:
rotatedCorners = [None, None, None, None, None, None, None, None]
# Wartość obrotu każdej osi:
xRotation = 0.0
yRotation = 0.0
zRotation = 0.0

try:
    while True:  # Główna pętla programu.
        # Obróć sześcian wokół osi o różne wartości:
        xRotation += X_ROTATE_SPEED
        yRotation += Y_ROTATE_SPEED
        zRotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotatedCorners[i] = rotatePoint(x, y, z, xRotation,
                yRotation, zRotation)

        # Pobierz punkty linii sześcianu:
        cubePoints = []
        for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            fromX, fromY = adjustPoint(rotatedCorners[fromCornerIndex])
            toX, toY = adjustPoint(rotatedCorners[toCornerIndex])
            pointsOnLine = line(fromX, fromY, toX, toY)
            cubePoints.extend(pointsOnLine)

        # Usuń powtarzające się punkty:
        cubePoints = tuple(frozenset(cubePoints))

        # Wyświetl sześcian na ekranie:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    # Wyświetl pełny blok:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    # Wyświetl spację:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Naciśnij Ctrl+C, by wyjść z programu.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)  # Zatrzymaj się na chwilę.

        # Wyczyść ekran:
        if sys.platform == 'win32':
            os.system('cls')  # System Windows używa polecenia cls.
        else:
            os.system('clear')  # Systemy macOS i Linux używają polecenia clear.

except KeyboardInterrupt:
    print('Obracający się sześcian, autor: Al Sweigart, al@inventwithpython.com')
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

"""Matematyka i kostki, autor: Al Sweigart, al@inventwithpython.com
Program, który sprawdza jak szybko potrafisz dodawać wyrzucone na kostkach oczka.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, gra, matematyka"""

import random, time

# Deklaracja stałych:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # Odejmij 3, by zostawić miejsce na dole na wprowadzenie sumy.

# Czas trwania w sekundach:
QUIZ_DURATION = 30  # (!) Spróbuj zmienić tę wartość na 10 lub 60.
MIN_DICE = 2  # (!) Spróbuj zmienić tę wartość na 1 lub 5.
MAX_DICE = 6  # (!) Spróbuj zmienić tę wartość na 14.

# (!) Spróbuj zmienić te wartości na inne:
REWARD = 4  # (!) Punkty przyznawane za poprawną odpowiedź.
PENALTY = 1  # (!) Punkty odejmowane za złą odpowiedź.
# (!) Spróbuj ustawić stałą PENALTY na liczbę ujemną,
# by gracz dostawał punkty za niepoprawną odpowiedź!

# Program zawiesza się, jeśli nie wszystkie kości mieszczą się na ekranie:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Matematyka i kości, autor: Al Sweigart, al@inventwithpython.com

Dodaj oczka wszystkich kości na ekranie. Masz {} sekund,
by podać jak największą liczbę odpowiedzi. Otrzymujesz {} punkty za każdą
poprawną odpowiedź i tracisz {} punkt za każdą złą odpowiedź.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Naciśnij Enter, aby rozpocząć...')

# Zapisuj liczbę poprawnych i niepoprawnych odpowiedzi:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:  # Główna pętla gry.
    # Wylosuj liczbę, innymi słowy, rzuć kostką:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0] zawiera listę łańcuchów znaków przedstawiających grafikę ścian kości:
        diceFaces.append(die[0])
        # die[1] zawiera liczbę całkowitą oznaczającą liczbę oczek na ścianie kości:
        sumAnswer += die[1]

    # Zawiera krotkę (x, y) górnego lewego rogu każdej kości.
    topLeftDiceCorners = []

    # Określ, gdzie powinna być wyświetlona kostka:
    for i in range(len(diceFaces)):
        while True:
            # Znajdź losowe miejsce na płótnie, gdzie zostanie wyświetlona kość:
            left = random.randint(0, CANVAS_WIDTH  - 1 - DICE_WIDTH)
            top  = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Pobierz współrzędne x, y dla wszystkich czterech rogów:
            #        lewy
            #        v
            #górny > +-------+ ^
            #        | O     | |
            #        |   O   | DICE_HEIGHT (5)
            #        |     O | |
            #        +-------+ v
            #        <------->
            #        DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # Sprawdź, czy ta kostka nie nachodzi na poprzednią.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # Sprawdź każdy róg kości, by zobaczyć, czy znajduje się w środku
                # poprzedniej kości:
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                            overlaps = True
            if not overlaps:
                # Kości nie zachodzą na siebie, więc możemy wyświetlić kostkę w tym miejscu:
                topLeftDiceCorners.append((left, top))
                break

    # Narysuj kość na płótnie:

    # Klucze (x, y) to krotki liczb całkowitych, które określają
    # położenie na ekranie:
    canvas = {}
    # Przejdź przez każdą kostkę:
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # Przejdź przez każdy znak tworzący grafikę ściany kości:
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # Skopiuj ten znak do odpowiedniego miejsca na płótnie:
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # Zauważ, że w liście łańcuchów znaków dieFace, x i y
                # są zamienione:
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # Wyświetl płótno na ekranie:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # Wyświetl znak nowej linii.

    # Pozwól graczowi wpisać odpowiedź:
    response = input('Podaj sumę: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Źle, poprawna odpowiedź to ', sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1

# Wyświetl wyniki końcowe:
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Poprawne odpowiedzi:  ', correctAnswers)
print('Niepoprawne odpowiedzi:', incorrectAnswers)
print('Wynik:    ', score)

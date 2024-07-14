"""Akwarium, autor: Al Sweigart, al@inventwithpython.com
Kojąca animacja akwarium z rybkami. Naciśnij Ctrl+C, by zatrzymać.
Program podobny do ASCIIQuarium lub @EmojiAquarium, ale mój jest oparty
na starszej wersji tego programu na system DOS.
https://robobunny.com/projects/asciiquarium/html/
https://twitter.com/EmojiAquarium
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: bardzo długi, artystyczny, bext"""

import random, sys, time

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

NUM_KELP = 2  # (!) Spróbuj zmienić tę wartość na 10.
NUM_FISH = 10  # (!) Spróbuj zmienić tę wartość na 2 lub 100.
NUM_BUBBLERS = 1  # (!) Spróbuj zmienić tę wartość na 0 lub 10.
FRAMES_PER_SECOND = 4  # (!) Spróbuj zmienić tę wartość na 1 lub 60.
# (!) Spróbuj zmienić stałe, by stworzyć akwarium tylko z roślinami.
# lub tylko z bąbelkami.

# UWAGA: Każdy łańcuch znaków w słowniku z rybami powinien mieć taką samą długość.
FISH_TYPES = [
  {'right': ['><>'],          'left': ['<><']},
  {'right': ['>||>'],         'left': ['<||<']},
  {'right': ['>))>'],         'left': ['<[[<']},
  {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
  {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
  {'right': ['>-==>'],        'left': ['<==-<']},
  {'right': [r'>\\>'],        'left': ['<//<']},
  {'right': ['><)))*>'],      'left': ['<*(((><']},
  {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
  {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
  {'right': ['><XXX*>'],      'left': ['<*XXX><']},
  {'right': ['_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'],
   'left':  ['<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.']},
  ]  # (!) Spróbuj dodać własną rybę do słownika FISH_TYPES.
LONGEST_FISH_LENGTH = 10  # Najdłuższy pojedynczy łańcuch znaków w słowniku FISH_TYPES.

# Pozycje x i y, gdzie ryba dociera do brzegu ekranu:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # Utwórz zmienne globalne:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # UWAGA: Bąbelki są rysowane, ale generator bąbelków nie.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Każdy generator bąbelków ustawia się w losowej pozycji.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # Utwórz każdą część rośliny:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # Uruchom symulację:
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1


def getRandomColor():
    """Zwraca losową nazwę koloru (w języku angielskim)."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generateFish():
    """Zwraca słownik, który przedstawia rybę."""
    fishType = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # Wszystkie części mają nadany losowy kolor.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength  # Wszystko jest takiego samego koloru.
    if colorPattern == 'head-tail':  # Głowa/ogon inne niż ciało.
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # Ustaw kolor głowy.
        colors[-1] = headTailColor  # Ustaw kolor ogona.

    # Ustaw resztę cech ryby:
    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1, 6),
            'vSpeed':           random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight':       random.choice([True, False]),
            'goingDown':        random.choice([True, False])}

    # 'x' jest zawsze punktem leżącym najbardziej z lewej strony ryby:
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    """Symuluje ruchy w akwarium przez jeden krok."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Symulacja ryby przez jeden krok:
    for fish in FISHES:
        # Przesuń rybę poziomo:
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1  # Przesuń rybę w prawo.
                else:
                    fish['goingRight'] = False  # Obróć rybę.
                    fish['colors'].reverse()  # Odwróć kolory.
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1  # Przesuń ogon w lewo.
                else:
                    fish['goingRight'] = True  # Obróć rybę.
                    fish['colors'].reverse()  # Odwróć kolory.

        # Ryba może losowo zmieniać swój kierunek w poziomie:
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            # Obróć rybę:
            fish['goingRight'] = not fish['goingRight']

        # Przesuń rybę pionowo:
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1  # Przesuń rybę w dół.
                else:
                    fish['goingDown'] = False  # Obróć rybę.
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1  # Przesuń rybę do góry.
                else:
                    fish['goingDown'] = True  # Obróć rybę.

        # Ryba może losowo zmieniać swój kierunek w pionie:
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            # Obróć rybę:
            fish['goingDown'] = not fish['goingDown']

    # Wypuść bąbelki z generatorów:
    for bubbler in BUBBLERS:
        # Istnieje szansa 1 na 5, że powstanie bąbelek:
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # Przesuń bąbelki:
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1  # Bąbelek idzie w lewo.
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1  # Bąbelek idzie w prawo.

        bubble['y'] -= 1  # Bąbelek zawsze idzie w górę.

    # Przejdź przez słownik BUBBLES do tyłu, ponieważ bąbelki są usuwane
    # w pętli.
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:  # Usuń bąbelki, które dotarły do górnej krawędzi.
            del BUBBLES[i]

    # Symulacja rośliny przez jeden krok:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # Szansa 1 na 20, że roślina będzie falować:
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    """Rysuje akwarium na ekranie."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Wyświetl informację o programie:
    bext.fg('white')
    bext.goto(0, 0)
    print('Akwarium, autor: Al Sweigart    Ctrl+C: wyjście.', end='')

    # Narysuj bąbelki:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    # Narysuj ryby:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # Pobierz odpowiedni łańcuch znaków dla ryby zwróconej w lewą lub prawą stronę.
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]

        # Narysuj każdy znak ryby w odpowiednim kolorze:
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # Narysuj rośliny:
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    # Narysuj piasek na dnie:
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')  # Rysuje znaki '░'.

    sys.stdout.flush()  # (Wymagane w programach używających modułu bext.)


def clearAquarium():
    """Rysuje puste pola na wszystkim, co jest na ekranie."""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Narysuj bąbelki:
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # Narysuj ryby:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # Narysuj każdy znak ryby w odpowiednim kolorze:
        print(' ' * len(fish['left'][0]), end='')

    # Narysuj rośliny:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')

    sys.stdout.flush()  # (Wymagane w programach używających modułu bext).


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

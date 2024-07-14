"""Znikopis, autor: Al Sweigart, al@inventwithpython.com
Program rysujący linię ciągłą na ekranie
za pomocą klawiszy WASD. Zainspirowany popularną zabawką, znikopisem.

Na przykład możesz narysować fraktal krzywej Hilberta za pomocą:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

A nawet większy fraktal krzywej Hilberta za pomocą:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD.

Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny"""

import shutil, sys

# Deklaracja stałych dla znaków linii:
UP_DOWN_CHAR         = chr(9474)  # Znak 9474 to '│'.
LEFT_RIGHT_CHAR      = chr(9472)  # Znak 9472 to '─'.
DOWN_RIGHT_CHAR      = chr(9484)  # Znak 9484 to '┌'.
DOWN_LEFT_CHAR       = chr(9488)  # Znak 9488 to '┐'.
UP_RIGHT_CHAR        = chr(9492)  # Znak 9492 to '└'.
UP_LEFT_CHAR         = chr(9496)  # Znak 9496 to '┘'.
UP_DOWN_RIGHT_CHAR   = chr(9500)  # Znak 9500 to '├'.
UP_DOWN_LEFT_CHAR    = chr(9508)  # Znak 9508 to '┤'.
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Znak 9516 to '┬'.
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Znak 9524 to '┴'.
CROSS_CHAR           = chr(9532)  # Znak 9532 to '┼'.
# Lista kodów chr() dostępna na stronie https://inventwithpython.com/chr.

# Pobierz rozmiar okna terminala:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania znaku nowej linii, więc zmniejsz szerokość o 1:
CANVAS_WIDTH -= 1
# Zostaw kilkuwierszowe miejsce na polecenia.
CANVAS_HEIGHT -= 5

"""Kluczami słownika canvas będą krotki liczb całkowitych (x, y) reprezentujących współrzędne,
a wartość to zestaw liter W, A, S, D, które mówią, jaki typ linii
ma być narysowany."""
canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """Zwraca wielolinijkowy łańcuch znaków przedstawiający linię narysowaną na płótnie, canvasData."""
    canvasStr = ''

    """canvasData to słownik, którego kluczami są krotki (x, y),
    a wartościami jest zestaw łańcuchów znaków 'W', 'A', 'S', i/lub 'D', by wskazać
    kierunek, w jakim rysowane są linie w każdym punkcie xy."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # Dodaj znak linii dla tego punktu do zmiennej canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'  # Dodaj znak nowej linii na końcu każdego wiersza.
    return canvasStr


moves = []
while True:  # Główna pętla programu.
    # Narysuj linię na podstawie danych w słowniku canvas:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD: ruch, H: pomoc, C: wyczyść, '
        + 'F: zapisz lub KONIEC.')
    response = input('> ').upper()

    if response == 'KONIEC':
        print('Dziękujemy za grę!')
        sys.exit()  # Wyjdź z programu.
    elif response == 'H':
        print('Podaj znaki W, A, S i D, by poruszać kursorem po ekranie')
        print('i rysuj za kursorem linię. Na przykład ddd')
        print('rysuje linię biegnącą w prawo, a sssdddwwwaaa rysuje kwadrat.')
        print()
        print('Możesz zapisać swój rysunek w pliku tekstowym za pomocą klawisza F.')
        input('Naciśnij Enter, by wrócić do programu...')
        continue
    elif response == 'C':
        canvas = {}  # Usuń dane ze słownika canvas.
        moves.append('C')  # Zapisz ten ruch.
    elif response == 'F':
        # Zapisz łańcuch znaków w pliku tekstowym:
        try:
            print('Podaj nazwę pliku:')
            filename = input('> ')

            # Upewnij się, że na końcu podanej nazwy pliku jest .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('BŁĄD: Nie można zapisać pliku.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # Pomiń tę literę i przejdź do kolejnej.
        moves.append(command)  # Zapisz ten ruch.

        # Pierwsza linia, którą dodajemy, musi tworzyć pełną linię:
        if canvas == {}:
            if command in ('W', 'S'):
                # Spraw, by pierwsza linia była pozioma:
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # Spraw, by pierwsza linia była pionowa:
                canvas[(cursorX, cursorY)] = set(['A', 'D'])

        # Zaktualizuj wartość x i y:
        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY - 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX - 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            # Jeśli kursor się nie rusza, ponieważ wyszedł poza ekran,
            # nie zmieniaj zestawu w słowniku
            # canvas[(cursorX, cursorY)].
            continue

        # Jeśli nie ma zestawu dla (cursorX, cursorY), dodaj pusty zestaw:
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        # Dodaj łańcuch znaków wyznaczający kierunek do zestawu punktów xy:
        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')

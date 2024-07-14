"""99 buUtellek Mleka an póŁce
Autorstwa Ala Sweigarta al@inventwithpython.com
Wyświetla wszystkie zwrotki jednej z najdłuższych  piosenek, jakie kiedykolwiek powstały!
Piosenka z każdym wersem staje się coraz zabawniejsza. Naciśnij Ctrl+C, by zatrzymać program.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, przewijanie, słowa"""

import random, sys, time

# Deklaracja stałych:
# (!) Spróbuj zmienić te dwie wartości na 0, by wyświetlić od razu całą piosenkę.
SPEED = 0.01  # Przerwa między wyświetlaniem się kolejnych liter.
LINE_PAUSE = 1.5  # Przerwa po każdym wersie.


def slowPrint(text, pauseAmount=0.1):
    """Powoli wyświetlaj znaki tekstu, tylko jeden naraz."""
    for character in text:
        # Tutaj ustaw flush=True, by tekst natychmiast wyświetlał się na ekranie:
        print(character, flush=True, end='')  # end='' oznacza brak nowej linii.
        time.sleep(pauseAmount)  # Przerwa czasowa między każdym znakiem.
    print()  # Wyświetl znak nowej linii.


print('niNety-nniinE BoOttels, autor: Al Sweigart, al@inventwithpython.com')
print()
print('(Naciśnij Ctrl+C, by zatrzymać program.)')

time.sleep(2)

bottles = 99  # To jest początkowa liczba butelek.

# Ta lista przechowuje łańcuch znaków z tekstem piosenki:
lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:  # Wyświetlaj zwrotki za pomocą pętli.
        slowPrint(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1  # Zmniejsz liczbę butelek o jeden.

        if bottles > 0:  # Wyświetl ostatnią linijkę bieżącej zwrotki.
            slowPrint(str(bottles) + lines[3], SPEED)
        else:  # Wyświetl ostatnią linijkę całej piosenki.
            slowPrint('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()  # Wyświetl znak nowej linii.

        # Wybierz losową linijkę i spraw, by jej zapis był zabawniejszy:
        lineNum = random.randint(0, 3)

        # Stwórz listę z łańcucha znaków danej linijki, by móc ją zmienić.
        # (Łańcuchy znaków w Pythonie są niezmienne).
        line = list(lines[lineNum])

        effect = random.randint(0, 3)
        if effect == 0:  # Zastąp znak spacją.
            charIndex = random.randint(0, len(line) - 1)
            line[charIndex] = ' '
        elif effect == 1:  # Zmień wielkość litery.
            charIndex = random.randint(0, len(line) - 1)
            if line[charIndex].isupper():
                line[charIndex] = line[charIndex].lower()
            elif line[charIndex].islower():
                line[charIndex] = line[charIndex].upper()
        elif effect == 2:  # Przestaw dwa znaki.
            charIndex = random.randint(0, len(line) - 2)
            firstChar = line[charIndex]
            secondChar = line[charIndex + 1]
            line[charIndex] = secondChar
            line[charIndex + 1] = firstChar
        elif effect == 3:  # Podwój znak.
            charIndex = random.randint(0, len(line) - 2)
            line.insert(charIndex, line[charIndex])

        # Zamień listę ze znakami linijki z powrotem na łańcuch znaków i dodaj go do listy z linijkami piosenki:
        lines[lineNum] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()  # Po naciśnięciu klawiszy Ctrl+C zakończ program.

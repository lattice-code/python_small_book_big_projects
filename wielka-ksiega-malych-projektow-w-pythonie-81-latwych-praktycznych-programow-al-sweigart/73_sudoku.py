"""Sudoku, by Al Sweigart al@inventwithpython.com
Klasyczna  układanka liczbowa z planszą 9x9.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Sudoku.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, zorientowany obiektowo, łamigłówka"""

import copy, random, sys

# Ta gra wymaga pliku sudokupuzzle.txt, który zawiera łamigłówkę.
# Plik możesz pobrać ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
# Oto przykład zawartości takiego pliku:
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
# 2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3
# ......9.7...42.18....7.5.261..9.4....5.....4....5.7..992.1.8....34.59...5.7......
# .3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.

# Deklaracja stałych:
EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, originalSetup):
        # Zmienna originalSetup to łańcuch 81 znaków początkowego stanu
        # planszy, z liczbami i kropkami (dla pustych pól).
        # Zobacz: https://inventwithpython.com/sudokupuzzles.txt
        self.originalSetup = originalSetup

        # Dany stan planszy sudoku jest przedstawiony za pomocą słownika
        # z kluczami (x, y) i wartością liczbową (zapisaną w formie łańcucha znaków) w
        # przypisanym do klucza miejscu.
        self.grid = {}
        self.resetGrid()  # Przywróć planszę do stanu początkowego.
        self.moves = []  # Zapisuje każdy ruch, co jest przydatne podczas korzystania z funkcji Cofnij.

    def resetGrid(self):
        """Przywraca początkowy stan planszy,
        zapisany w self.originalSetup."""
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0  # i rośnie od 0 do 80
        y = 0  # y rośnie od 0 do 8
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]
                i += 1
            y += 1

    def makeMove(self, column, row, number):
        """Umieszcza na planszy liczbę w danej kolumnie (litera od A do I)
        i danym wierszu (liczba całkowita od 1 do 9)."""
        x = 'ABCDEFGHI'.find(column)  # Zamień na liczbę całkowitą.
        y = int(row) - 1

        # Sprawdź, czy dany ruch jest wykonywany na liczbie, która jest podana na początku gry:
        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number  # Umieść tę liczbę na siatce.

        # Musimy zapisać osobną kopię słownika:
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        """Przywróć stan planszy do poprzedniego stanu
        zapisanego w liście self.moves."""
        if self.moves == []:
            return  # Brak danych w self.moves, nic nie rób.

        self.moves.pop()  # Usuń dane bieżącego stanu.

        if self.moves == []:
            self.resetGrid()
        else:
            # Ustaw poprzedni stan siatki:
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        """Wyświetl aktualny stan planszy na ekranie."""
        print('   A B C   D E F   G H I')  # Wyświetl oznaczenia kolumn.
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    # Wyświetl oznaczenia wierszy:
                    print(str(y + 1) + '  ', end='')

                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    # Wyświetl linię pionową:
                    print('| ', end='')
            print()  # Wyświetl znak nowej linii:

            if y == 2 or y == 5:
                # Wyświetl linię poziomą:
                print('   ------+-------+------')

    def _isCompleteSetOfNumbers(self, numbers):
        """Zwraca wartość True, jeśli liczby zawierają cyfry od 1 do 9."""
        return sorted(numbers) == list('123456789')

    def isSolved(self):
        """Zwraca wartość True, jeśli bieżący stan planszy to rozwiązanie."""
        # Sprawdź każdy wiersz:
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False

        # Sprawdź każdą kolumnę:
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False

        # Sprawdź każdy blok 3x3:
        for boxx in (0, 3, 6):
            for boxy in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False

        return True


print('''Sudoku, autor: Al Sweigart, al@inventwithpython.com

Sudoku to układanka liczbowa. Plansza sudoku to siatka 9x9.
Spróbuj umieścić na siatce liczby w taki sposób, by dana cyfra od 1 do 9
występowała tylko raz w danym wierszu, kolumnie i bloku 3x3.

Oto przykładowa plansza na początku gry i już rozwiązana:

    5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
    6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
    . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
    ------+-------+------     ------+-------+------
    8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
    4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
    7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
    ------+-------+------     ------+-------+------
    . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
    . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
    . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
''')
input('Naciśnij Enter, aby rozpocząć...')


# Wgraj plik sudokupuzzles.txt:
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()

# Usuń znak nowej linii na końcu każdej łamigłówki:
for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

while True:  # Główna pętla gry.
    grid.display()

    # Sprawdź, czy sudoku zostało rozwiązane.
    if grid.isSolved():
        print('Gratulacje! Rozwiązałeś łamigłówkę!')
        print('Dziękujemy za grę!')
        sys.exit()

    # Pobierz ruch gracza:
    while True:  # Pytaj, dopóki gracz nie poda prawidłowego działania.
        print()  # Wyświetl znak nowej linii.
        print('Podaj ruch lub wpisz RESET, NOWA, COFNIJ, POCZĄTEK lub KONIEC:')
        print('(Przykładowy ruch to "B4 9".)')

        action = input('> ').upper().strip()

        if len(action) > 0 and action[0] in ('R', 'N', 'C', 'P', 'K'):
            # Gracz podał prawidłowe działanie.
            break

        if len(action.split()) == 2:
            space, number = action.split()
            if len(space) != 2:
                continue

            column, row = space
            if column not in list('ABCDEFGHI'):
                print('Nie ma takiej kolumny', column)
                continue
            if not row.isdecimal() or not (1 <= int(row) <= 9):
                print('Nie ma takiego wiersza', row)
                continue
            if not (1 <= int(number) <= 9):
                print('Wybierz cyfrę od 1 do 9, a nie ', number)
                continue
            break  # Gracz podał odpowiedni ruch.

    print()  # Wyświetl znak nowej linii.

    if action.startswith('R'):
        # Przywróć planszę do stanu początkowego:
        grid.resetGrid()
        continue

    if action.startswith('N'):
        # Wgraj nową łamigłówkę:
        grid = SudokuGrid(random.choice(puzzles))
        continue

    if action.startswith('C'):
        # Cofnij ostatni ruch:
        grid.undo()
        continue

    if action.startswith('P'):
        # Pokaż początkowy stan planszy:
        originalGrid = SudokuGrid(grid.originalSetup)
        print('Na początku plansza wyglądała tak:')
        originalGrid.display()
        input('Naciśnij Enter, aby rozpocząć...')

    if action.startswith('K'):
        # Wyjdź z gry.
        print('Dziękujemy za grę!')
        sys.exit()

    # Wykonaj podany przez gracza ruch:
    if grid.makeMove(column, row, number) == False:
        print('Nie możesz nadpisać liczby, która była wpisana już na początku gry.')
        print('Wpisz POCZĄTEK, by zobaczyć planszę początkową.')
        input('Naciśnij Enter, aby rozpocząć...')

"""Wieże Hanoi, autor: Al Sweigart, al@inventwithpython.com
Łamigłówka polegająca na przekładaniu krążków.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, gra, łamigłówka"""

import copy
import sys

TOTAL_DISKS = 5  # Im więcej krążków, tym trudniejsza jest układanka.

# Na początku wszystkie krążki znajdują się na wieży A:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    print("""Wieże Hanoi, autor: Al Sweigart, al@inventwithpython.com

Przenieś krążki z jednej wieży na drugą, za każdym razem przenosząc tylko jeden krążek.
Większe krążki nie mogą leżeć na mniejszych.

Więcej informacji na stronie https://pl.wikipedia.org/wiki/Wieże_Hanoi.
"""
    )

    # Ustawienie wież. Koniec listy to wierzchołek wieży.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:  # Przeprowadź pojedynczą rundę.
        # Wyświetl wieże i krążki:
        displayTowers(towers)

        # Poproś użytkownika o podanie ruchu:
        fromTower, toTower = askForPlayerMove(towers)

        # Przenieś górny krążek z wieży fromTower na wieżę toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Sprawdź, czy użytkownik rozwiązał łamigłówkę:
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)  # Wyświetl wieże ostatni raz.
            print('Rozwiązałeś układankę! Dobra robota!')
            sys.exit()


def askForPlayerMove(towers):
    """Pyta użytkownika o ruch. Zwraca krotkę (fromTower, toTower)."""

    while True:  # Pytaj, dopóki użytkownik nie poda poprawnego ruchu.
        print('Podaj literę wieży, z której chcesz przenieść krążek, oraz literę wieży, na której chcesz umieścić krążek, lub KONIEC.')
        print('(np. AB przenosi krążek z wieży A na wieżę B.)')
        response = input('> ').upper().strip()

        if response == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        # Upewnij się, że użytkownik podał odpowiednie litery wież:
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Podaj jedną z następujących możliwości: AB, AC, BA, BC, CA lub CB.')
            continue  # Spytaj użytkownika ponownie o ruch.

        # Lukier składniowy - użycie bardziej opisowych nazw zmiennych:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # Wieża "źródłowa" nie może być pusta:
            print('Na wybranej wieży nie ma krążków.')
            continue  # Ponownie poproś użytkownika o podanie ruchu.
        elif len(towers[toTower]) == 0:
            # Każdy krążek może być przeniesiony na pustą wieżę:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Nie można kłaść większych krążków na mniejsze.')
            continue  # Ponownie poproś użytkownika o podanie ruchu.
        else:
            # Podany ruch jest poprawny, więc zwróć wybrane wieże:
            return fromTower, toTower


def displayTowers(towers):
    """Wyświetla bieżący stan wież."""

    # Wyświetl trzy wieże:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)  # Wyświetl pusty słupek.
            else:
                displayDisk(tower[level])  # Wyświetl krążek.
        print()

    # Wyświetl oznaczenia wież (A, B i C).
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """Wyświetla krążek o zadanej średnicy. Szerokość (width) 0 oznacza brak krążka."""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # Wyświetl część wieży bez krążka:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Wyświetl krążek:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


# Wywołaj funkcję main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.
if __name__ == '__main__':
    main()

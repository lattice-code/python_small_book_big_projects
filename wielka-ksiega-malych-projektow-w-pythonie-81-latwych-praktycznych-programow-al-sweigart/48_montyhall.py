"""Paradoks Monty'ego Halla, autor: Al Sweigart, al@inventwithpython.com
Symulacja paradoksu teleturnieju "Idź na całość".
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Paradoks_Monty%E2%80%99ego_Halla.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, matematyka, symulacja"""

import random, sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|KOZA|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |KOZA|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |KOZA|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| AUTO!|  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |KOZA|||  |KOZA|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | AUTO!|  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|KOZA|||  |   O  |  |KOZA|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | AUTO!|
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|KOZA|||  |KOZA|||  |   O  |
+------+  +------+  +------+"""

print('''Paradoks Monty'ego Halla, autor: Al Sweigart, al@inventwithpython.com

W tej grze możesz wybrać jedną z trzech bramek. 
Za jedną z nich kryje się nowy samochód. Pozostałe dwie kryją nic niewarte kozy:
{}
Powiedzmy, że wybrałeś bramkę #1.
Zanim otworzy się wybrana przez Ciebie bramka, otwiera się inna bramka, w której jest koza:
{}
Możesz wybrać, czy chcesz otworzyć pierwotnie wybraną bramkę,
czy zmienić swój wybór na drugą nieotwartą bramkę. 

Może się wydawać, że nie ma znaczenia, czy zmienisz swój wybór, czy nie, 
ale Twoje szanse się zwiększają, jeśli zamienisz bramkę! 
Ten program pokazuje paradoks Monty’ego Halla przez możliwość wykonania wielu powtarzalnych doświadczeń.

Szczegółowe informacje znajdziesz na stronie
https://pl.wikipedia.org/wiki/Paradoks_Monty%E2%80%99ego_Halla.
'''.format(ALL_CLOSED, THIRD_GOAT))

input('Naciśnij Enter, aby rozpocząć...')


swapWins = 0
swapLosses = 0
stayWins = 0
stayLosses = 0
while True:  # Główna pętla programu.
    # Komputer wybiera, w której bramce jest samochód:
    doorThatHasCar = random.randint(1, 3)

    # Poproś gracza o wybranie bramki:
    print(ALL_CLOSED)
    while True:  # Pytaj gracza tak długo, dopóki nie poda numeru bramki.
        print('Wybierz bramkę 1, 2 lub 3 (lub "KONIEC", by zatrzymać program):')
        response = input('> ').upper()
        if response == 'KONIEC':
            # Zakończ grę.
            print('Dziękujemy za grę!')
            sys.exit()

        if response == '1' or response == '2' or response == '3':
            break
    doorPick = int(response)

    # Znajdź bramkę z kozą, którą pokażesz graczowi:
    while True:
        # Wybierz niewskazaną przez gracza bramkę, w której jest koza:
        showGoatDoor = random.randint(1, 3)
        if showGoatDoor != doorPick and showGoatDoor != doorThatHasCar:
            break

    # Pokaż graczowi bramkę z kozą:
    if showGoatDoor == 1:
        print(FIRST_GOAT)
    elif showGoatDoor == 2:
        print(SECOND_GOAT)
    elif showGoatDoor == 3:
        print(THIRD_GOAT)

    print('W bramce nr {} jest koza!'.format(showGoatDoor))

    # Zapytaj gracza, czy chce zmienić swój wybór:
    while True:  # Pytaj tak długo, dopóki gracz nie poda albo T, albo N.
        print('Chcesz zamienić bramki? T/N')
        swap = input('> ').upper()
        if swap == 'T' or swap == 'N':
            break

    # Zmień bramkę gracza, jeśli podjął taką decyzję:
    if swap == 'T':
        if doorPick == 1 and showGoatDoor == 2:
            doorPick = 3
        elif doorPick == 1 and showGoatDoor == 3:
            doorPick = 2
        elif doorPick == 2 and showGoatDoor == 1:
            doorPick = 3
        elif doorPick == 2 and showGoatDoor == 3:
            doorPick = 1
        elif doorPick == 3 and showGoatDoor == 1:
            doorPick = 2
        elif doorPick == 3 and showGoatDoor == 2:
            doorPick = 1

    # Otwórz wszystkie bramki:
    if doorThatHasCar == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 3:
        print(THIRD_CAR_OTHERS_GOAT)

    print('W bramce nr {} jest samochód!'.format(doorThatHasCar))

    # Zapisz wygrane i przegrane w przypadku zamiany i braku zamiany bramek:
    if doorPick == doorThatHasCar:
        print('Wygrałeś!')
        if swap == 'T':
            swapWins += 1
        elif swap == 'N':
            stayWins += 1
    else:
        print('Przykro mi, przegrałeś.')
        if swap == 'T':
            swapLosses += 1
        elif swap == 'N':
            stayLosses += 1

    # Oblicz wskaźnik wygranych w przypadku zamiany i braku zamiany bramek:
    totalSwaps = swapWins + swapLosses
    if totalSwaps != 0:  # Zabezpieczenie przed dzieleniem przez 0.
        swapSuccess = round(swapWins / totalSwaps * 100, 1)
    else:
        swapSuccess = 0.0

    totalStays = stayWins + stayLosses
    if (stayWins + stayLosses) != 0:  # Zabezpieczenie przed dzieleniem przez 0.
        staySuccess = round(stayWins / totalStays * 100, 1)
    else:
        staySuccess = 0.0

    print()
    print('Zamiana:     ', end='')
    print('{} wygrane, {} przegrane, '.format(swapWins, swapLosses), end='')
    print('wskaźnik powodzenia {}%'.format(swapSuccess))
    print('Brak zamiany: ', end='')
    print('{} wygrane, {} przegrane, '.format(stayWins, stayLosses), end='')
    print('wskaźnik powodzenia {}%'.format(staySuccess))
    print()
    input('Naciśnij Enter, aby powtórzyć eksperyment...')

"""Wiadra z wodą, autor: Al Sweigart, al@inventwithpython.com
Łamigłówka polegająca na przelewaniu wody.
Więcej informacji na stronie (strona w języku angielskim) https://en.wikipedia.org/wiki/Water_pouring_puzzle.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, matematyka, łamigłówka"""

import sys


print('Wiadra z wodą, autor: Al Sweigart, al@inventwithpython.com')

GOAL = 4  # Dokładna liczba litrów w jednym z wiader, która oznacza wygraną.
steps = 0  # Zmienna przechowująca liczbę kroków wykonanych przez gracza.

# Liczba litrów w każdym wiadrze:
waterInBucket = {'8': 0, '5': 0, '3': 0}

while True:  # Główna pętla gry.
    # Wyświetl aktualną liczbę litrów w każdym wiadrze:
    print()
    print('Postaraj się uzyskać ' + str(GOAL) + ' litrów wody w jednym')
    print('z tych wiader:')

    waterDisplay = []  # Zawiera łańcuchy znaków przedstawiające wodę lub pustą przestrzeń.

    # Pobierz łańcuchy znaków dla wiadra 8 l:
    for i in range(1, 9):
        if waterInBucket['8'] < i:
            waterDisplay.append('      ')  # Dodaj pustą przestrzeń.
        else:
            waterDisplay.append('WWWWWW')  # Dodaj wodę.

    # Pobierz łańcuch znaków dla wiadra 5 L:
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append('      ')  # Dodaj pustą przestrzeń.
        else:
            waterDisplay.append('WWWWWW')  # Dodaj wodę.

    # Pobierz łańcuch znaków dla wiadra 3 l:
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append('      ')  # Dodaj pustą przestrzeń.
        else:
            waterDisplay.append('WWWWWW')  # Dodaj wodę.

    # Wyświetl wiadra z wodą:
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8 l         5 l       3 l
'''.format(*waterDisplay))

    # Sprawdź czy któreś z wiader nie ma docelowej ilości wody:
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Dobra robota! Rozwiązałeś tę łamigłówkę w', steps, 'krokach!')
            sys.exit()

    # Pozwól graczowi wybrać działanie na wybranym wiadrze:
    print('Możesz:')
    print('  (N)apełnić wiadro')
    print('  (O)próżnić wiadro')
    print('  (P)rzelać wodę z jednego wiadra do drugiego')
    print('  (K)oniec')

    while True:  # Pytaj, dopóki gracz nie poda prawidłowego działania.
        move = input('> ').upper()
        if move == 'KONIEC' or move == 'K':
            print('Dziękujemy za grę!')
            sys.exit()

        if move in ('N', 'O', 'P'):
            break  # Gracz wybrał prawidłowe działanie.
        print('Wpisz N, O, P lub K')

    # Poproś gracza o wybór wiadra:
    while True:  # Pytaj, dopóki gracz nie poda jednej z możliwości.
        print('Wybierz wiadro 8, 5, 3 lub KONIEC:')
        srcBucket = input('> ').upper()

        if srcBucket == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break  # Gracz wybrał jedną z dostępnych możliwości.

    # Wykonaj wybrane działanie:
    if move == 'N':
        # Ustaw ilość wody w wiadrze na maksymalną liczbę litrów.
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'O':
        waterInBucket[srcBucket] = 0  # Ustaw liczbę litrów na zero.
        steps += 1

    elif move == 'P':
        # Spytaj gracza, do którego wiadra chce przelać wodę:
        while True:  # Pytaj dopóki, gracz nie poda jednej z dostępnych możliwości.
            print('Wybierz wiadro, do którego przelać wodę: 8, 5 lub 3')
            dstBucket = input('> ').upper()
            if dstBucket in ('8', '5', '3'):
                break  # Gracz podał jedną z dostępnych możliwości.

        # Określ ilość wody do przelania:
        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]
        waterInSrcBucket = waterInBucket[srcBucket]
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)

        # Wylej wodę z wybranego wiadra:
        waterInBucket[srcBucket] -= amountToPour

        # Wlej wodę do drugiego wiadra:
        waterInBucket[dstBucket] += amountToPour
        steps += 1

    elif move == 'A':
        pass  # Jeśli gracz anulował ruch, nic nie rób.

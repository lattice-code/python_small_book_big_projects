"""Ciąg Fibonacciego, autor: Al Sweigart, al@inventwithpython.com
Oblicza wyrazy ciągu Fibonacciego: 0, 1, 1, 2, 3, 5, 8, 13...
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, matematyka"""

import sys

print('''Ciąg Fibonacciego, autor: Al Sweigart, al@inventwithpython.com

Ciąg Fibonacciego zaczyna się od 0 i 1, a kolejny element
jest sumą dwóch poprzednich. Ciąg nie ma końca:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

while True:  # Główna pętla programu.
    while True:  # Pytaj, dopóki użytkownik nie wpisze odpowiedniej wartości.
        print('Wpisz n-ty wyraz, do którego chcesz obliczyć ')
        print('ciąg Fibonacciego (na przykład 5, 50, 1000, 9999) lub KONIEC, by wyjść:')
        response = input('> ').upper()

        if response == 'KONIEC':
            print('Dziękujemy za grę!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # Wyjdź z pętli, gdy użytkownik poda odpowiednią wartość.

        print('Podaj liczbę większą od 0, lub KONIEC.')
    print()

    # Obsługa szczególnych przypadków, gdy użytkownik poda 1 lub 2:
    if nth == 1:
        print('0')
        print()
        print('#1 wyraz ciągu Fibonacciego to 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('#2 wyraz ciągu Fibonacciego to 1.')
        continue

    # Wyświetl ostrzeżenie, gdy użytkownik poda bardzo dużą liczbę:
    if nth >= 10000:
        print('UWAGA: Wyświetlanie wszystkich wyrazów ciągu na ekranie')
        print('zajmie chwilę. Jeśli chcesz zatrzymać program przed wyświetleniem')
        print('wszystkich elementów, naciśnij Ctrl+C.')
        input('Wciśnij Enter, by rozpocząć...')

    # Oblicz n-ty wyraz ciągu Fibonacciego:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # Wyświetl pierwsze dwa elementy ciągu Fibonacciego.

    # Wyświetl kolejne wyrazu w ciągu Fibonacciego:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # Wyświetl kolejną liczbę ciągu:
        print(nextNumber, end='')

        # Sprawdź czy znaleźliśmy n-ty element, do którego użytkownik chciał obliczyć ciąg:
        if fibNumbersCalculated == nth:
            print()
            print()
            print('#', fibNumbersCalculated, ' wyraz ciągu Fibonacciego ',
                  'to ', nextNumber, sep='')
            break

        # Wyświetl przecinek między elementami ciągu:
        print(', ', end='')

        # Przestaw ostatnie dwie liczby:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber

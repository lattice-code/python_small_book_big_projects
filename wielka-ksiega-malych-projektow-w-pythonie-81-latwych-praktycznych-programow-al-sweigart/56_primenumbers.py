"""Liczby pierwsze, autor: Al Sweigart, al@inventwithpython.com
Oblicza liczby pierwsze, które dzielą się bez reszty
tylko przez jeden i przez siebie same. 
Te liczby mają wiele praktycznych zastosowań.
Więcej informacji znajdziesz na stronie https://pl.wikipedia.org/wiki/Liczba_pierwsza.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, matematyka, przewijanie"""

import math, sys

def main():
    print('Liczby pierwsze, autor: Al Sweigart, al@inventwithpython.com')
    print('Liczby pierwsze to takie liczby,')
    print('które dzielą się bez reszty tylko przez jeden i przez siebie same.')
    print('Mają wiele praktycznych zastosowań, ale nie można ich przewidzieć.')
    print('Trzeba wykonać obliczenia, by sprawdzić, czy dana liczba jest pierwsza.')
    print()
    while True:
        print('Wpisz liczbę początkową, od której program będzie szukał liczb pierwszych:')
        print('(Spróbuj 0 lub 1000000000000 (12 zer), lub innej liczby.)')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break

    input('W każdej chwili możesz nacisnąć Ctrl+C, aby wyjść z programu. Naciśnij Enter, aby rozpocząć...')

    while True:
        # Wyświetl liczbę pierwszą:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num = num + 1  # Przejdź do kolejnej liczby.


def isPrime(number):
    """Zwraca wartość True, jeśli liczba jest pierwsza, w przeciwnym razie zwraca wartość False."""
    # Obsługa szczególnych przypadków:
    if number < 2:
        return False
    elif number == 2:
        return True

    # Daną liczbę spróbuj podzielić bez reszty przez wszystkie liczby od 2
    # do pierwiastka kwadratowego samej liczby.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

"""Bajgle, autor: Al Sweigart, al@inventwithpython.com
Logiczna gra na dedukcję, gdzie musisz odgadnąć liczbę na podstawie wskazówek.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip
Nieco inną wersję tej gry znajdziesz w książce "Twórz własne gry komputerowe w Pythonie",
https://helion.pl/ksiazki/tworz-wlasne-gry-komputerowe-w-pythonie-al-sweigart,e_0jan.htm#format/e.
Etykiety: krótki, gra, łamigłówka"""

import random

NUM_DIGITS = 3  # (!) Spróbuj ustawić tę stałą na 1 lub 10.
MAX_GUESSES = 10  # (!) Spróbuj ustawić tę stałą na 1 lub 100.


def main():
    print('''Bajgle, logiczna gra na dedukcję.
Autor: Al Sweigart, al@inventwithpython.com

Mam na myśli {}-cyfrową liczbę, która nie powtarza się żadna z cyfr. Spróbuj ją odgadnąć.
Oto wskazówki:
Gdy mówię:    Oznacza to:
  Piko         Jedna cyfra jest poprawna, ale jest na złej pozycji.
  Fermi        Jedna cyfra jest poprawna i znajduje się w odpowiednim miejscu.
  Bajgle       Żadna cyfra nie jest poprawna.

Na przykład, jeśli tajna liczba to 248, a Ty podasz liczbę 843, wskazówka będzie brzmieć
Fermi Piko.'''.format(NUM_DIGITS))

    while True:  # Pętla główna.
        # Ta zmienna przechowuje liczbę, którą gracz musi odgadnąć:
        secretNum = getSecretNum()
        print('Mam na myśli liczbę.')
        print(' Masz {} prób, by odgadnąć, jaka to liczba.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Wykonywanie pętli, dopóki gracz nie poda poprawnej liczby:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Próba #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Podana liczba jest poprawna, zakończ pętlę.
            if numGuesses > MAX_GUESSES:
                print('Wykorzystałeś wszystkie próby.')
                print('Prawidłowa odpowiedź to: {}.'.format(secretNum))

        # Zapytaj gracza, czy chce zagrać ponownie.
        print('Czy chcesz zagrać jeszcze raz? (tak lub nie)')
        if not input('> ').lower().startswith('t'):
            break
    print('Dziękuję za grę!')


def getSecretNum():
    """Zwraca liczbę złożoną z tylu losowych, unikatowych cyfr, ile wynosi wartość NUM_DIGITS."""
    numbers = list('0123456789')  # Utwórz listę cyfr od 0 do 9.
    random.shuffle(numbers)  # Ustaw je w losowej kolejności.

    # Dodaj kolejne cyfry do tajemnej liczby:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Zwraca łańcuch znaków piko, fermi, bajgle dla danej próby
    lub informację o wygranej."""
    if guess == secretNum:
        return 'Udało się!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Poprawna cyfra w odpowiednim miejscu.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Poprawna cyfra w złym miejscu.
            clues.append('Piko')
    if len(clues) == 0:
        return 'Bajgle'  # Brak poprawnych cyfr.
    else:
        # Ustaw wskazówki w kolejności alfabetycznej,
        # by ich kolejność nie zdradzała zbyt wiele informacji.
        clues.sort()
        # Wszystkie wskazówki połącz w jeden łańcuch znaków.
        return ' '.join(clues)


# Jeśli program został uruchomiony (a nie zaimportowany), uruchom grę:
if __name__ == '__main__':
    main()

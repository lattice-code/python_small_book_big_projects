"""Odgadnij liczbę, autor: Al Sweigart, al@inventwithpython.com
Spróbuj odgadnąć tajemniczą liczbę kierując się wskazówkami.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, gra"""

import random


def askForGuess():
    while True:
        guess = input('> ')  # Gracz podaje liczbę.

        if guess.isdecimal():
            return int(guess)  # Przekonwertuj podaną liczbę w formie łańcucha znaków  na liczbę całkowitą.
        print('Proszę, podaj liczbę z zakresu od 1 do 100.')


print('Odgadnij liczbę, autor: Al Sweigart, al@inventwithpython.com')
print()
secretNumber = random.randint(1, 100)  # Wylosuj liczbę.
print('Mam na myśli liczbę z zakresu do 1 do 100.')

for i in range(10):  # Przyznaj graczowi 10 szans.
    print('Masz jeszcze {} prób(y). Spróbuj odgadnąć liczbę.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break  # Wyjdź z pętli, jeśli podana przez gracza liczba jest poprawna.

    # Podaj wskazówkę:
    if guess < secretNumber:
        print('Podana przez Ciebie liczba jest za mała.')
    if guess > secretNumber:
        print('Podana przez Ciebie liczba jest za wysoka.')

# Podaj wyniki:
if guess == secretNumber:
    print('Hurra! Odgadłeś moją liczbę!')
else:
    print('Koniec gry. Liczbą, o której myślałem, jest', secretNumber,'.')

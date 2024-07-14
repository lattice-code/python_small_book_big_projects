"""Wisielec, autor: Al Sweigart, al@inventwithpython.com
Odgadnij litery ukrytego słowa, zanim program narysuje całego wisielca.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, słowo, łamigłówka"""

# Inną wersję tej gry znajdziesz w książce "Twórz własne gry komputerowe w Pythonie"
# # (Wydawnictwo PWN, Warszawa 2017).

import random, sys

# Deklaracja stałych:
# (!) Spróbuj dodać lub zmienić łańcuchy znaków zapisane w zmiennej,
# by rysunki przedstawiały gilotynę zamiast szubienicy.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# (!) Spróbuj zastąpić łańcuchy znaków w zmiennych CATEGORY i WORDS nowymi.
CATEGORY = 'Zwierzęta'
WORDS = 'MRÓWKA PAWIAN BÓBR NIETOPERZ NIEDŹWIEDŹ BORSKUK WIELBŁĄD KOT MAŁŻA KOBRA PUMA KOJOT KROWA JELEŃ PIES OSIOŁ KACZKA ORZEŁ FRETKA LIS ŻABA KOZA GĘŚ JASTRZĄB LEW JASZCZURKA LAMA MÓL MAŁPA ŁOŚ MYSZ MULE TRASZKA WYDRA SOWA PANDA PAPUGA GOŁĄB PYTON ZAJĄC OWCA SZCZUR KRUK NOSOROŻEC ŁOSOŚ FOKA REKIN BARAN SKUNKS LENIWIEC WĄŻ PAJĄK BOCIAN ŁĄBĘDŹ TYGRYS ROPUCHA PSTRĄG INDYK ŻÓŁW ŁASICA WIELBŁĄD WILK WOMBAT ZEBRA'.split()


def main():
    print('Wisielec, autor: Al Sweigart, al@inventwithpython.com')

    # Ustaw zmienne dla nowej gry:
    missedLetters = []  # Lista niepoprawnie odgadniętych liter.
    correctLetters = []  # Lista poprawnie odgadniętych liter.
    secretWord = random.choice(WORDS)  # Słowo, które gracz musi odgadnąć.

    while True:  # Główna pętla gry.
        drawHangman(missedLetters, correctLetters, secretWord)

        # Gracz podaje literę:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Dodaj poprawnie odgadniętą literę do listy correctLetters:
            correctLetters.append(guess)

            # Sprawdź, czy gracz wygrał:
            foundAllLetters = True  # Zacznij od nowa, zakładając, że gracz wygrał.
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # W ukrytym słowie jest litera,
                    # której jeszcze nie ma na liście correctLetters, więc gracz jeszcze nie wygrał:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Tak! Ukryte słowo to:', secretWord)
                print('Wygrałeś!')
                break  # Wyjdź z głównej pętli gry.
        else:
            # Gracz nie zgadł:
            missedLetters.append(guess)

            # Sprawdź, czy gracz wykorzystał już wszystkie próby i przegrał.
            # (Odejmujemy 1, ponieważ nie liczymy pustej szubienicy w liście
            # HANGMAN_PICS).
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('Wykorzystałeś już wszystkie szanse!')
                print('Ukryte słowo to: "{}"'.format(secretWord))
                break


def drawHangman(missedLetters, correctLetters, secretWord):
    """Rysuje aktualny etap wisielca wraz z listą niepoprawnie
    i poprawnie odgadniętych liter."""
    print(HANGMAN_PICS[len(missedLetters)])
    print('Kategoria ukrytego słowa to:', CATEGORY)
    print()

    # Pokaż błędnie odgadnięte litery
    print('Błędne litery: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('Nie podałeś jeszcze litery, która byłaby błędna.')
    print()

    # Wyświetl puste pola dla liter (jeden znak podkreślenia dla jednej litery):
    blanks = ['_'] * len(secretWord)

    # Zastąp puste pola poprawnie odgadniętymi literami:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Pokaż ukryte słowo ze spacją między każdą literą:
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """Zwraca podaną przez gracza literę.Funkcja upewnia się,
    że gracz wpisał tylko jedną literę, której nie podawał wcześniej."""
    while True:  # Pytaj, dopóki gracz nie wpisze poprawnej litery.
        print('Podaj literę.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Proszę, podaj tylko jedną literę.')
        elif guess in alreadyGuessed:
            print('Tę literę już podawałeś. Wpisz inną.')
        elif not guess.isalpha():
            print('Proszę, podaj LITERĘ.')
        else:
            return guess


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

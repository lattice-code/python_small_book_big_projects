"""Soroban - japońskie liczydło, autor: Al Sweigart, al@inventwithpython.com
Symulator japońskiego liczydła.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Soroban.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, matematyka, symulacja"""

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban - japoński abakus')
    print('autor: Al Sweigart, al@inventwithpython.com')
    print()

    abacusNumber = 0  # To jest liczba przedstawiana na liczydle.

    while True:  # Główna pętla programu.
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'koniec':
            # Wyjdź z programu.
            break
        elif commands.isdecimal():
            # Ustaw liczbę liczydła:
            abacusNumber = int(commands)
        else:
            # Obsługa poleceń zwiększających/zmniejszających liczbę:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        # Abakus nie może przedstawiać liczb ujemnych:
        if abacusNumber < 0:
            abacusNumber = 0  # Zamień każdą liczbę ujemną na 0.
        # Liczydło nie może przedstawiać liczb większych niż 9999999999:
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    hasBead = []  # Lista zawiera wartość True lub False dla każdej pozycji koralika.

    # Górny wiersz "nieba" ma koralik dla cyfr 0, 1, 2, 3 i 4.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01234')

    # Dolny wiersz "nieba" ma koralik dla cyfr 5, 6, 7, 8 i 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '56789')

    # Pierwszy od góry wiersz "ziemii" ma koralik dla każdej cyfry poza 0.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '12346789')

    # Drugi wiersz "ziemi" ma koraliki dla cyfr 2, 3, 4, 7, 8 i 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '234789')

    # Trzeci wiersz "ziemi" ma koraliki dla cyfr 0, 3, 4, 5, 8 i 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '034589')

    # Czwarty wiersz "ziemi" ma koraliki dla cyfr 0, 1, 2, 4, 5, 6 i 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '014569')

    # Piąty wiersz "ziemi" ma koraliki dla cyfr 0, 1, 2, 5, 6 i 7.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '012567')

    # Szósty wiersz "ziemi" ma koraliki dla cyfr 0, 1, 2, 3, 5, 6, 7 i 8.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01235678')

    # Zamień wartość True lub False na znak O lub |.
    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    # Wyświetl liczydło ze znakami O/|.
    chars = abacusChar + numberList
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def displayControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Wpisz liczbę, "koniec" lub zwiększaj/zmniejszaj liczby za pomocą liter.)')


if __name__ == '__main__':
    main()

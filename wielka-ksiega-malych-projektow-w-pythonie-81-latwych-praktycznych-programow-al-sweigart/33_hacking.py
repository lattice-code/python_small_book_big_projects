"""Łamacz haseł, autor: Al Sweigart, al@inventwithpython.com
Mini gra polegająca na łanmaniu haseł z gry "Fallout 3". Odgadnij siedmioliterowe
słowo, które jest hasłem na podstawie wskazówek, które otrzymasz po każdej próbie.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, gra, łamigłówka"""

# UWAGA: Ten program wymaga pliku sevenletterwords.txt,
# który również znajduje się w archiwum pobranym ze strony https://ftp.helion.pl/przyklady/wiksma.zip.

import random, sys

# Deklaracja stałych:
# Znaki "śmieci" do wyświetlania zawartości pamięci komputera, gdzie przechowywane są hasła.
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Wgraj listę WORDS z pliku tekstowego, w którym zapisane są siedmioliterowe słowa.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Zamień każdą literę w słowie na wielką i usuń znak końca linii:
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Uruchom prostą grę w łamanie haseł."""
    print('''Łamacz haseł, autor: Al Sweigart, al@inventwithpython.com
Odgadnij hasło zapisane w pamięci komputera. Po każdej próbie
otrzymasz wskazówkę. Na przykład jeśli tajnym hasłem jest MONITOR, a gracz podał CONTACT,
dostanie informację, że dwie spośród siedmiu liter są poprawne,
gdyż zarówno w słowie MONITOR, jak i KONTAKT
litery O i N są na drugim i trzecim miejscu. Masz cztery próby.\n''')
    input('Naciśnij Enter, aby rozpocząć...')

    gameWords = getWords()
    # Można by pominąć w tym programie zmienną computerMemory (pamięć komputera), ale wygląda fajnie:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # Zacznij od 4 prób i stopniowo odejmuj:
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('D O S T Ę P  P R Z Y Z N A N Y')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Odmowa dostępu (poprawnych {}/7 liter)'.format(numMatches))
    print('Nie ma już więcej szans. Tajne hasło to {}.'.format(secretPassword))


def getWords():
    """Zwróć listę 12 słów, które mogą być hasłami.

    Tajnym hasłem będzie pierwsze słowo z listy.
    Aby gra była sprawiedliwa, postaramy się upewnić, że na liście będą słowa
    z pewną liczbą takich samych liter jak tajne słowo."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Znajdź dwa słowa, które nie mają takich samych liter jak tajne hasło.
    # Używamy "< 3", ponieważ tajne hasło jest już na liście słów.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # Znajdź trzy słowa, które mają 3 takie same litery (ale poddaj się po 500 próbach,
    # jeśli nie znajdziesz pięciu).
    for i in range(500):
        if len(words) == 5:
            break  # Znaleziono 3 słowa, dlatego wyjdź z pętli.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Znajdź przynajmniej siedem słów, które mają przynajmniej jedną taką samą literę
    # (ale poddaj się po 500 próbach, jeśli nie znajdziesz odpowiedniej liczby słów).
    for i in range(500):
        if len(words) == 12:
            break  # Znaleziono 7 lub więcej słów, dlatego wyjdź z pętli.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # Dodaj losowe słowa, by uzyskać w sumie 12 możliwych haseł.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """Zwraca losowe słowo z listy WORDS, które nie jest na liście blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """Zwraca liczbę takich samych liter w danych dwóch słowach."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerMemoryString(words):
    """Zwraca łańcuch znaków reprezentujący "pamięć komputera"."""

    # Wybierz jedną linijkę na słowo. Jest 16 linijek,
    # ale są podzielone na pół.
    linesWithWords = random.sample(range(16 * 2), len(words))
    # Początkowy adres w pamięci (to również jest w zasadzie zbędne).
    memoryAddress = 16 * random.randint(0, 4000)

    # Utwórz łańcuch znaków przedstawiający "pamięć komputera".
    computerMemory = []  # Lista będzie zawierać 16 łańcuchów znaków, po jednym na każdą linię.
    nextWord = 0  # Indeks słowa, które zostanie umieszczone w danej linijce.
    for lineNum in range(16):  # "Pamięć komputera" ma 16 linijek.
        # Wypełnij połowę linii znakami "śmieciami":
        leftHalf = ''
        rightHalf = ''
        for j in range(16):  # Każda połowa linii ma 16 znaków.
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)

        # Wypełnij linię słowem:
        if lineNum in linesWithWords:
            # Znajdź losowe miejsce w połowie linii, by wstawić słowo:
            insertionIndex = random.randint(0, 9)
            # Wstaw słowo:
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord]
                + leftHalf[insertionIndex + 7:])
            nextWord += 1  # Weź kolejne słowo, by wstawić je w połowę linii.
        if lineNum + 16 in linesWithWords:
            # Znajdź losowe miejsce w połowie linii, by wstawić słowo:
            insertionIndex = random.randint(0, 9)
            # Wstaw słowo:
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord]
                + rightHalf[insertionIndex + 7:])
            nextWord += 1  # Weź kolejne słowo, by wstawić je w połowę linii.

        computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                     + '  ' + leftHalf + '    '
                     + '0x' + hex(memoryAddress + (16*16))[2:].zfill(4)
                     + '  ' + rightHalf)

        memoryAddress += 16  # Przeskocz, powiedzmy, z 0xe680 na 0xe690.

    # Każdy łańcuch znaków w liście computerMemory
    # jest łączony w jeden długi łańcuch znaków, który jest zwracany przez funkcję:
    return '\n'.join(computerMemory)


def askForPlayerGuess(words, tries):
    """Daj szansę graczowi, aby spróbował złamać hasło."""
    while True:
        print('Podaj hasło: (pozostały {} próby)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('Podane przez Ciebie hasło nie jest jednym z możliwych słów, podanych powyżej.')
        print('Spróbuj wpisać "{}" lub "{}".'.format(words[0], words[1]))


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

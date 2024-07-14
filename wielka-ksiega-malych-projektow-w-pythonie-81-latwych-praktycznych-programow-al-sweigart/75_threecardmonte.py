"""Gra w trzy karty, autor: Al Sweigart, al@inventwithpython.com
Znajdź damę kier po zmianie ustawienia kart.
(W rzeczywistości krupier ukrywa damę kier w dłoni,
tak byś nigdy nie wygrał).
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Trzy_karty.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra karciana, gra"""

import random, time

# Deklaracja stałych:
NUM_SWAPS = 16   # (!) Spróbuj zmienić tę wartość na 30 lub 100.
DELAY     = 0.8  # (!) Spróbuj zmienić tę wartość na 2.0 lub 0.0.

# Znaki kolorów w kartach:
HEARTS   = chr(9829)  # Znak 9829 to '♥'.
DIAMONDS = chr(9830)  # Znak 9830 to '♦'.
SPADES   = chr(9824)  # Znak 9824 to '♠'.
CLUBS    = chr(9827)  # Znak 9827 to '♣'.
# Lista kodów chr() dostępna na stronie: https://inventwithpython.com/chr.

# Indeksy listy z trzema kartami:
LEFT   = 0
MIDDLE = 1
RIGHT  = 2


def displayCards(cards):
    """Wyświetl karty w liście cards, 
    której elementami są krotki (figura, kolor)."""
    rows = ['', '', '', '', '']  # Lista z tekstem do wyświetlenia.

    for i, card in enumerate(cards):
        rank, suit = card  # Karta przedstawiona jest za pomocą krotki.
        rows[0] += ' ___  '  # Wyświetl górną krawędź karty.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))


    # Wyświetl każdy wiersz na ekranie:
    for i in range(5):
        print(rows[i])


def getRandomCard():
    """Zwraca losową kartę, która nie jest damą kier."""
    while True:  # Losuj karty, dopóki nie wylosujesz karty niebędącej damą kier.
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

        # Zwróć kartę, jeśli nie jest damą kier:
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)


print('Gra w trzy karty, autor: Al Sweigart, al@inventwithpython.com')
print()
print('Znajdź damę kier! Patrz uważnie,')
print('jak karty zmieniają swoje miejsce.')
print()

# Pokaż pierwotne ustawienie:
cards = [('Q', HEARTS), getRandomCard(), getRandomCard()]
random.shuffle(cards)  # Połóż damę kier w losowym miejscu.
print('Oto karty:')
displayCards(cards)
input('Naciśnij Enter, gdy będziesz gotowy rozpocząć grę...')

# Wyświetl zamiany:
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

    if swap == 'l-m':
        print('zamiana lewej ze środkową...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('zamiana środkowej z prawą...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('zamiana lewej z prawą...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('zamiana środkowej z lewą...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('zamiana prawej ze środkową...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('zamiana prawej z lewą...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

    time.sleep(DELAY)

# Wyświetl wiele znaków nowej linii, by ukryć zamiany.
print('\n' * 60)

# Poproś gracza o wskazanie damy kier:
while True:  # Pytaj, dopóki gracz nie poda LEWA, ŚRODKOWA lub PRAWA.
    print('Która karta to dama kier? (LEWA ŚRODKOWA PRAWA)')
    guess = input('> ').upper()

    # Pobierz indeks karty podanej przez gracza:
    if guess in ['LEWA', 'ŚRODKOWA', 'PRAWA']:
        if guess == 'LEWA':
            guessIndex = 0
        elif guess == 'ŚRODKOWA':
            guessIndex = 1
        elif guess == 'PRAWA':
            guessIndex = 2
        break

# (!) Usuń znaczniki komentarza z tej części kodu, jeśli chcesz, by gracz zawsze przegrywał:
#if cards[guessIndex] == ('Q', HEARTS):
#    # Gracz wygrał, więc zmień położenie damy kier.
#    possibleNewIndexes = [0, 1, 2]
#    possibleNewIndexes.remove(guessIndex)  # Usuń indeks elementu z damą kier.
#    newInd = random.choice(possibleNewIndexes)  # Wybierz nowy indeks.
#    # Nadaj damie kier nowy indeks:
#    cards[guessIndex], cards[newInd] = cards[newInd], cards[guessIndex]

displayCards(cards)  # Pokaż wszystkie karty.

# Sprawdź, czy gracz wygrał:
if cards[guessIndex] == ('Q', HEARTS):
    print('Wygrałeś!')
    print('Dziękujemy za grę!')
else:
    print('Przegrałeś!')
    print('Dziękujemy za grę, naiwniaku!')

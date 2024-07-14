"""Wyścig ślimaków, autor: Al Sweigart, al@inventwithpython.com
Ślimacze tempo w akcji!
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, artystyczny, dla początkujących, gra, dla wielu graczy"""

import random, time, sys

# Deklaracja stałych:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40  # (!) Spróbuj zmienić wartość tej stałej.

print('''Wyścig ślimaków, autor: Al Sweigart, al@inventwithpython.com

    @v <-- ślimak

''')

# Spytaj o liczbę ślimaków biorących udział w wyścigu:
while True:  # Pytaj, dopóki gracz nie poda liczby.
    print('Ile ślimaków weźmie udział w wyścigu? Maksymalnie:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Podaj liczbę od 2 do ', MAX_NUM_SNAILS)

# Podaj imię każdego ślimaka:
snailNames = []  # Lista z imionami ślimaków.
for i in range(1, numSnailsRacing + 1):
    while True:  # Pytaj, dopóki gracz nie poda odpowiednich imion.
        print('Podaj imię ślimaka #' + str(i))
        name = input('> ')
        if len(name) == 0:
            print('Proszę, wpisz imię.')
        elif name in snailNames:
            print('Wybierz imię, które jeszcze nie zostało użyte.')
        else:
            break  # Wpisane imię jest zaakceptowane.
    snailNames.append(name)

# Wyświetl wszystkie ślimaki na linii startu.
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'META'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)  # Pauza przed rozpoczęciem wyścigu.

while True:  # Główna pętla programu.
    # Wybierz losowego ślimaka, który ma się przesunąć do przodu:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        # Sprawdź, czy wszystkie ślimaki dotarły do linii mety:
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    # (!) EKSPERYMENT: Dodaj oszukujący kod, który zwiększa ruchy ślimaka
    # z Twoim imieniem.

    time.sleep(0.5)  # (!) EKSPERYMENT: Spróbuj zmienić wartość w nawiasie.

    # (!) EKSPERYMENT: Co się stanie, gdy przed tą linią umieścisz znacznik komentarza?
    print('\n' * 40)

    # Wyświetl linie startu i mety:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'META'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # Wyświetl ślimaki (z imionami):
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')

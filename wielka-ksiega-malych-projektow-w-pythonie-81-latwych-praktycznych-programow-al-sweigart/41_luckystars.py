"""Szczęśliwe gwiazdy, autorstwo Ala Sweigarta al@inventwithpython.com
Gra, w której trzeba mieć szczęście i aby wygrać, trzeba wyrzucić jak najwięcej gwiazdek.
Możesz rzucać tyle razy, ile tylko chcesz, ale jeśli wyrzucisz
trzy czaszki, tracisz wszystkie gwiazdki.

Gra zainspirowana grą Zombie Dice stworzoną przez Steve Jackson Games.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, gra, dla wielu graczy"""

import random

# Deklaracja stałych:
GOLD = 'ZŁOTA'
SILVER = 'SREBRNA'
BRONZE = 'BRĄZOWA'

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Szczęśliwe gwiazdy, autor: Al Sweigart, al@inventwithpython.com

Gra, w której musisz mieć szczęście, rzucając kostkami z gwiazdkami, czaszkami i pytajnikami.

Gdy nadejdzie Twoja kolej, wyciągasz trzy losowe kostki z kubka i nimi rzucasz. 
Możesz wyrzucić gwiazdki, czaszki lub pytajniki.
Gdy skończysz swoją turę, otrzymujesz jeden punkt za każdą Gwiazdkę. 
Jeśli zdecydujesz się na ponowny rzut, zatrzymujesz pytajniki i wyciągasz nowe kostki, by zastąpić czaszki i gwiazdki. 
Jeśli zbierzesz trzy czaszki, tracisz wszystkie swoje gwiazdki i kończysz kolejkę.


Gdy gracz uzbiera 13 punktów, pozostali gracze mają jeszcze jedną szansę, zanim gra się skończy. 
Wygrywa ten, kto zdobył najwięcej punktów.

W kubku jest sześć złotych kostek, cztery srebrne i trzy brązowe. 
Złota kostka ma więcej gwiazdek, brązowa więcej czaszek,  
a srebrna ma wszystkich znaków po równo.
""")

print('Ilu jest graczy?')
while True:  # Zapętlaj, dopóki gracz nie wprowadzi liczby.
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
    print('Proszę, podaj liczbę większą niż 1.')

playerNames = []  # Lista łańcuchów znaków z imionami graczy.
playerScores = {}  # Kluczami są imiona graczy, wartościami zdobyte przez nich punkty.
for i in range(numPlayers):
    while True:  # Zapętlaj, dopóki nie zostanie podane imię.
        print('Podaj imię gracza #' + str(i + 1))
        response = input('> ')
        if response != '' and response not in playerNames:
            playerNames.append(response)
            playerScores[response] = 0
            break
        print('Proszę, podaj imię.')
print()

turn = 0  # Gracz playerNames[0] będzie zaczynał.
# (!) Usuń znacznik komentarza, by gracz o imieniu Al zaczynał z trzema punktami:
#playerScores['Al'] = 3
endGameWith = None
while True:  # Główna pętla gry.
    # Wyświetl wyniki wszystkich graczy:
    print()
    print('WYNIKI: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # Po wszystkich imionach, poza ostatnim graczem, występuje przecinek.
            print(', ', end='')
    print('\n')

    # Liczba początkowa gwiazdek i czaszek to 0.
    stars = 0
    skulls = 0
    # W kubku jest 6 kostek złotych, 4 srebrne i 3 brązowe:
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []  # Na początku gracz nie ma w dłoni żadnych kostek.
    print('Teraz rzuca: ' + playerNames[turn])
    while True:  # Każdy przebieg tej pętli to rzut kostką.
        print()

        # Upewnij się, że w kubku została wystarczająca liczba kostek:
        if (3 - len(hand)) > len(cup):
            # Zakończ kolejkę, gdyż w kubku nie ma wystarczającej liczby kostek:
            print('W kubku nie ma wystarczającej liczby kostek, '
                + 'aby' + playerNames[turn]+ ' mógł kontynuować kolejkę.' )
            break

        # Wyciągaj kostki z kubka, dopóki nie będziesz miał w ręku trzech kostek:
        random.shuffle(cup)  # Zamieszaj kostki w kubku.
        while len(hand) < 3:
            hand.append(cup.pop())

        # Rzuć kostką:
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                # Rzuć złotą kostką (3 gwiazdki, 2 pytajniki, 1 czaszka):
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == SILVER:
                # Rzuć srebrną kostką (2 gwiazdki, 2 pytajniki, 2 czaszki):
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == BRONZE:
                # Rzuć brązową kostką (1 gwiazdka, 2 pytajniki, 3 czaszki):
                if roll == 1:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1

        # Wyświetl wyrzucone znaki:
        for lineNum in range(FACE_HEIGHT):
            for diceNum in range(3):
                print(rollResults[diceNum][lineNum] + ' ', end='')
            print()  # Wyświetl znak nowej linii.

        # Wyświetl rodzaj kostki (złota, srebrna lub brązowa):
        for diceType in hand:
            print(diceType.center(FACE_WIDTH) + ' ', end='')
        print()  # Wyświetl znak nowej linii.

        print('Liczba wyrzuconych gwiazdek: ', stars, '  Liczba wyrzuconych czaszek:', skulls)

        # Sprawdź, czy gracz zebrał 3 lub więcej czaszek:
        if skulls >= 3:
            print('3 lub więcej czaszek oznacza, że tracisz wszystkie swoje gwiazdki!')
            input('Naciśnij Enter, aby kontynuować...')
            break

        print(playerNames[turn] + ', czy chcesz rzucać jeszcze raz? T/N')
        while True:  # Pytaj gracza tak długo, aż poda litery T lub N:
            response = input('> ').upper()
            if response != '' and response[0] in ('T', 'N'):
                break
            print('Proszę, wpisz Tak lub Nie.')

        if response.startswith('N'):
            print(playerNames[turn], 'Twoja liczba gwiazdek to: ', stars)
            # Dodaj gwiazdki do punktacji ogólnej gracza:
            playerScores[playerNames[turn]] += stars

            # Sprawdź, czy gracz ma w sumie 13 lub więcej punktów:
            # (!) Spróbuj zmienić tę wartość na 5 lub 50 punktów.
            if (endGameWith == None
                and playerScores[playerNames[turn]] >= 13):
                # Jako że gracz uzyskał 13 (lub więcej) punktów,
                # przeprowadź jeszcze jedną rundę dla wszystkich graczy:
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' uzyskał 13 punktów!!!')
                print('Pozostali gracze mają jeszcze jedną szansę!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
            input('Naciśnij Enter, aby kontynuować...')
            break

        # Pozbądź się gwiazdek i czaszek, ale zostaw pytajniki:
        nextHand = []
        for i in range(3):
            if rollResults[i] == QUESTION_FACE:
                nextHand.append(hand[i])  # Zostaw pytajniki.
        hand = nextHand

    # Przejdź do kolejnego gracza:
    turn = (turn + 1) % numPlayers

    # Jeśli gra się skończyła, wyjdź z tej pętli:
    if endGameWith == playerNames[turn]:
        break  # Zakończ grę.

print('Koniec gry...')

# Wyświetl wyniki wszystkich graczy:
print()
print('WYNIKI: ', end='')
for i, name in enumerate(playerNames):
    print(name + ' = ' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        # Po wszystkich imionach, poza ostatnim graczem, występuje przecinek.
        print(', ', end='')
print('\n')

# Znajdź zwycięzców:
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        # Ten gracz ma najwyższy wynik:
        highestScore = score
        winners = [name]  # Nadpisz wcześniejszych zwycięzców.
    elif score == highestScore:
        # Ten gracz jest powiązany z najwyższym wynikiem.
        winners.append(name)

if len(winners) == 1:
    # Jest tylko jeden zwycięzca:
    print('Wygrał ' + winners[0] + '!!!')
else:
    # Jest więcej niż jeden zwycięzca:
    print('Wygrali: ' + ', '.join(winners))

print('Dziękujemy za grę!')

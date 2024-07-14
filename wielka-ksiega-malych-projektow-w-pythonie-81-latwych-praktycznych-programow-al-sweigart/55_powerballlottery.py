"""Loteria Powerball, autor: Al Sweigart, al@inventwithpython.com
Symulacja loterii, w której możesz doświadczyć dreszczyku
przegrywania bez utraty pieniędzy.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, zabawny, symulacja"""

import random

print('''Loteria Powerball, autor: Al Sweigart, al@inventwithpython.com

Każdy los na loterię Powerball kosztuje 2 dolary. Główna wygrana
wynosi 1586 miliardów dolarów! Jednak nieważna jest wysokość nagrody głównej,
ponieważ szanse na jej wygraną wynoszą 1 do 292201338, zatem nie wygrasz.

Ta symulacja dostarcza dreszczyku związanego z grą bez przegrywania pieniędzy.
''')

# Poproś gracza o podanie pierwszych pięciu liczb z zakresu od 1 do 69:
while True:
    print('Podaj pięć różnych, oddzielonych spacją liczb od 1 do 69.')
    print('(Na przykład: 5 17 23 42 50)')
    response = input('> ')

    # Sprawdź, czy gracz podał pięć liczb:
    numbers = response.split()
    if len(numbers) != 5:
        print('Proszę, podaj pięć liczb, oddzielonych spacją.')
        continue

    # Zamień łańcuchy znaków na liczby całkowite:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Proszę, podaj liczby, na przykład 27, 35 czy 62.')
        continue

    # Sprawdź, czy liczby mieszczą się w zakresie od 1 do 69:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('Podane liczby muszą być z zakresu od 1 do 69.')
            continue

    # Sprawdź, czy liczby się nie powtarzają:
    # (Stwórz z liczb zestaw, by usunąć duplikaty).
    if len(set(numbers)) != 5:
        print('Musisz podać pięć różnych liczb.')
        continue

    break

# Poproś gracza o podanie liczby Powerball z zakresu od 1 do 26:
while True:
    print('Podaj liczbę Powerball od 1 do 26.')
    response = input('> ')

    # Zamień łańcuchy znaków na liczby całkowite:
    try:
        powerball = int(response)
    except ValueError:
        print('Proszę, podaj liczby, na przykład 3, 15 czy 22.')
        continue

    # Sprawdź, czy liczby mieszczą się w zakresie od 1 do 26:
    if not (1 <= powerball <= 26):
        print('Podana liczba Powerball musi być z zakresu od 1 do 26.')
        continue

    break

# Spytaj gracza, ile razy chce zagrać:
while True:
    print('Ile razy chciałbyś zagrać? (Maksymalnie: 1000000)')
    response = input('> ')

    # Zamień łańcuchy znaków na liczby całkowite:
    try:
        numPlays = int(response)
    except ValueError:
        print('Proszę, podaj liczbę, na przykład 3, 15 czy 22000.')
        continue

    # Sprawdź, czy liczba mieści się w zakresie od 1 do 1000000:
    if not (1 <= numPlays <= 1000000):
        print('Możesz zagrać od 1 do 1000000 razy.')
        continue

    break

# Uruchom symulację:
price = str(2 * numPlays) + ' dolarów'
print('Musisz zapłacić', price, ', by zagrać', numPlays, 'razy,')
print('ale nie martw się. Jestem pewien, że się odegrasz.')
input('Naciśnij Enter, aby rozpocząć...')

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # Wylosuj liczby:
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # Wyświetl wylosowane liczby:
    print('Szczęśliwe liczby to: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'oraz ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')

    # UWAGA: Dane w zestawach nie są posortowane, więc kolejność
    # liczb całkowitych w set(numbers) i set(winningNumbers) nie jest istotna.
    if (set(numbers) == set(winningNumbers)
        and powerball == winningPowerball):
            print()
            print('Wygrałeś loterię Powerball! Gratulacje,')
            print('byłbyś miliarderem, gdy by to była prawdziwa loteria!')
            break
    else:
        print(' Przegrałeś.')  # Spacja na początku jest tutaj niezbędna.

print('Przegrałeś', price)
print('Dziękujemy za grę!')

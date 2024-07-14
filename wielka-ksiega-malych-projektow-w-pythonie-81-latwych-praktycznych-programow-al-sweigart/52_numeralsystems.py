"""Systemy liczbowe, autor: Al Sweigart, al@inventwithpython.com
Wyświetla liczby w systemach dziesiętnym, szesnastkowym i binarnym.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, matematyka"""


print('''Systemy liczbowe, autor: Al Sweigart, al@inventwithpython.com

Ten program pokazuje te same liczby w systemie dziesiętnym (podstawa 10),
szesnastkowym (podstawa 16) i binarnym (podstawa 2).

(Naciśnij Ctrl+C, aby wyjść z programu.)
''')

while True:
    response = input('Podaj początkową liczbę (np. 0) > ')
    if response == '':
        response = '0'  # Domyślnie zacznij od 0.
        break
    if response.isdecimal():
        break
    print('Proszę, podaj liczbę większą lub równą 0.')
start = int(response)

while True:
    response = input('Wpisz, ile liczb chcesz wyświetlić (np. 1000) > ')
    if response == '':
        response = '1000'  # Domyślnie wyświetl 1000 liczb.
        break
    if response.isdecimal():
        break
    print('Proszę, podaj liczbę.')
amount = int(response)

for number in range(start, start + amount):  # Pętla główna programu.
    # Zamień na system szesnastkowy/binarny i usuń przedrostek:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DZIESIĘTNY:', number, '   SZESNASTKOWY:', hexNumber, '   BINARNY:', binNumber)

"""Powtarzanie dźwięków, autor: Al Sweigart, al@inventwithpython.com
Gra pamięciowa z dźwiękami. Spróbuj zapamiętać coraz to dłuższe
sekwencje liter. Program inspirowany zabawką elektroniczną
Simon.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, dla początkujących, gra"""

import random, sys, time

# Pobierz pliki dźwiękowe z poniżej wymienionych adresów (lub użyj własnych):
# https://inventwithpython.com/soundA.wav
# https://inventwithpython.com/soundS.wav
# https://inventwithpython.com/soundD.wav
# https://inventwithpython.com/soundF.wav

try:
    import playsound
except ImportError:
    print('Moduł playsound musi być najpierw zainstalowany, by program')
    print('zadziałał. W przypadku systemu Windows otwórz wiersz Polecenia i uruchom:')
    print('pip install playsound')
    print('W przypadku systemu macOS i Linux otwórz terminal i uruchom:')
    print('pip3 install playsound')
    sys.exit()


print('''Powtarzanie dźwięków, autor: Al Sweigart, al@inventwithpython.com
Spróbuj zapamiętać sekwencję liter A S D F (do każdej przypisany jest inny dźwięk),
która stopniowo staje się coraz dłuższa.''')

input('Naciśnij Enter, aby rozpocząć...')

pattern = ''
while True:
    print('\n' * 60)  # Wyczyść ekran przez wyświetlenie wielu znaków nowej linii.

    # Dodaj do sekwencji losową literę:
    pattern = pattern + random.choice('ASDF')

    # Wyświetl sekwencję (i odtwórz dźwięki):
    print('Sekwencja: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound('dźwięk' + letter + '.wav')

    time.sleep(1)  # Dodaj krótką pauzę na końcu.
    print('\n' * 60)  # Wyczyść ekran przez wyświetlenie wielu znaków nowej linii.

    # Poproś gracza o powtórzenie sekwencji:
    print('Wpisz sekwencję, którą właśnie usłyszałeś:')
    response = input('> ').upper()

    if response != pattern:
        print('Źle!')
        print('Prawidłowa sekwencja to:', pattern)
    else:
        print('Dobrze!')

    for letter in pattern:
        playsound.playsound('dźwięk' + letter + '.wav')

    if response != pattern:
        print('Zdobyłeś', len(pattern) - 1, 'punktów.')
        print('Dziękujemy za grę!')
        break

    time.sleep(1)

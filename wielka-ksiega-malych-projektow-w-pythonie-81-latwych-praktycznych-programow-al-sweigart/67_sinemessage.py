"""Sinusoidalna wiadomość, autor: Al Sweigart, al@inventwithpython.com
Tworzy wiadomość o kształcie sinusoidy.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, artystyczny"""

import math, shutil, sys, time

# Pobierz rozmiar okna terminala:
WIDTH, HEIGHT = shutil.get_terminal_size()
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania nowej linii, więc zmniejsz szerokość o 1:
WIDTH -= 1

print('Wiadomość sinusoidalna, autor: Al Sweigart, al@inventwithpython.com')
print('(Naciśnij Ctrl+C, aby wyjść z programu.)')
print()
print('Jaką wiadomość chcesz wyświetlić? (Maksymalnie', WIDTH // 2, 'znaków.)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Wiadomość musi mieć od 1 do ', WIDTH // 2, 'znaków.')


step = 0.0  # Zmienna step (krok) określa, w jakim punkcie sinusoidy jesteśmy.
# Wartości sinusoidy wahają się od -1.0 do 1.0, więc musimy je zmieniać za pomocą mnożnika:
multiplier = (WIDTH - len(message)) / 2
try:
    while True:  # Główna pętla programu.
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25  # (!) Spróbuj zmienić tę wartość na 0.1 lub 0.5.
except KeyboardInterrupt:
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

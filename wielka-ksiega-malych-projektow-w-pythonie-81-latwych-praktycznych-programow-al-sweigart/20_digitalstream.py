"""Strumień cyfrowy, autor: Al Sweigart, al@inventwithpython.com
Wygaszacz ekranu w stylu wizualizacji z filmu 'Matrix'.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, artystyczny, dla początkujących, przewijanie"""

import random, shutil, sys, time

# Deklaracja stałych:
MIN_STREAM_LENGTH = 6  # (!) Spróbuj zmienić tę wartość na 1 lub 50.
MAX_STREAM_LENGTH = 14  # (!) Spróbuj zmienić tę wartość na 100.
PAUSE = 0.1  # (!) Spróbuj zmienić tę wartość na 0.0 lub 2.0.
STREAM_CHARS = ['0', '1']  # (!) Spróbuj użyć innych znaków.

# Gęstość mieści się w zakresie od 0.0 do 1.0:
DENSITY = 0.02  # (!) Spróbuj zmienić tę wartość na 0.10 lub 0.30.

# Pobierz rozmiar okna terminala:
WIDTH = shutil.get_terminal_size()[0]
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania znaku nowej linii, więc zmniejsz szerokość o 1:
WIDTH -= 1

print('Strumień cyfrowy, autor: Al Sweigart, al@inventwithpython.com')
print('Naciśnij Ctrl+C, by wyjść.')
time.sleep(2)

try:
    # Dla każdej kolumny, gdy licznik wynosi 0, nic nie jest wyświetlane.
    # W przeciwnym razie, zachowuje się jak licznik określający liczbę 1 lub 0,
    # które powinny być wyświetlone w tej kolumnie.
    columns = [0] * WIDTH
    while True:
        # Ustaw licznik dla każdej kolumny:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Zrestartuj strumień w tej kolumnie.
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)

            # Wyświetl spację lub znak 1/0.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()  # Wyświetl znak nowej linii na końcu wiersza.
        sys.stdout.flush()  # Upewnij się, że tekst pojawił się na ekranie.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

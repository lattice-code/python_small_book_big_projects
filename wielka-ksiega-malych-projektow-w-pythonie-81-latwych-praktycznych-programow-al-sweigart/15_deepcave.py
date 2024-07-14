"""Głęboka jaskinia, autorstwa Al Sweigart al@inventwithpython.com
Animacja głębokiej jaskini, która nieskończenie schodzi w głąb ziemi.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, przewijanie, artystyczny"""


import random, sys, time

# Deklaracja stałych:
WIDTH = 70  # (!) Spróbuj zmienić tę wartość na 10 lub 30.
PAUSE_AMOUNT = 0.05  # (!) Spróbuj zmienić tę wartość na 0 lub 1.0.

print('Głęboka jaskinia, autor: Al Sweigart, al@inventwithpython.com')
print('Naciśnij Ctrl+C, by zatrzymać.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Wyświetl segment tunelu:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    # Sprawdź, czy podczas krótkiej przerwy nie została naciśnięta kombinacja Ctrl+C:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zatrzymaj program.

    # Dostosuj szerokość lewej strony:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1  # Zmniejsz szerokość lewej strony.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1  # Zwiększ szerokość lewej strony.
    else:
        pass  # Nic nie rób; szerokość lewej strony bez zmian.

    # Dostosuj szerokość przerwy:
    # (!) Spróbuj usunąć znaczniki komentarza sprzed poniższych linijek:
    #diceRoll = random.randint(1, 6)
    #if diceRoll == 1 and gapWidth > 1:
    #    gapWidth = gapWidth - 1  # Zmniejsz szerokość przerwy.
    #elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
    #    gapWidth = gapWidth + 1  # Zwiększ szerokość przerwy.
    #else:
    #    pass  # Nic nie rób; szerokość przerwy bez zmian.

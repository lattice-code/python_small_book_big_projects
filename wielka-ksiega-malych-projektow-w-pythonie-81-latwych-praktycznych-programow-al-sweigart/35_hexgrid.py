"""Siatka heksagonalna, autor: Al Sweigart, al@inventwithpython.com
Wyświetla prosty rysnek siatki heksagonalnej.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip
Etykiety: króciutki, dla początkujących, artystyczny"""

# Deklaracja stałych:
# (!) Spróbuj zmienić te wartości na inne liczby:
X_REPEAT = 19  # Liczba poziomych powtórzeń.
Y_REPEAT = 12  # Liczba pionowych powtórzeń.

for y in range(Y_REPEAT):
    # Wyświetl górną część sześciokąta:
    for x in range(X_REPEAT):
        print(r'/ \_', end='')
    print()

    # Wyświetl dolną część sześciokąta:
    for x in range(X_REPEAT):
        print(r'\_/ ', end='')
    print()

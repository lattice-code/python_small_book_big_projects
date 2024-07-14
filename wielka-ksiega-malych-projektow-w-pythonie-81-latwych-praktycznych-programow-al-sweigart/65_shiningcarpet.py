"""Lśniący dywan, autor: Al Sweigart, al@inventwithpython.com
Wyświetla hipnotyzujący wzór dywanu z fimu 'Lśnienie'.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, artystyczny"""

# Deklaracja stałych
X_REPEAT = 6  # Liczba powtórzeń w poziomie.
Y_REPEAT = 4  # Liczba powtórzeń w pionie.

for i in range(Y_REPEAT):
    print(r'_ \ \ \_/ __' * X_REPEAT)
    print(r' \ \ \___/ _' * X_REPEAT)
    print(r'\ \ \_____/ ' * X_REPEAT)
    print(r'/ / / ___ \_' * X_REPEAT)
    print(r'_/ / / _ \__' * X_REPEAT)
    print(r'__/ / / \___' * X_REPEAT)

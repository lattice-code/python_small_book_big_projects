"""Bitmapowa wiadomość, autor: Al Sweigart, al@inventwithpython.com
Wyświetla wiadomość tekstową zgodnie z określoną bitmapą.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip
Etykiety: króciutki, dla początkujących, artystyczny"""

import sys

# (!) Spróbuj zmienić ten wielolinijkowy łańcuch znaków na dowolny obraz:

# Na górze i na dole łańcucha znaków jest 68 kropek:
# (Ten łańcuch znaków możesz przekopiować również ze strony
# https://inventwithpython.com/bitmapworld.txt).
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmapowa wiadomość, autor: Al Sweigart, al@inventwithpython.com')
print('Wpisz wiadomość, którą chcesz wyświetlić w postaci bitmapy.')
message = input('> ')
if message == '':
    sys.exit()

# Pętla przechodząca przez każdą linijkę bitmapy:
for line in bitmap.splitlines():
    # Pętla przechodząca przez każdy znak w linijce:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Wyświetlenie spacji w pustych polach bitmapy:
            print(' ', end='')
        else:
            # Wyświetlenie znaku z wiadomości:
            print(message[i % len(message)], end='')
    print()  # Przejście do nowej linii.

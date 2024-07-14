"""Wygaszacz z kaczuszkami, autor: Al Sweigart, al@inventwithpython.com
Wygaszacz z wieloma kaczuszkami.

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: długi, artystyczny, zorientowany obiektowo, przewijanie"""

import random, shutil, sys, time

# Deklaracja stałych:
PAUSE = 0.2  # (!) Spróbuj zmienić tę wartość na 1.0 lub 0.0.
DENSITY = 0.10  # (!) Spróbuj zmienić tę wartość na dowolną liczbę z zakresu od 0.0 do 1.0.

DUCKLING_WIDTH = 5
LEFT = 'lewo'
RIGHT = 'prawo'
BEADY = 'przenikliwe'
WIDE = 'szerokie'
HAPPY = 'wesołe'
ALOOF = 'zdystansowany'
CHUBBY = 'grubiutka'
VERY_CHUBBY = 'puszysta'
OPEN = 'otwarty'
CLOSED = 'zamknięty'
OUT = 'na zewnątrz'
DOWN = 'w dół'
UP = 'w górę'
HEAD = 'głowa'
BODY = 'ciało'
FEET = 'nogi'

# Pobierz rozmiar okna terminala:
WIDTH = shutil.get_terminal_size()[0]
# Nie możemy wyświetlić ostatniej kolumny w systemie Windows
# bez automatycznego dodania znaku nowej linii, więc zmniejsz szerokość o 1:
WIDTH -= 1


def main():
    print('Kaczuszkowy wygaszacz, autor: Al Sweigart')
    print('Naciśńij Ctrl+C, by wyjść z programu...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # Główna pętla programu.
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # Sprawdź, czy w tym pasie powinniśmy dodać kaczuszkę:
            if (ducklingObj == None and random.random() <= DENSITY):
                    # Umieść kaczuszkę w tym pasie:
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # Narysuj kaczuszkę, jeśli jest do tego pasa przypisana:
                print(ducklingObj.getNextBodyPart(), end='')
                # Usuń kaczuszkę po jej wyświetleniu:
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # Narysuj pięć spacji, jeśli w tym miejscu nie ma kaczuszki.
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # Wyświetl znak nowej linii.
        sys.stdout.flush()  # Upewnij się, że tekst został wyświetlony na ekranie.
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """Utwórz nową kaczuszkę z losowymi cechami."""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # Grubiutkie kaczuszki mogą mieć tylko przenikliwe oczy.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """Funkcja zwraca łańcuch znaków przedstawiający głowę kaczuszki."""
        headStr = ''
        if self.direction == LEFT:
            # Określ dziób:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            # Określ oczy:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '  # Określ tył głowy.

        if self.direction == RIGHT:
            headStr += ' ('  # Określ tył głowy.

            # Określ oczy:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # Określ dziób:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # Dodaj spację, by grubiutkie kaczuszki miały
            # taką samą szerokość jak pulchne kaczęta.
            headStr += ' '

        return headStr

    def getBodyStr(self):
        """Funkcja zwraca łańcuch znaków przedstawiający ciało kaczuszki."""
        bodyStr = '('  # Określ lewą stronę ciała.
        if self.direction == LEFT:
            # Określ spację w środku ciała:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # Określ skrzydło:
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            # Określ skrzydło:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # Określ spacje w środku ciała:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'  # Określ prawą stronę ciała.

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """Funkcja zwraca łańcuch znaków przedstawiający nogi kaczuszki."""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """Funkcja wywołuje odpowiednią metodę wyświetlania dla następnej części ciała kaczuszki,
        która ma być wyświetlona. Po zakończeniu przypisuje wartość None 
        zmiennej partToDisplayNext."""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()



# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.

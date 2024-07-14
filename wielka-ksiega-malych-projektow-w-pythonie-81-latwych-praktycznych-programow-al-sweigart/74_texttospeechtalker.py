"""Zamiana tekstu na mowę, autor: Al Sweigart, al@inventwithpython.com
Przykładowy program używający funkcji zamiany tekstu na mowę
modułu pyttsx3.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących"""

import sys

try:
    import pyttsx3
except ImportError:
    print('Aby uruchomić ten program, musi być zainstalowany moduł pyttsx3.')
    print('W przypadku systemu Windows otwórz wiersz polecenia i uruchom:')
    print('pip install pyttsx3')
    print('W przypadku systemów macOS i Linux otwórz terminal i uruchom:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()  # Inicjalizacja silnika TTS.

print('Zamiana tekstu na mowę, autor: Al Sweigart, al@inventwithpython.com')
print('Zamiana tekstu na mowę z użyciem modułu pyttsx3, który z kolei używa')
print('silnika NSSpeechSynthesizer (w przypadku systemu macOS), SAPI5 (Windows)')
print('lub eSpeak (Linux).')
print()
print('Wpisz tekst, który ma zostać wypowiedziany, lub KONIEC, by wyjść z programu.')
while True:
    text = input('> ')

    if text.upper() == 'KONIEC':
        print('Dziękujemy za skorzystanie z programu!')
        sys.exit()

    tts.say(text)  # Prześlij tekst do silnika TTS.
    tts.runAndWait()  # Spraw, by silnik TTS wypowiedział ten tekst.

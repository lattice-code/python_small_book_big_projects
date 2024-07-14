#copyright stuff:
"""Bajgle, autor: Al Sweigart, al@inventwithpython.com
Logiczna gra na dedukcję, gdzie musisz odgadnąć liczbę na podstawie wskazówek.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip
Nieco inną wersję tej gry znajdziesz w książce "Twórz własne gry komputerowe w Pythonie",
https://helion.pl/ksiazki/tworz-wlasne-gry-komputerowe-w-pythonie-al-sweigart,e_0jan.htm#format/e.
Etykiety: krótki, gra, łamigłówka"""


import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
	print('''Bajgle logic game on deduction.
	Author: Al Sweigart, al@inventwithpython.com
	
I have in mind a {}-digit number, which has every number is different. Try to guess it.
Tips are:
When I say:			It means:
Piko				One of numbers is right but on wrong place.
Fermi				One of number is right and on right place.
Bajgle				None of numbers is right.

'''.format(NUM_DIGITS))


	while True :
		secretNum = getSecretNum()
        print(' ')
		print('You have {} tries to guess.'.format(MAX_GUESSES))
		
		numGuesses = 1
		while numGuesses <= MAX_GUESSES:
			guess = ''
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print('Try #{}: '.format(numGuesses))
				guess = input('> ')
				
			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1
			
			if guess == secretNum:
				break
			if numGuesses > MAX_GUESSES:
				print('Already used all your tries.')
				print('The number was : {}'.format(secretNum))
				
		print('Would you like to play again? (y/n)')
		if not input('> ').lower().startswith('y'):
			break
		print('Thanks for the game.')
		
def getSecretNum():
	numbers = list('0123456789')
	random.shuffle(numbers)
	
	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum
	
def getClues(guess, secretNum):
	if guess == secretNum:
		return 'You got this!'
		
	clues = []
	
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi')
		elif guess[i] in secretNum:
			clues.append('Piko')
	if len(clues) == 0:
		return('Bajgle')
	else:
		clues.sort()
		return ' '.join(clues)
		
		
if __name__ == '__main__':
	main()

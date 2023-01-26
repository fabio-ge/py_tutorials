from random import randint
from math import log

def usage():
	print("""
		Welcome to guess the number game.
		I think a number and yuo try to guess. Ready?
		""")

def secret_number():
	max_number = int(input("give me the max number i can think of "))
	secret_number = randint(1,max_number)
	tries = int(log(max_number,2))
	print(f"you have {tries} trials to guess")
	return (secret_number,tries,max_number)


def take_guess(max):
	guess = input("try to guess the number ")
	if guess.isdecimal(): 
		resp = int(guess)
		if resp >=1 and resp <= max:
			return resp
	print(f"please enter a valid number between 1 and {max}")
	return take_guess(max)

def play(secret,tries,max):
	while tries > 0:
		guess = take_guess(max)
		if guess == secret:
			print(f"Congratulations, you won. {guess} is the right number")
			break
		elif guess < secret:
			print("My number is bigger")
			tries -= 1
		else:
			print("My number is smaller")
			tries -=1

	if tries == 0:
		print("Sorry, you lose")
		

def main():
	usage()
	(secret,tries,max) = secret_number()
	play(secret,tries,max)

if __name__ == '__main__':
	main()

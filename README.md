# GUESS THE NUMBER AND PYTHON FUN

becoming fluent in a programming language is often a matter of practice and having fun while doing practice.
So, shall we try with a simple game in which are involved most of the programming features you'll need to use on daily basis.
The perfect candidate for this is a game called guess the number; if you don' t know what i'm speaking of, continue on reading.
The fact is that, even trying to do a simple thing like this, involves a certain number of topics. So, as we don' t have particular constraints for doing this, we can take this opportunity to make interesting digressions on important computer science topics.
To give only a brief example in this article we'll speak of recursion, binary search, time complexity, sorting algorithms and powerful, one-liners, pieces of code.
So, if this is in your taste, stay with us. To have your appetite even wetter, go seeing the list of [inspiring readings](#bib), at the bottom of this article.

## Table of contents

- [The game: guess the number](#game)
- [Why matters in learning a language?](#matters)
- [Top down approach](#top-down) 
- [Implementing in python](#implement)
    - [code](#code)
	- [comment](#comment)
- binary search and why is involved
- How to search for something
	- linear search
	- binary search
- How mich does it cost? Alghortims complexity
    - compute complexity
	- differences with linear search
	- a rocket man example (grokking algorithms)
- The importance of being ordered
	- sorting algorithms
		- selection sort
		- quick sort
		- wow, only in one line?
			- binary search
			- quick sort

<span id="game"></span>
### **The game**

The simple game chosen for this example is guess the number.
You must decide an upper bound (depending on this you have a max number of trials) and try to guess a secret number the computer is thinking. The number is between one and the upper bound chosen. For every trial your possibilities decrease by one. If your guessing number is greater than the secret one the computer say something like "Too high, try a smaller one". Same for the inverse situation with an appropriate message.
If you go to zero trials before guessing the number you lose. If your guess matches the number thought you win. Pretty simple, isn't it?

<span id="matters"></span>
### **Why matters in learning a language?**

This is really a simple game, so we bother with it? Simply because it involves a lot of topics you have to master if you want to become proficient in a language.
First of all you must be able to handle input inserted via a keyboard. Obviously you have to become familiar of the more convenient way to print things on the screen. You need to know how to write conditional instructions and preparing a loop that lasts until a predefined condition is reached.
And, as will see in a moment, a lot of more complicated subjects.
So, the more important thing is that you learn to think computationally in your language of choice, while implementing this simple game.

<span id="top-down"></span>
### **Top down approach**

There are, potentially, multiple ways to handle a challenge. Just to be specific i want to afford this particular one starting with a top down approach of the task we must handle for completing our homework.
I' ll write a very basic (top-down) instructions just to have a path to follow. This is the global vision of the problem, from my point of view.
- print some instructions to the player
- ask the player the max number i can think
- calculate a secret number between 1 and max
- calculate the max number of trials the player has and saying this number to him
- start a loop in which
	- ask a guess to the player
	- if the number is right player won
	- if is bigger or smaller give a hint
	- if number of trials is 0 the player lose

<span id="implement"></span>
### **Implementing in python**

#### **code**
```python
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

```

#### **comment**

First of all you see that the code is uncommented. This is not a practice i recommend. In this case i thought it was clearer to have the bare code in one place and write every useful comment in this section. If this section hadn' t been here it would have been a real terrible idea.
The style of the program is functional. Everything is achieved by function that are joined together in a main function. This very last function is invoked when the program run as a standalone piece of software. If you have a command line in your os, and go to the dir in which this file is saved, you can invoke the program running python guess_the_number.py (supposing you have saved the file with this name and you have the python interpreter already installed). The program immediately recognize that the instruction if __name__ == '__main__' is true, and execute the main function defined above.
The first step of the main function is to invoke another function that take care of printing some instructions to the user. Nothing too complicated.
After this, from the main function perspective, another function is invoked, the secret_number.
This function read an input (by the "input" instruction) via the keyboard and cast it to an integer (int() do the dirty job). Then the function, using the randint imported at the top of the file, calculate a random number and, depending on the max number choosen by the player compute the number of trials available. This is accomplished using the log function from the math library. The import is at the top of the file and the reason why we use the log function will be clear in the next section.
The function returns three useful informations stored in a tuple: the secret number, the max number of trials and the upper bound.
With these information as arguments we can now invoke the play function, responsible for the central loop of the game.
Inside this loop the player is being asked to enter a number and the input is validated by the function take_guess that checks the rightness of the input inserted.
Perhaps the most interesting stuff in this function is that, if the input is wrong, the function call itself recursevely, until a right input is inserted.This is done by this piece of code: return take_guess(max)
If there's something wrong there's a message for asking the player another number between the bounds allowed.
If the number in input is right the program check if the player has won, otherwise print an hint and decrement the number of trials.
If no right guess is made until the trials reach 0, the player lose.



<span id="bib"></span>
### Inspiring
- *Grokking algorithms, Aditya Y. Bhargava, Manning 2016*
- *Python oneliners, Christian Mayer, No starch press 2020*
- *A common sense guide to data structure and alghoritms, Jay Wengrow, Pragmatic bookshelf 2020*
- *The big book of small python projects, Al Sweigart, No starch press 2021*
- *Tiny python projects, Ken Youens-Clark, Manning 2020* 
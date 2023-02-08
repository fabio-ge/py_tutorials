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
- [binary search and why is involved](#bs)
	- [How to search for something](#how)
		- [linear search](#ls)
		- [binary search](#bscode)
	- [likelyhood of winning](#prob)
	- how to compute with monte carlo method
- How much does it cost? Alghorithms complexity
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

<span id="bs"></span>
### **Binary search and why is involved**

In the previuos section we told about how to decide the number of trials available to the player,
and i promised you to reveal why, to compute this value, i have used the log function.
Well, the short answer is that there is a strategy that the player can adopt, to certainly win the game, if the number of trials are gretar than log2 of the maximum number allowed.

<span id="how"></span>
#### **How to search for something**
Let's see if we can clarify this thing of searching. If you have to search for a number between 1 and 100 which strategy will you adopt? Make sure to have an answer and then read on.
I think the brute (or stupid) way of accomplish this task is going in order, a number after the other. So we can check: is the number 1? No,is greater. Ok, is 2? No, is gretare. Ok is 3? And so on. But maybe you would try a smarter approach and your first guess will probably be a number in the middle.
Is the number 50? No. is smaller. Now, i hope, you wouldn't say is 49, but maybe is the number 25? No is greater. Ok Now we have a really smaller set of number to guess.
The same for a dictionary. You can search for a word browsing all the pages of the dictionary in order and see if the searched word is in that page.
But, if the word you are searching is, for example, "semantic", is not a real clever approach. So you'll probabily open the dictionary in a point near the initial letter searched, and then you go right or left if the word is before or after in the alfabet.
Ok, that's enough for a common sense approach, but still very important, anyway.
Now is time to tell you about linear and binary search, the formal implementation of the topics just discussed.

<span id="ls"></span>
#### **linear search**

There' s no particular mistery in linear search. Suppose you have an array of number and you must search for a value. Here is the code to do this.


```python
def ls(array,search_value):
	for ar_index,ar_value in enumerate(array):
		if ar_value == search_value:
			return ar_index
	return -1

def main():
	ar = range(1,101)
	print("Searching a value between 1 and 100")
	search_val = int(input("Give me a value for which you want to search> "))
	## i assume the input is valid
	found_index = ls(ar,search_val)
	if found_index > -1:
		print(f"The searched value is at index {found_index}")
	else:
		print("Value not found")

if __name__ == '__main__':
	main()

```

The ls function, responsible for the search, is really straightforward, and maybe a little stupid. It scans the number of an array one after the other, and make a comparison. If the check results in a success comparison, it returns the index of the position of the value in the array, otherwise, if the end of the array is reached, a main convention for the searching function suggest to return a -1, that is to say "i have not found the value".
This simple program is only for explanation purposes and if we took count of the number of trials in which the function find the searched value it will be the number of numbers before the searched values. Not really the more convenient way to search. And now, for something completely different, I introduce a friend of mine...

#### **binary search**

I prefer to introduce first the code

```python
def bs(ar,val):
	lower,upper = (0,len(ar)-1)
	while lower <= upper:
		mid = lower + (upper -lower)//2
		if ar[mid] == val:
			return mid
		elif ar[mid] > val:
			upper = mid - 1
		else:
			lower = mid + 1
	return -1
```
Now that you understand the main point I omit the code in which, simply, I try to execute the code to see that it works
and i give you only the function.
The code is simply: assumed that the array in which i have to search for a particular value is ordered (this is essential) i try the value in the middle. If this is the searched value the function returns the index, otherwise, if the value is greater, the function can eliminate all the values on the right and now does't have to examine all the values but only the values on the left.
If the value is lesser this means that the value searched is in the right part of the array.
The function continues until the lower value, from which starting the search is greater than the upper value. In that case the while is interrupted and -1 is returned, because the value isn' t in the array.
To make an example, suppose we want to search if the array [1,2,3,4,5,6,7,8,9,10] has the value 3.
We start with a lower index of 0 and and upper index of 9.
The index in the middle is = 4 and the value at that index is 5. The searched value is 3, lesser than 5, so wen can eliminate all the numbers on the right, 5 included.
So the array now is this [1,2,3,4~~5,6,7,8,9,10~~] and the upper bound become 3. The middle point now is 2, which value is 3. So the function returns the index 2, and this is the answer to our question.

<span id="prob"></span>
#### **Likelyhood of winning**
Why all these considerations matters in this simple game?
The answer is that, in the way the game is considered, is important not to have a big number of trials, because after a certain value, if the player applies binary search, is matematically sure that he'll guess the number.
So the number of trials are established in a range under the mathematical certainty. It would be nice if the likelywood would be something near 50%, so how we can decide the number of trials?
If we have numbers from 1 to 10, and we have to guess a number, is 3 a good amount of trials.
3 is integer part of the base 2 logarithm of 10. What if I give the player 5 trials. If the player applies binary search, with 5 trials, cannot loose. In fact, with the first guess, if wrong, remain 5 numbers to guess. Than, with the second guess, if wrong, remain 2 numbers to guess and 3 other trial. Math clearly says that the player wins. If we limited the number of trials to 3, after 2 trials we remain with 2 numbers and, at the point, the probability is 50% to guess.
Ok, it sounds nice, but is there another proof that our argomentation is right? Because we are walking in the forest of programming let's try an answer with a monte carlo method.





<span id="bib"></span>
### Inspiring
- *Grokking algorithms, Aditya Y. Bhargava, Manning 2016*
- *Python oneliners, Christian Mayer, No starch press 2020*
- *A common sense guide to data structure and alghoritms, Jay Wengrow, Pragmatic bookshelf 2020*
- *The big book of small python projects, Al Sweigart, No starch press 2021*
- *Tiny python projects, Ken Youens-Clark, Manning 2020* 
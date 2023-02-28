# GUESS THE NUMBER AND PYTHON FUN

becoming fluent in a programming language is often a matter of practice and having fun while doing practice.
So, shall we try with a simple game in which are involved most of the programming features you'll need to use on daily basis.
The perfect candidate for this is a game called guess the number; if you don' t know what i'm speaking of, continue on reading.
The fact is that, even trying to do a simple thing like this, involves a certain number of topics. So, as we don' t have particular constraints for doing this, we can take this opportunity to make interesting digressions on important computer science topics.
To give only a brief example in this article we'll speak of recursion, binary search, time complexity, sorting algorithms and powerful, one-liners, pieces of code.
So, if this is in your taste, stay with us. To have your appetite even wetter, go seeing the list of [inspiring readings](#bib), at the bottom of this article.

<span id="top"></span>

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
	- [how to compute with monte carlo method](#mc)
- [How much does it cost? Alghorithms complexity](#complex)
    - [compute complexity](#compute)
	- [differences with linear search](#diff)
- [The importance of being ordered](#order)
	- [sorting algorithms](#sort)
		- [selection sort](#selsort)
		- [quick sort](#quicksort)
		- [wow, only in one line?](#oneliners)
			- [binary search](#bsoneline)
			- quick sort

<span id="game"></span>
### **The game**

The simple game chosen for this example is guess the number.
You must decide an upper bound (depending on this you have a max number of trials) and try to guess a secret number the computer is thinking. The number is between one and the upper bound chosen. For every trial your possibilities decrease by one. If your guessing number is greater than the secret one, the computer says something like "Too high, try a smaller one". Same for the inverse situation with an appropriate message.
If your numbers of trials go to zero before you guess the number, you lose. If your guess matches the number thought you win. Pretty simple, isn't it?

<span id="matters"></span>
### **Why matters in learning a language?**

This is really a simple game, so why do we bother? Simply because it involves a lot of topics you have to master if you want to become proficient in a language.
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
- calculate the max number of trials for the player
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
		I think a number and you try to guess. Ready?
		""")

def secret_number():
	max_number = int(input("give/ me the max number i can think of "))
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
Perhaps the most interesting stuff in this function is that, if the input is wrong, the function call itself recursively, until a right input is inserted.This is done by this piece of code: return take_guess(max)
If there's something wrong there's a message for asking the player another number between the bounds allowed.
If the number in input is right the program check if the player has won, otherwise print an hint and decrement the number of trials.
If no right guess is made until the trials reach 0, the player lose.

<span id="bs"></span>
### **Binary search and why is involved**

In the previuos section we told about how to decide the number of trials available to the player,
and i promised you to reveal why, to compute this value, i used the log function.
Well, the short answer is that there is a strategy that the player can adopt, to win the game for sure, if the number of trials are greater than log2 of the maximum number allowed.

<span id="how"></span>
#### **How to search for something**
Let's see if we can clarify this thing. If you want to search for a number between 1 and 100 which strategy will you adopt? Make sure to have an answer and then read on.
I think the brute (or stupid) way of accomplish this task is going in order, a number after the other. So we can check: is the number 1? No,is greater. Ok, is 2? No, is greater. Ok is 3? And so on. But maybe you would try a smarter approach and your first guess will probably be a number in the middle.
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

The ls function, responsible for the search, is really straightforward, and maybe a little stupid. It scans the number of an array one after the other, and make a comparison. If the check results in a success comparison, it returns the index of the position of the first value in the array, otherwise, if the end of the array is reached, a main convention for the searching function suggest to return a -1, that is to say "i have not found the value".
This simple program is only for explanation purposes and if we took count of the number of trials in which the function find the searched value it will be the number of numbers before the searched values. Not really the more convenient way to search. And now, for something completely different, I introduce a friend of mine...

#### **binary search**

code first

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
The code is simply: assumed that the array in which i have to search for a particular value is ordered (this is essential) i try the value in the middle. If this is the searched value the function returns the index, otherwise, if the value is greater, the function can eliminate all the values on the right and now doesn't have to examine all the values but only the values on the left.
If the value is lesser this means that the value searched is in the right part of the array.
The function continues until the lower value, from which starting the search is greater than the upper value. In that case the while is interrupted and -1 is returned, because the value isn' t in the array.
To make an example, suppose we want to search if the array [1,2,3,4,5,6,7,8,9,10] has the value 3.
We start with a lower index of 0 and and upper index of 9.
The index in the middle is = 4 and the value at that index is 5. The searched value is 3, lesser than 5, so wen can eliminate all the numbers on the right, 5 included.
So the array now is this [1,2,3,4,~~5,6,7,8,9,10~~] and the upper bound become 3. The middle point now is 1, which value is 2, less than 3, so we can eliminate the left side [~~1,2~~,3,4]. Now the lower index is 2 and the upper is 3. Middle point index is 2 and the value is 3, and this is the answer to our question. The searched element exists and the index in the array is 2.

<span id="prob"></span>
#### **Likelyhood of winning**
Why all these considerations matters in this simple game?
The answer is that, in the way the game is considered, is important not to have a big number of trials, because after a certain value, if the player applies binary search, is matematically sure that he'll guess the number.
So the number of trials are established in a range under the mathematical certainty. It would be nice if the likelywood would be something near 50%, so how we can decide the number of trials?
If we have numbers from 1 to 10, and we have to guess a number, is 3 a good amount of trials?
3 is integer part of the base 2 logarithm of 10. What if I give the player 5 trials. If the player applies binary search, with 5 trials, cannot lose. In fact, with the first guess, if wrong, remain 5 numbers to guess. Than, with the second guess, if wrong, remain 2 numbers to guess and 3 other trial. Math clearly says that the player wins. If we limited the number of trials to 3, after 2 trials we remain with 2 numbers and, at that point, the probability is 50% to guess.
Ok, it sounds nice, but is there another proof that our argomentation is right? Because we are walking in the forest of programming let's try an answer with a monte carlo method.

<span id="mc"></span>
#### **how to compute with monte carlo method**

What' s a monte carlo method? To stay at our example, we want to compute a probability but, may be we are not so confident in math, or maybe we are but we want a counterproof also. So we can write a little program that is basically a simulation. Instead of playing only one game our simulation can play 100000 games in a row, and can do these multiple times. If every time the program run 1000000 simulations the results is near the other result we have choosen a sufficient enough amount of repetitions. If the results are really far one from the other, maybe randomness still plays a huge role. To eliminate this component we have to increase the number of games, until, with a sufficient amount, randomness is cut off from the equation. It's the same with a coin toss. If we throw the coin 10 times, the result may be unpredictable, but if we throws the coin 100000 times, the percentage of times the throw gives you a head will be something near 50%.
Monte Carlo method is really a fascinating method and can be used to compute hard to figure out probability. For example: do you know the monty hall problem? You can choose between three envelope. In one of them you can win a car, in the others two you win nothing. After you have choosen an envelope a person show you the content of one of the others two envelope that doesn' t contain the car.Is it more convenient for you to change your choice or to remain with the initial envelope?
This is not a difficult question, but it is tricky and if you have not thought about it, a common sense reasoning will probably lead you to a wrong conclusion. The point is that, with a monte carlo simulation, you can easily figure out the right answer, and writing the code for this is really simple (maybe is a good exercise for the reader). I like when code helps to answer to real world problems :-)
So, without further ado, here it is the code for the monte carlo simulation for our problem.

```python
from random import randint

MAX_NUMBER=100
TRIALS=6
MATCHES=100000
ITERATION=20

def bs_with_trials(ar,val):
	trials = 0
	lower,upper = (0,len(ar)-1)
	while lower <= upper:
		mid = lower + (upper -lower)//2
		trials += 1
		if ar[mid] == val:
			return trials
		elif ar[mid] > val:
			upper = mid - 1
		else:
			lower = mid + 1
	return trials

def single_match_win():
	secret_number = randint(1,MAX_NUMBER)
	array = range(1,MAX_NUMBER)
	return bs_with_trials(array,secret_number) <= TRIALS

def main():
	for i in range(ITERATION):
		win = 0
		for single_match in range(MATCHES):
			if single_match_win():
				win += 1
			
		print(f"In this simulation i played {MATCHES} matches, and i win {win} times. I have a {int((win/MATCHES)*100)} % of success.")


if __name__ == '__main__':
	main()
```
If you try to run this code you will see that you win with a probability of 62, 63% in which of the 20 simulation. For each simulation you play 100000 games and the results are almost identical, so i can trust these results. This means that if you have to guess a number between 1 and 100, 6 is a good amount of trials. What if the game gives you only 5 trials. The beauty of this method is that, now, we can modify the constant  at the top of the program and immediately see the result. 30% of success, in my opinion too low. So, let's try with 7. 100% of success. Ok, in this case, is too much. So a perfect balance will be 6 trials.
Remember that the assumption is that the player is using the best possible strategy to guess the number which is binary search.
Let's do a last experimentation: what if we modify the max number to be 128. The integer part of the base 2 logarithm of 128 is 7 and, if you run your simulations you see that you win 100 times out of 100.
Why? The answer is simple: 128 is an exact power of 2. So the logarithm will be the exact number of times you have to divide the numbers until you reach the only possible solution. The things are different, for example, with the max number equals to 100 because the base 2 log of 100 is 6,64... which is rounded to 6 by the // python operator (an integer division).
So the numbers of trials aren't enough to have a mathematical probability of the 100%. If this is a bug in your game and you have to calculate the number of trials in a different way or a reward to the smart enough player who choose, for the max, an exact power of two, is your decision. In my opinion, the only thing to say is this: "It's not a bug, it's a feature" 

<span id="complex"></span>
### **How much does it cost? Alghorithms complexity**

What the hell is this section? It concerns a very important topic in computer science: performance, but don't be too scaried, is not a very formal approach.
What is the complexity of an algorithm? The simpler way to explain is thinking how much time the algorithm need to run and how this time is related to the input of the algorithm. There are other measures of the complexity (space is an example), but for our purposes we limit our consideration to the time complexity.
So the question of the questions: how do we measure this time complexity of an algorithm?

<span id="compute"></span>
#### **compute complexity**

Let' s start with a simple statement: to compute the complexity of an algorithm we must count the numbers of operation the algorithm need to do to accomplish the task.
Yes but... what about the time? Is irrelevant. What? Yes, the only important thing is the number of operations. So let' s do an example: if we have an array and, for each element we print its value, we have an operation for every element of the array. With an array of n elements we have n operations, k with an array of k elements.
The important thing is that, if you increase the size of your input, the time of the array will increase in a linear proportional way. So doubling the size of the array will result in a double time to finish.
To be just a little bit more formal we can say that the time complexity of the algorithm is n (is linear) and we write     O(n), read as big o of n.
What if i tell you that the difference between linear search and binary search is that, if i double the input, one doubles its time complexity while the other increment by one the number of operations, so that this size increasing is almost irrelevant.  


<span id="diff"></span>
#### **Differences between linear search and binary search**
 Yes, this is precisely our difference: linear search is O(n), while binary search is O(log n).
 Let' s do an example: imagine you write an algorithm that search is a friend is present in the facebook archive. To search for your friend you use linear search. Facebook, now at the very beginning of its life, is composed of 100 users. You need to do, in the worst case (if your friend is the last or if is not present), 100 operations. If the pc you use has the capability to do 1000 operations in a second, your algorithm will spend a tenth of a second to give you the answer. If your implementation change, and you switch to binary search, the number of operations become 7, and the time is now, for sake of semplicity, a thousandth of second, so 100 times smaller.
 Now you think carefully about this and because linear search is really easy to implement and not error prone as binary search is, you decide to keep the one with the linear search implementation.
 The difference between the tow is really not that big. 
 A year later you want to repeat this search: maybe my friend has subscribed facebook now. The users, now, are a million.
 Wow, a huge increase. So my algorithm need a million/1000 seconds. To have an answer i have to wait for 17 minutes. With binary search, the number of operations needed are log2(1000000) = 19, so we are still under a second.
 The point is that, for small numbers, the two algorithms are both good, but for big numbers there's a huge difference. The other key point is this: with 100 users the difference between the tow is 1 to 100.
 But with a million users the difference has no more this proportion. Is more 1000000 to 1. So the performance ratio between the two algorithm is not constant, increase as the input number become bigger.

 <span id="order"></span>

 ### **The importance of being ordered**

 Now, considering that this is a free digression on topics related to our simple game implementation in python, i think it's time to consider a very important one: order. All discussions made until now, and even our game, is based on the fact that the number i'm searching for is in an ordered list of numbers. The dictionary can be searched in an effective way because is ordered: but what about an unordered list of things? Well, you simply can't make a good search. You have to deal with the one by one kind of searching we told speaking of linear search.
 Don't be too desperate because there's a family of useful algorithms with the purpose of ordering a list of things, given an ordering criterium.
 The simplest one is the <. A number a is before a number b if a < b. That's all.
 We stick with this, but other criteria, like lexycographical, are possible.

<span id="sort"></span>
 #### **Sorting algorithms**
As we told few lines ago there are a bunch of algorithms to make order in an unordered collections of any kind of types. The classic example is an array of unordered integers. A good one would be [1,7,3,2,9,4,10,5]. A sorting algorithm will receive this array or list as argument and will return a new array [1,2,3,4,5,7,9,10]
Sorting algorithms are perhaps the most classical example in the realm of algorithms and there are really a lot of this kind. To mention only a few: bubble sort, selection sort, insertion sort,merge sort, quick sort, heap sort.
There are difference between them, tipically related to the time complexity (the big O thing), so one is better than others. Bubble sort has a complexity of O(n^2), so is not a suitable choice if you must order a big array.
In this case may be merge sort is a better choice. In addition some implementations are clearer and more straightforward than others. So, to keep things simple, i chose 2 algorithms of different time complexity and with an easy implementation: selection sort and quick sort.
Let's begin with the first one.


 <span id="selsort"></span>
#### **Selection sort**

Code first. Now you're an expert, so try to figure out what this code does and then read on.

```python
def find_min_index(l):
    """
        find the index of the min element of the array
        @input l starting list
    """
    min_index = 0
    min_el = l[0]
    for i,v in enumerate(l):
        if v < min_el:
            min_el = v
            min_index = i

    return min_index

def selection_sort(l):
	"""
		order a list of numbers returning a new array
		@input l list of numbers
	"""
    #make a copy of the list to left the original untouched
    ordered_list = l[:]
    for index,el in enumerate(ordered_list):
        ## new list to examin, start from the new index
        new_list = ordered_list[index:]
        new_min_index = find_min_index(new_list)
        ordered_list[index],ordered_list[index+new_min_index] = ordered_list[index+new_min_index] ,ordered_list[index]

    return ordered_list
```
In the first function, find_min_index, the top part between """""" is a documentation string. It tells us what the function does and its parameters.
In selection sort, first of all, we make a copy, so the originally array is safe. Otherwise ordering the list will also modifiy the original and may be this is not the intended behaviour.
Then, for every element of the list create a sublist with all the element on the right of the actual element, which is included. In this new_list the min el is searched and then the funcion makes a swap between the actual element and the min one in the new sub_list. At the end of this loop ordered_list is really ordered and can be returned from the function.

<span id="quicksort"></span>
#### **Quick sort**

Quick sort is one of my favourite algorithms. May be you feel strange in listening to me sayng I have a preference about a specific algorithm, but this is how the world goes, at least for a software developer.
There are good reasons to love quick sort. It's a linear, simple and pretty fast algorithm. Here, there's the code.

from random import randint

```python
def quick_sort(l):
	"""
		Sort a given list
		
		@input l list to order
	"""
	if len(l) <= 1:
		return l

	greater,smaller = [],[]
	rand_index = randint(0,len(l)-1)
	pivot = l[rand_index]
	for i,el in enumerate(l):
		if el <= pivot: ##if is smaller 
			if i != rand_index: ## double check is not the pivot
				smaller.append(el)
		else:
			greater.append(el)

	return quick_sort(smaller) + [pivot] + quick_sort(greater)
```

I hope you really feel is a beautiful algorithm and is not my implementation, is the algorithm itself. The logic is straightforward. If the input list is empty, or is a single element list, the function return the list given as input. In fact, with such a list, you don't have to make order. This is the base case. Otherwise, if the list is at least two elements, you pick a random element from the list and create two new list. The first with the values smaller or equal to the random element, called the pivot. You must pay attention to include all the values equals to the pivot, that are not the pivot. Otherwise you could loss an eventual repetition.
The other list is composed by the numbers whose value are greater than the pivot.
Choosing the pivot by picking a random index is a good strategy, because prevent you from going in the worst case if, for example, the list is already ordered and you choose ever the first element to be the pivot.
At the very last of the function, the return statement, concatenate 3 list. Except for the one composed by the pivot only (be sure to include the pivot in square bracket), the other two aren't simply returned as they are but is returned the result of calling the quick_sort function on the list itself.
So, to bi clear, is not smaller that it's returned, but quick_sort(smaller). It' s a recursive call.
We can be sure that is not a infinite loop because, at the top of the function, our base case return without calling itself.

<span id="oneliners"></span>
#### **Wow, only in one line**

Now, it's time for something completely different. Python is a fun language, in which you can have fun in really creative and unpredictable ways. For me the fun may come from a challenge: rewrite some of the program used before in only one line. And now, you should ask:" Wow, only in one line?". Yes! Isn't amazing?
Yes, it is, but beware, i dont' recommend this programming style. The code is not much maintenable, and if you must change something often is a pain. Is only a way to have fun and master better python which is, in itself, a very fun thing.
Let's start with the first program.

<span id="bsoneline"></span>
#### **Binary search**

Please, before reading on, go to review the original code for this program. Now, let's start with a crucial modification. To write this in one line, we must implement binary search in a recursive way. Here the code.
```python
def bs(lista,search_value,low,high):
	if low > high:
		return -1

	mid = low + ((high-low)//2)
	if lista[mid] == search_value:
		return mid
	elif lista[mid] > search_value:
		return bs(lista,search_value,low,mid-1)
	else:
		return bs(lista,search_value,mid+1,high)
```
The difference is that, now, the logic is recursive, and you pass the low and high index as parameters of the function.
At the very top there's the base case. If the indexes passed as arguments are crossed (low index is greater than high index) this means the searched element is not in the list, and the function returns -1, as before.
Now, let's make together a step towarsd oneliner code.
For this, is important to understand a one line statement to handle if and else. In a return, or assigning a value to a variable, instead of writing an indented piece of code, you car wirte a one line statement. 

```python
	## usual way
	if value >= 0:
		result = 'positive'
	else:
		result = 'negative'

	## one line way
	result = 'positive' if value >= 0 else 'negative'
```

You can also annidate multiple if statements if you need. So let' s see our function with this one line modification in place.

```python
def bs(lista,search_value,low,high):
	if low > high:
		return -1

	mid = low + ((high-low)//2)
	return mid if lista[mid] == search_value else (bs(lista,search_value,low,mid-1) if 	lista[mid] > search_value else bs(lista,search_value,mid+1,high)) 
```

The previous if, elif, else multi rows statement has been translated in a single row. Pretty concise but, as you easily see, not really a readable piece of code. This is why i don't recommend this style except for entertainment purposes.
So, with this purposes in mind, let's continue. Ready? Sure? Really? Ok, you wanted it.
Take this one.

```python
def bs(lista,search_value,low,high):
	return -1 if low > high else ((low + ((high-low)//2)) if lista[low + ((high-low)//2)] == search_value else (bs(lista,search_value,low,(low + ((high-low)//2))-1) if 	lista[low + ((high-low)//2)] > search_value else bs(lista,search_value,(low + ((high-low)//2))+1,high)))
```

If you see more than one line i assure you that is only for visualization. This is a one line piece of code but... wait a minute. You are a liar. What about the line with def bs...:?
May be you don't believe me, but i can shrink also that line. I need only a new concept: lambda function.
Lambda function is a way to create an anonymous function on the fly. The simplest explanation is this. If you must declare a fuction, instead of doing this:
```python
	def sum(x,y):
		return x +y
```
you can do this

```python
sum = lambda x,y: x+y
```

With lambda you create a function whose parameters are the variable before ":" and the return statement, implicit, is the statement after the ":".
With this in mind, finally, the code for our binary search is:

```python
bs = lambda lista,search_value,low,high: -1 if low > high else ((low + ((high-low)//2)) if lista[low + ((high-low)//2)] == search_value else (bs(lista,search_value,low,(low + ((high-low)//2))-1) if 	lista[low + ((high-low)//2)] > search_value else bs(lista,search_value,(low + ((high-low)//2))+1,high)))
```
Wonderful!



<span id="bib"></span>
### **Inspiring**   [back to top](#top)
- *Grokking algorithms, Aditya Y. Bhargava, Manning 2016*
- *Python oneliners, Christian Mayer, No starch press 2020*
- *A common sense guide to data structure and alghoritms, Jay Wengrow, Pragmatic bookshelf 2020*
- *The big book of small python projects, Al Sweigart, No starch press 2021*
- *Tiny python projects, Ken Youens-Clark, Manning 2020* 
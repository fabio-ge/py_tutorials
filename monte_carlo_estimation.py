from random import randint

MAX_NUMBER=128
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
	## I know in advance that the number is present, so this part is unreachable
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
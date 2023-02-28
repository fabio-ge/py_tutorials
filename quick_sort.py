from random import randint

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


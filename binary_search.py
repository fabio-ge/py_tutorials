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
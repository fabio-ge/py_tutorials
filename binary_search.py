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


if __name__ == '__main__':
	ar1 = [1,2,3,4,5,6,7,8]
	ar2 = [11,22,33,44,55,66,77,88,99,111]
	print(bs(ar1,3))
	print(bs(ar1,7))
	print(bs(ar1,13))
	print("__________________")
	print(bs(ar2,44))
	print(bs(ar2,99))
	print(bs(ar2,50))

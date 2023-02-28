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

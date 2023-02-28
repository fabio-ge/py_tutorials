def bs(lista,search_value,low,high):
	if low > high:
		return -1

	mid = low + ((high-low)//2)
	return mid if lista[mid] == search_value else (bs(lista,search_value,low,mid-1) if 	lista[mid] > search_value else bs(lista,search_value,mid+1,high)) 

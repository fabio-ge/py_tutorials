def bs(lista,search_value,low,high):
	return -1 if low > high else ((low + ((high-low)//2)) if lista[low + ((high-low)//2)] == search_value else (bs(lista,search_value,low,(low + ((high-low)//2))-1) if 	lista[low + ((high-low)//2)] > search_value else bs(lista,search_value,(low + ((high-low)//2))+1,high)))

if __name__ == '__main__':
	lista = [1,2,3,4,5,6,7,8,9,10]
	print(bs(lista,3,0,len(lista)-1))
	print(bs(lista,4,0,len(lista)-1))
	print(bs(lista,5,0,len(lista)-1))
	print(bs(lista,6,0,len(lista)-1))
	print(bs(lista,7,0,len(lista)-1))
	print(bs(lista,11,0,len(lista)-1)) 

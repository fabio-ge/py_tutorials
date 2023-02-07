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

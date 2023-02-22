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
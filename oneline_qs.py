qs = lambda l:qs([el for el in l[1:] if el <= l[0]]) + [l[0]] + qs([el for el in l[1:] if el > l[0]]) if l else []

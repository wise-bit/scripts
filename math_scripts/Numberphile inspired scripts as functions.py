def nth_digit_to_n_gives_original_number():
	for i in range(100000000):
		s = sum([int(x)**int(x) for x in str(i)])
		if i == s:
			return(i)

def parker_square_attempt():
	arr = map(int,"0"*9)
	s = sum([i**2 for i in arr])
	return s

print(parker_square_attempt())
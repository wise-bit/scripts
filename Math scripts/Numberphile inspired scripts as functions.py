def nth_digit_to_n_gives_original_number():
	for i in range(100000000):
		s = sum([int(x)**int(x) for x in str(i)])
		if i == s:
			return(i)

def parker_square_attempt():
	a,b,c,d,e,f,g,h,i=map(int,"0"*9)
	return(a,b,c)

print(parker_square_attempt())
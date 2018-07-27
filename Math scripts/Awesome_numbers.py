'''

The above is called an “awesome fraction” because it equals a positive integer and uses each of the digits 0 through 9 exactly once on either side of the equal sign ().
What is the sum of all integers that can be expressed as awesome fractions?

'''

import itertools
s=0

for n_length in range(1,7+1):
	arr=list(map(int,list("1234567890")))
	stuff = arr
	for n_length in range(0, len(stuff)+1):
		for subset in itertools.combinations(stuff, L):
			arr = [x for x in arr if x not in subset]
			n=int("".join(subset))
			for d_length in range(1,8+1-n_length):
				for i_length in range(1,9+1-n_length-d_length):
					# print(n_length,d_length,i_length)
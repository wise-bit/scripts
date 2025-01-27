#readable_time

#!/bin/python3

import os

def timeInWords(h, m):
	hours = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twleve"]
	after_ten = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	denominations = ["twenty", "thirty", "forty", "fifty"]
	if m == 0:
		return hours[h-1] + " o' clock"
	elif m == 15:
		return "quarter past " + hours[h-1]
	elif m == 30:
		return "half past " + hours[h-1]
	elif m == 45:
		x = (h,0)[h==12]; return "quarter to " + hours[x]
	else:
		y = (m,60-m)[m>30]
		if y <= 10: minutes = hours[y-1]
		elif 11 <= y <= 19: minutes = after_ten[y-11]
		else: minutes = denominations[int(y/10) - 2] + " " + hours[y%10 - 1]
		ss = ("minutes", "minute")[m == 1]
		if m < 30: return "{} {} past {}".format(minutes, ss, hours[h-1])
		else: x = (h,0)[h==12]; return "{} {} to {}".format(minutes, ss, hours[x])

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	h = int(input())
	m = int(input())
	result = timeInWords(h, m)
	fptr.write(result + '\n')
	fptr.close()

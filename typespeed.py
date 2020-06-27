'''
learn from use and start asking for harder words based on difficulty 
level (prefer characters that are usually gotten wrong, maintain csv)
'''

import time
from random import *

def paragraph_generator(para, pieces):
	average_len = len(para) / pieces
	remaining = len(para)

	# Not used rn, can be used to enhance alg
	buffer_len = 0

	graph = []

	while remaining > 0:
		word_length = int(randrange(5, 10)*average_len/10)

		new_word = para[:word_length]

		if len(new_word) > 3:
			graph.append(new_word)

		para = para[word_length:]

		remaining -= word_length

	# print(graph)

	return graph


def chunk_generator(length):

	arr = []

	for i in range(length):
		# boolean
		upper_case = (0,1)[random() > 0.5]

		letter = chr(round(uniform(65, 65+25)))

		if upper_case:
			letter = letter.lower()

		arr.append(letter)

	return ''.join(arr)


def prompt(arr):

	if len(arr) == 0:
		return "Bad parameters, please try again"

	start = time.time()

	print("\nTest starts now ---->\n")

	score = 0
	for x in arr:
		if input(x + ": ") == x:
			score += len(x)

	total_time = time.time() - start
	print(total_time)

	return str(score*60 / total_time) + " <-- CPM"

print( prompt(paragraph_generator(chunk_generator(50), 7)) )

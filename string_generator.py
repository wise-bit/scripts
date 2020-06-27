import random

alph="abcdefghijklmnopqrstuvwxyz"

def generate(l):
	s = ""
	wordlength = 1
	for i in range(l):
		if wordlength == 0:
			s += " "
			wordlength = random.randint(4, 8)
		s += alph[random.randint(0, len(alph)-1)];
		wordlength -= 1
	return s

print(generate(500))
import random

alph="abcdefghijklmnopqrstuvwxyz"
numeric="0123456789"
hexa=numeric+"abcdef"

def generate_para(l):
	s = ""
	wordlength = 1
	for i in range(l):
		if wordlength == 0:
			s += " "
			wordlength = random.randint(4, 8)
		s += alph[random.randint(0, len(alph)-1)];
		wordlength -= 1
	return s

def generate_word(l):
	s = ""
	for i in range(l):
		if random.random() > 0.7:
			s += hexa[random.randint(0, len(hexa)-1)]
		else:
			s += numeric[random.randint(0, len(numeric)-1)];
	return s

print(generate_word(16))

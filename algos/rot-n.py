def caesar_cipher(plaintext, shift):
	# plaintext = plaintext.lower()
	# alphabet = "abcdefghijklmnopqrstuvwxyz"
	# shift_function = lambda x: (alphabet.index(x) + shift) % 26

	# ciphertext = map(shift_function, plaintext)
	skip = [".", " ", ",", "'"]
	arr = list(plaintext)
	for i in range(len(arr)):
		c = (ord(arr[i])+shift) if arr[i] not in skip else ord(arr[i])
		c -= 26 if c > 122 and arr[i] not in skip else 0
		c += 26 if c < 97 and arr[i] not in skip else 0
		arr[i] = chr(c)

	return "".join(arr)

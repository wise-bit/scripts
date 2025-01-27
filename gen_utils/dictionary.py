from PyDictionary import PyDictionary

import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

dictionary=PyDictionary()

s = ""

old_s = ""

while(s != "0"):
	s = input("Word / option: ")

	print("")

	if s == "1":
		if old_s == "":
			print("No previous records")
		else:
			print(dictionary.synonym(old_s))
			print()
		continue

	result = str(dictionary.meaning(s))

	if "list index out of range" in result:
		print("Try again")
	else:
		print(result)
		old_s = s

	print("")

print("Byeth")

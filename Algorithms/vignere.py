import sys

m = sys.argv[1]
s = sys.argv[2]

key = "wordle"

if m == "e":
  print("".join([chr(((ord(x) - 97) + (ord(key[i % 6]) - 97)) % 26 + 97) for i, x in enumerate(s)]))
elif m == "d":
  print("".join([chr(((ord(x) - 97) - (ord(key[i % 6]) - 97)) % 26 + 97) for i, x in enumerate(s)]))
else:
  print("only supports `e` and `d`")

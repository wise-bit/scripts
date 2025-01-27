d,n=map(int,input().split())
a=[]
s="+"*3**d;print(s)
for i in range(d):
	l=int(len(s)/3)
	s = s[:l] + " "*l + s[l*2:]
	print(s)

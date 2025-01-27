## Size defines the tree

size = int(input())
l=size+1
for i in range(size):
    n = 1 + i
    m=0
    while True:
        s="*"*(1+m)
        print(" "*(l-len(s)//2-1)+s)
        if n == 0: break
        n -= 1
        m += 2
print(" "*(size) + "|")
print("="*(size) + "V" + "="*(size))
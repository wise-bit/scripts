#infinite_fraction_reducer

n=int(input())
a=[]
for i in input().split():
    a.append(int(i))
u=1
d=a[-1]
c=0

for i in range(n-1,0,-1):
    #print(a[i-1])
    c=a[i-1]
    u = d
    d = d*c + 1
    u,d=d,u
    #print("{}/{}".format(d,u))
print("{}/{}".format(u,d))


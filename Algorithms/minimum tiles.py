import sys
import math

def gcd(a,b):
    if b > a: return gcd(b, a)
    if a % b == 0: return b
    return gcd(b, a % b) 

n,m = [int(i) for i in input().split()]
a=n*m/gcd(m,n)**2
print(int(a))

### Reflection on a line ###

'''
Line 1 : A string a for the axis for which to reflect over (either x or y)
Line 2: An integer b being the line, perpendicular to the a axis, to reflect over
Line 3 : An integer n for the number of points to reflect
Next n lines : Two space separated integers x and y
'''

a = input()
b = int(input())
n = int(input())

for i in range(n):
    x, y = [int(j) for j in input().split()]
    if a == "x": diff = b-y; y = b+diff
    else: diff = b-x; x = b+diff
    print(x,y)

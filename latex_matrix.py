s = input() 
l = len(s)
ans = "\\left[\n" + "\\begin{array}{" + "c"*l + "}"
first = True

while s:
    if not first:
        ans += "\\\\"
    first = False
    ans += "\n" + " & ".join(list(s))
    s = input()
    if s and len(s) != l:
        raise Exception("all rows must be equal in length!")

ans += "\n\\end{array}" + "\n\\right]"

print(ans)


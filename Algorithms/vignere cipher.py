c=input()
k=input()
l=len(k)
j=[ord(i)for i in k]
d=[ord(i)for i in c]
p=''
for i in range(len(d)):
    if d[i] != " ":
        v=(d[i] - j[i % l]) % 26
        p+=chr(v+97)
print(p)
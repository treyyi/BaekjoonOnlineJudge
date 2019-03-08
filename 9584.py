s=input()
d=[i for i in range(len(s)) if s[i]!='*']
b=0;c=0;a=[]
for i in range(int(input())):
    l=input()
    for j in d:
        if s[j] == l[j]:b+=1
    if b==len(d):
        c+=1
        a.append(l)
    b=0
print(c)
print('\n'.join(a))

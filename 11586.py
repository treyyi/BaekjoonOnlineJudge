a=[]
for _ in range(int(input())):
    a.append(input())
e=int(input())
if e==1:print('\n'.join(a))
elif e==2:
    for s in a:
        print(s[::-1])
else: print('\n'.join(a[::-1]))

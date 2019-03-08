l=[]
def d(n):
    t=n+eval('+'.join(str(n)))
    if t<=10000:
        l.append(t)
n=0
while(1):
    if int(n)<=10000:d(n)
    else:break
    n+=1
for i in range(10001):
    if i not in l:
        print(i)

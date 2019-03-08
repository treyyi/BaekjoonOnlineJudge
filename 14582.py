a=list(map(int,input().split()));b=list(map(int,input().split()))
c=False;d=0;n=[]
for i in range(2,11):
    if i-1==1:n.append(1 if sum(a[:i])>0 else 0)
    else:n.append(1 if sum(a[:i])>sum(b[:i]) else 0)
if n.count(1)>0 and sum(a)<sum(b):c=True
print("Yes" if c else "No")

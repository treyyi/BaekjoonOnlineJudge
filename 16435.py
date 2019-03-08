n,s=map(int,input().split())
f=sorted([*map(int,input().split())])
for i in range(n):
 if f[i]<=s:s+=1        
print(s)

a=0;b='';c=1
for i in range(1,6):
    x=sum(map(int,input().split()))
    if x>a:
        a=x;b=str(i)+' '+str(x)
print(b)

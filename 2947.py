x=list(map(int,input().split()))
while(x != [1,2,3,4,5]):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            tmp=x[i]
            x[i]=x[i+1]
            x[i+1]=tmp
            print(' '.join(str(s) for s in x))

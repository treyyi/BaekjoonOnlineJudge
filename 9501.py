for _ in range(int(input())):
    N,D=map(int,input().split());count=0
    for i in range(N):
        v,f,c=map(int,input().split())
        if D<=v*f/c:count+=1
    print(count)

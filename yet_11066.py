for _ in range(int(input())):
    k=int(input())
    d=list(map(int,input().split()))
    # define 2D array
    m=[[0 for x in range(k)] for y in range(k)]
    # fill out the array according to the coordinates
    for y in range(k):
        for x in range(y,k):
            if y==x:
                m[y][x]=d[y]
    for i in range(1,k):  #x
        for j in range(1,k):  #y
            if i+1!=k:


    for l in m:
        print(l)

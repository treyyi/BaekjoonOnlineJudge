for p in range(int(input())):
    count=0
    n=int(input())
    a=input();b=input()
    for i in range(n):
        if a[i]!=b[i]:count+=1
    print("Case {}: {}".format(p+1,count))

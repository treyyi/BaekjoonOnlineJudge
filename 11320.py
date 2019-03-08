for _ in range(int(input())):
    a,b=map(int,input().split())
    a1=a*a;b1=b*b
    ans=a1/b1
    if a1%b1!=0:ans+=1
    print(int(ans))

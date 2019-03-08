for i in range(1,int(input())+1):
    s="Scenario #"+str(i)+":\n"
    a,b,c=sorted(map(int,input().split()))
    if c*c == a*a+b*b:print(s+"yes")
    else:print(s+"no")
    print()

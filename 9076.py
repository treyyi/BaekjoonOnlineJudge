for i in range(int(input())):
    l=sorted(map(int,input().split()))[1:4]
    if max(l)-min(l)>=4:print("KIN")
    else:print(sum(l))

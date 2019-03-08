for _ in range(int(input())):
    l=list(map(int,input().split()))[1:]
    a=[x for x in l if x>sum(l)/len(l)]
    print("{0:0.3f}%".format(len(a)/len(l)*100))

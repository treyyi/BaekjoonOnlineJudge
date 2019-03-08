a=['Wolf','Coyote','Bobcat','Mountain Lion']
for _ in range(int(input())):
    n,s=input().split()
    W=s.count("W")*3;C=s.count("C");B=s.count("B")*2;M=s.count("M")*4
    t=[W,C,B,M];t2=[]
    for i in t:
        if i!=0:t2.append(i)
    m=t.index(max(t))
    if len(set(t))<4 and len(t2)>=2:print(n+": "+"There is no dominant species")
    else:print("{}: The {} is the dominant species".format(n,a[m]))

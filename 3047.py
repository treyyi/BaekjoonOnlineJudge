l=list(sorted(map(int,input().split())))
a=input()
dict={'A':0,'B':1,'C':2}
index=[]
for s in a:
    index.append(dict[s])
for i in index:
    print(l[i],end=' ')

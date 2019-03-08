b=[1,0,0]
for s in input():
    if s=='A':
        tmp=b[0]
        b[0]=b[1]
        b[1]=tmp
    elif s=='B':
        tmp=b[1]
        b[1]=b[2]
        b[2]=tmp
    else:
        tmp=b[0]
        b[0]=b[2]
        b[2]=tmp
print(b.index(1)+1)

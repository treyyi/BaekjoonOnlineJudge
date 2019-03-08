import sys
n=1;m="Triangle #";p="abc"
for i in sys.stdin:
    l=m+str(n)+"\n"
    s=list(map(int,i.split()))
    if s==[0,0,0]:break
    d=s.index(-1)
    if d==0:
        if s[2]**2-s[1]**2<=0:print(l+"Impossible.")
        else:
            s[0]=(s[2]**2-s[1]**2)**0.5
            print(l+"{} = {:.3f}".format(p[d],s[d]))
    elif d==1:
        if s[2]**2-s[0]**2<=0:print(l+"Impossible.")
        else:
            s[1]=(s[2]**2-s[0]**2)**0.5
            print(l+"{} = {:.3f}".format(p[d],s[d]))
    elif d==2:
        if s[0]**2+s[1]**2<=0:print(l+"Impossible.")
        else:
            s[2]=(s[0]**2+s[1]**2)**0.5
            print(l+"{} = {:.3f}".format(p[d],s[d]))
    print()
    n+=1

while(1):
    l=input()
    if set(l.split())=={'0'}:break
    else:
        a=list(map(int,l.split()))
        a1=a[1]-a[0];a2=a[2]-a[1]
        if a1==a2:print("AP "+str(a[2]+a1))
        else:
            b1=a[1]//a[0];b2=a[2]//a[1]
            print("GP "+str(a[2]*b1))

e,f,c=map(int,input().split());a=e+f
if a==0:print(0)
else:
    x=a//c
    y=a%c
    z=a-(x*c)
    new=x+y
    while(new>=c):
        x=x+(a//c)
        new=x+y
    print(x)

r=int(input())
while(1):
    s=input()
    if s=="=":print(r);break;
    n=int(input())
    if s=="+":r=r+n
    elif s=="-":r=r-n
    elif s=="/":r=r//n
    elif s=="*":r=r*n

while(1):
    s=input()
    if s=="0 0":break;
    else:
        a,b=map(int,s.split())
        print(2*a-b)

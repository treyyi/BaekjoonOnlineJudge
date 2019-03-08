for _ in range(int(input())):
    countg=0;countb=0;st=''
    l=input()
    for s in l:
        if s.lower()=='g':countg+=1
        elif s.lower()=='b':countb+=1
    if countg>countb:st="GOOD"
    elif countg<countb:st="A BADDY"
    else:st="NEUTRAL"
    print(l+" is "+st)

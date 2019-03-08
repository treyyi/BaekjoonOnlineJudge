n=int(input())
while(1):
    l=int(input())
    if l==0:
        break
    else:
        if l%n==0:
            print(str(l)+" is a multiple of "+str(n)+".")
        else:
            print(str(l)+" is NOT a multiple of "+str(n)+".")

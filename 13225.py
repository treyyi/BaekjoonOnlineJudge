for _ in range(int(input())):
    a=0;l=int(input())
    for c in range(1,l+1):
        if l%c==0:a+=1
    print(l, a)

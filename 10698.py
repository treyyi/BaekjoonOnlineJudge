for i in range(int(input())):
    a,b,c,d,e=input().split()
    print("Case {}: {}".format(i+1,"YES" if eval(a+b+c) == int(e) else "NO"))

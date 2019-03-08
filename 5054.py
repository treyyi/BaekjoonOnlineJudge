for _ in range(int(input())):
    x=input()
    line=set(list(map(int,input().split())))
    if line != 1:
        mn=min(line);mx=max(line)
        print((mx-mn)*2)
    else:print(0)

dict={'S':0,'R':1,'P':2}
l=[[2,1],[0,2],[1,0]]
for _ in range(int(input())):
    x=0;y=0
    for _ in range(int(input())):
        a,b=input().split()
        if dict[a] != dict[b]:
            q=dict[a];p=dict[b]
            if l[q].index(dict[b]) == 0:x+=1
            else:y+=1
    if x>y:print("Player 1")
    elif x<y:print("Player 2")
    else:print("TIE")
#가위바위보

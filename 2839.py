N=int(input())
fcount = 0
ans = []
while(1):
    tmp = 5*fcount
    if (tmp>N):
        break
    if (N-tmp)%3 == 0:
        three = (N-tmp)//3
        ans = [fcount, three]
    fcount+=1
if ans == []:
    print(-1)
else:
    print(ans[0]+ans[1])

N=int(input())
count = 0
num = 1
while(N!=0):
    if N >= num:
        N=N-num
        count += 1
        num+=1
    else:
        num = 1
print(count)

from itertools import combinations
import sys
for _ in range(int(input())):
    count=0
    n,m=map(int,sys.stdin.readline().split())
    for i in range(1,n):
        for j in range(i+1, n):
            if (i*i+j*j+m)%(i*j)==0:count+=1
    print(count)

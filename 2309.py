import sys
from itertools import combinations
heights=[]
result=[]
for _ in range(9):
    height=sys.stdin.readline().strip()
    heights.append(int(height))
for i, j in combinations(range(9), 2):
    result = sum(heights)-(heights[i]+heights[j])
    if result == 100:
        heights.pop(i)
        heights.pop(j-1)  # to adjust the index after removing i element
        print('\n'.join(map(str, sorted(heights))))
        break
#
# import itertools as I;a=sorted(map(int,map(input,['']*9)))
# for i in I.combinations(a,7):
#  if(sum(i)==100):print(*i,sep='\n');break

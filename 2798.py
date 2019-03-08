from itertools import combinations
A,B=map(int,input().split())
cards=[*map(int,input().split())]
max_nums=[]
for item in combinations(cards,3):
    if sum(item) <= B:
        max_nums.append(sum(item))
print(max(max_nums))

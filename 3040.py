from itertools import combinations
N=[]
for _ in range(9):
    n=int(input())
    N.append(n)
for i in combinations(N,7):
    if sum(i) == 100:
        print('\n'.join(str(item) for item in i))

from itertools import product, combinations_with_replacement
N=int(input())
c=[]
for a,b in itertools.product(range(N), repeat=2):
    if a+b <= N:
        result=(a+1)*(b+1)
        c.append(result)
print(max(c))

#can use combinations_with_replacement replacing product()

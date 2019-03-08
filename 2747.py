import sys,timeit
def f(n):
    if n==0:return 0
    elif n==1:return 1
    if n not in m:
        m[n]=f(n-1)+f(n-2)
    return m[n]
n=int(sys.stdin.readline())
m={0:0,1:1}
print(f(n))

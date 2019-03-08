for _ in range(int(input())):
    n=int(input())
    a=1;b=0;c=0;d=1
    if n==0:print("1 0")
    elif n==1:print("0 1")
    else:
        for _ in range(n-1):
            x,y=a+c,b+d
            a,b=c,d
            c,d=x,y
        print(x,y)

#
#
# global z,o
# z=0;o=0
# def f(n):
#     global z,o
#     if n==0:
#         z=z+1
#         return 0
#     elif n==1:
#         o=o+1
#         return 1
#     # else:return f(n-1)+f(n-2)
#     if n not in m:
#         m[n]=f(n-1)+f(n-2)
#     return m[n]
#
# for _ in range(int(sys.stdin.readline())):
#     n=int(sys.stdin.readline())
#     m={0:0,1:1}  # Memoization
#     start=timeit.default_timer()
#     print("F: ",f(n))
#     stop=timeit.default_timer()
#     print("M: ",m)
#     print("Time: ", stop-start)
#     f(n)
#     print(z, o)

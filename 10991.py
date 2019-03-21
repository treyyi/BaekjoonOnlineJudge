n=int(input())
for i in range(n-1,-1,-1):
    a=i*" ";b="*"
    if n>1:c=" *"*(n-i-1);print(a+b+c)
    else:print(a+b)
#
# n = int(input())
# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)

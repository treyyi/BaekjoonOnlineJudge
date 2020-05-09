N, r, c = map(int, input().split())

# 2, 3, 1
cnt = 0
result = 0
def divide(n, x, y):
    global cnt, result
    print(n, x, y)


    if x == c and y == r:
        print("print this...", cnt)
        result = cnt
        return
    if r < y + n and r >= y and c < x + n and c >= x:
        divide(n//2, x, y)  #1사분면
        divide(n//2, x, y+(n//2))  #2사분면
        divide(n//2, x+(n//2), y)  #3사분면
        divide(n//2, x+(n//2), y+(n//2))  #4사분면
    else:
        cnt += (n*n)

divide(2**N, 0, 0)
print(result)


# N,r,c = list(map(int,input().split()))
# result = 0
# while N>=1 :
#     temp = 2**(N-1) - 1
#
#     # 2사분면
#     if r <= temp and c<= temp :
#
#         N-=1
#         continue
#
#     # 1 사분면
#     elif c > temp and r<=temp :
#
#         c = c- temp-1
#         result += (temp+1)*(temp+1)
#
#     # 3 사분면
#     elif r> temp and c<= temp:
#
#         r =r-temp-1
#         result += (temp+1)*(temp+1) * 2
#
#     # 4사분면
#     else :
#
#         c = c- temp-1
#         r = r- temp -1
#         result += (temp+1)*(temp+1) * 3
#     N-=1
#
# print(result)

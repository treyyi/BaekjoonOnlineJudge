import math

N, K = map(int, input().split())

print(int(math.factorial(N + K - 1)//(math.factorial(K)*math.factorial(N-1)))%1000000000)

import math

n = int(input())
n_factorial = str(math.factorial(n))
cnt = 0

for i in range(len(n_factorial)-1, -1, -1):
    if n_factorial[i] == '0':
        cnt += 1
    else:
        break
print(cnt)

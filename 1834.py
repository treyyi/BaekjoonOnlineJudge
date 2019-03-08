N = int(input())
num_arr = []
num = 1
for i in range(1, N):  # 1 ~ (N-1)
    result = (N*i)+i
    num_arr.append(result)
print(sum(num_arr))

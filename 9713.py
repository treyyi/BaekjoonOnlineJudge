N = int(input().strip())
odds = []
for _ in range(N):
    num = int(input().strip())
    odds.append(num)
sum_of_odd = 0
for i in range(len(odds)):
    sum_of_odd = sum_of_odd + odds[i]
    print(sum_of_odd)

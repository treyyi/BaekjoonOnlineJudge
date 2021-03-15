n = int(input())

schedules = []
for _ in range(n):
    schedule = schedules.append(list(map(int, input().split())))

schedules.sort()
schedules.sort(key = lambda x:x[1])

print(schedules)

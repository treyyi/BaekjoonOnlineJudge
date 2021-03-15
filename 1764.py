import sys

n, m = map(int, input().split())

dic = {}
for i in range(n+m):  # O(n)
    name = sys.stdin.readline().strip()
    # dictionary에 key값이 처음 들어가는 경우
    if name not in dic:  # O(1)
        dic[name] = 1
    # dictionary에 key값이 이미 들어가 있는 경우
    else:
        dic[name] = dic[name]+1  # O(1)

answer = []
for k, v in dic.items():  # O(n)
    if v == 2:
        answer.append(k)
print(len(answer))
print("\n".join(sorted(answer)))

import sys
T = int(input())
answers = sys.stdin.readline().strip().split()
count = 0
for answer in answers:
    if T == int(answer):
        count += 1
if count == 0:
    print(0)
else:
    print(count)

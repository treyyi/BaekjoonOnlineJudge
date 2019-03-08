lines = int(input())
if lines == 0:
    print(-1)
else:
    cups = [1, 2, 3]
    for _ in range(lines):
        line = list(map(int, input().split()))
        X = line[0]
        Y = line[1]
        X_index = cups.index(X)
        Y_index = cups.index(Y)
        for i in range(3):
            if (i != X_index) and (i != Y_index):
                Z_index = i
                cups[Z_index] = cups[i]
        cups[X_index] = Y
        cups[Y_index] = X
    print(cups[0])
# cups = {'1':1, '2':2, '3':3}
# for _ in range(lines):
#     line = input().split()
#     X = cups[line[0]]
#     Y = cups[line[1]]
#     cups['1'] = X
#     cups['2'] = Y
#     for Z in cups:
#         if X != 1
#     cups['3'] =

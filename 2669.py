square = [[0]*101for _ in'a'*101]
for _ in range(4):
    points = [*map(int, input().split())]
    for i in range(points[0], points[2]):
        for j in range(points[1], points[3]):
            square[i][j] = 1
print(sum([sum(x) for x in square]))

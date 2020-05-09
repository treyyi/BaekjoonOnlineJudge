from collections import deque

def bfs(x, y):
    global board, visited
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    area = 0
    while q:
        area += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if visited[nx][ny] or board[nx][ny] == 0: continue
            visited[nx][ny] = True
            q.append([nx, ny])
    return area

n, m = map(int, input().split())

board = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

areas = []
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or visited[i][j]: continue
        area = bfs(i, j)
        areas.append(area)
        cnt += 1
print(board)
print(visited)
print(cnt)
if len(areas) == 0: print(0)
else: print(max(areas))

import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global graph, rows, cols
    # 범위 벗어날 경우 종료
    if x <= -1 or x >= rows or y <= -1 or y >= cols:
        return False
    # 아직 방문하지 않은 노드라면,
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 연결된 모든 노드 방문처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

if __name__ == '__main__':

    T = int(input())

    for _ in range(T):
        # 인접 행렬로 그래프 생성
        rows, cols, K = map(int, input().split())
        graph = [[0]*cols for _ in range(rows)]  # graph 초기화
        for i in range(K):
            x, y = map(int, input().split())
            graph[x][y] = 1

        # 모든 노드 탐색
        result = 0  # result초기화
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j) == True:
                    result += 1
        print(result)

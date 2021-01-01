# 2026.py

# exclude the node 0
counter = -1

def dfs(graph, v, visited):
    visited[v] = True
    global counter
    counter += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n_computers = int(input())
n = int(input())

# Initialize the graph
graph = [[]]
for i in range(n_computers):
    graph.append([])

# List of boolean values of the nodes
# for checking if it is visited
visited = [False] * (n_computers + 1)

for _ in range(n):
    edge = list(map(int, input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

dfs(graph, 1, visited)
print(counter)

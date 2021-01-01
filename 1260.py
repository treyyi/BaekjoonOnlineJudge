from collections import deque

def dfs(graph, start_node, visited):
    visited[start_node] = True
    print(start_node, end = " ")

    # recursively visit the all nodes
    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start_node, visited):
    q = deque([start_node])
    visited[start_node] = True

    # if q is empty, the search is finished
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
# Input
n_node, n_edge, start_node = map(int, input().split())

# Initialize a graph with the empty list at the first index of the graph
graph = [[]]
for _ in range(n_node):
    graph.append([])

# Create the graph
for i in range(n_edge):
    edge = list(map(int, input().split()))
    if edge[1] not in graph[edge[0]]:
        graph[edge[0]].append(edge[1])
    if edge[0] not in graph[edge[1]]:
        graph[edge[1]].append(edge[0])

# Sort the edges
for i in range(len(graph)):
    tmp = sorted(graph[i])
    graph[i] = tmp

# Create a visiting list (+1 because of the first index of the graph)
visited = [False] * (n_node+1)
visited2 = [False] * (n_node+1)

# Output
dfs(graph, start_node, visited)
print()
bfs(graph, start_node, visited2)

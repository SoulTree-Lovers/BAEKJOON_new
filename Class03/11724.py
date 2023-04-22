# 연결 요소의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# define a function to perform DFS on the graph
def dfs(graph, visited, vertex):
    # mark the vertex as visited
    visited[vertex] = True
    # iterate over the adjacent vertices
    for adj in graph[vertex]:
        # if the adjacent vertex is not visited, perform DFS on it
        if not visited[adj]:
            dfs(graph, visited, adj)

# read the number of vertices and edges from input
n, m = map(int, input().split())

# initialize an empty graph
graph = [[] for _ in range(n+1)]

# read the edges and add them to the graph
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# initialize an array to keep track of visited vertices
visited = [False] * (n+1)

# count the number of connected components
num_components = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, visited, i)
        num_components += 1

# print the result
print(num_components)

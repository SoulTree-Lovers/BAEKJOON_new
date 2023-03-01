# # DFS와 BFS

from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)









# ------------------------------------------------------------------------------
# import sys
# from collections import deque
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# nodes = {}


# n, m, v = map(int, input().split())

# for i in range(m):
#     start, end = map(int, input().split())
#     if start not in nodes:
#         nodes[start] = {end}
        
#     if end not in nodes:
#         nodes[end] = {start}
    
#     if start in nodes:
#         nodes[start].add(end)
    
#     if end in nodes:
#         nodes[end].add(start)
        

# nodes = dict(sorted(nodes.items()))
# # print(nodes)

# startNode = v

# def DFS(nodes, startNode, visited):
#     visited[startNode-1] = True

#     print(startNode, end=" ")
#     # print(visited)
#     if startNode in nodes:
#         for i in nodes[startNode]:
#             if not visited[i-1]:
#                 DFS(nodes, i, visited)    
        
#     # for i in nodes:
#     #     if not visited[i-1]:
#     #         DFS(nodes, i, visited) 

# def BFS(nodes, startNode, visited):
#     visited[startNode-1] = True
#     queue = deque([startNode])

#     print(startNode, end=" ")
#     while queue and queue[0] in nodes:
#         # print(queue)
#         # print("----------------------------------------------------------------")
            
#         for i in nodes[queue.popleft()]:
#             if not visited[i-1]:
#                 visited[i-1] = True
#                 print(i, end=" ")
#                 queue.append(i)
        
#     # for i in nodes:
#     #     if not visited[i-1]:
#     #         BFS(nodes, i, visited)
    

# if v not in nodes:
#     print(v)
#     print(v)
#     exit(0)


# visited = [False] * n
# DFS(nodes, startNode, visited)
# print()

# visited = [False] * n
# BFS(nodes, startNode, visited)
# print()
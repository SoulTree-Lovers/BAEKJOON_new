import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

start, end = map(int, input().split())

# Dijkstra's algorithm
dist = [float('inf')] * (n + 1)
dist[start] = 0
heap = [(0, start)]

while heap:
    cost, pos = heapq.heappop(heap)

    if pos == end:
        print(dist[end])
        break

    if dist[pos] < cost:
        continue

    for nxt, nw in graph[pos]:
        if dist[nxt] > dist[pos] + nw:
            dist[nxt] = dist[pos] + nw
            heapq.heappush(heap, (dist[nxt], nxt))

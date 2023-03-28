# 최소비용 구하기 2

import heapq
INF = int(1e9)

n = int(input())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)
path = [0] * (n + 1)

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 출력
print(distance[end])

# 경로 구하기
path_list = []
temp = end
while temp != start:
    path_list.append(temp)
    temp = path[temp]
path_list.append(start)

# 경로 역순으로 출력
print(len(path_list))
for city in reversed(path_list):
    print(city, end=" ")

print()
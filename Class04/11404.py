# 플로이드
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# initialize distances array
distances = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    distances[i][i] = 0

# update distances array with bus information
for _ in range(m):
    a, b, c = map(int, input().split())
    distances[a-1][b-1] = min(distances[a-1][b-1], c)

# run Floyd-Warshall algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

# print distances array
for i in range(n):
    for j in range(n):
        if distances[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()

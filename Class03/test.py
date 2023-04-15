# 경로 찾기
import sys
input = sys.stdin.readline

n = int(input())  # 정점의 개수
adj_matrix = [list(map(int, input().split())) for _ in range(n)]  # 인접 행렬 입력 받기

# Floyd-Warshall 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][k] and adj_matrix[k][j]:
                adj_matrix[i][j] = 1

# 결과 출력
for i in range(n):
    for j in range(n):
        print(adj_matrix[i][j], end=' ')
    print()

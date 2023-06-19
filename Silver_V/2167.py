# 2차원 배열의 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

# print(array)
dp = [[0]*(m+1) for _ in range(n+1)]
# print(dp)


for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = array[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# print(dp)

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())

    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

    # total = 0

    # for a in range(i-1, x):
    #     # total += (sum(array[a][0:y]) - sum(array[a][0:j-1]))
    #     for b in range(j-1, y):
    #         total += array[a][b]

    # print(total)
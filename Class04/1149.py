# RGB 거리
import sys
input = sys.stdin.readline

INF = float('inf')

def solve(n, costs):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0] = costs[0]

    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[i][j])
    
    return min(dp[-1])

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, costs))

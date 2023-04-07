# 평범한 베낭
import sys
input = sys.stdin.readline

# take input for number of items and maximum weight the backpack can hold
n, k = map(int, input().split())

# initialize a list to store the maximum value that can be obtained for a given weight
dp = [0] * (k + 1)

# loop through the items and update the dp list
for i in range(n):
    w, v = map(int, input().split())
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

# print the maximum value that can be obtained for the given weight
print(dp[k])

# 백팩이 담을 수 있는 항목 수(N)와 최대 무게(K)를 입력합니다.
# 주어진 가중치에 대해 얻을 수 있는 최대값을 저장하기 위해 'K+1' 크기의 리스트 'dp'를 초기화합니다.
# N 항목을 반복하고 각 항목에 대해 dp 목록을 거꾸로(K에서 w-1로) 반복하고 각 가중치에 대해 얻을 수 있는 최대값을 업데이트합니다.
# 주어진 가중치 K에 대해 얻을 수 있는 최대값은 dp 목록의 마지막 인덱스에 저장되므로 dp[K]를 출력으로 출력합니다.

# 이 접근 방식은 O(NK)의 시간 복잡도를 가지며 주어진 제약 조건을 처리하기에 충분히 효율적입니다.
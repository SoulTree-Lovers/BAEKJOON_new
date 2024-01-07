# 줄어들지 않아

def non_decreasing_count(n):
    # dp[i][j]는 i자리 숫자 중 가장 마지막 자리가 j인 줄어들지 않는 수의 개수를 나타냄
    dp = [[0] * 10 for _ in range(n + 1)]

    # 한 자리 숫자는 모두 줄어들지 않는 수이므로 1로 초기화
    for i in range(10):
        dp[1][i] = 1

    # i자리 숫자를 만들 때
    for i in range(2, n + 1):
        # 마지막 자리 수가 j일 때
        for j in range(10):
            # 이전 자리 수의 j 이상의 수들의 합
            dp[i][j] = sum(dp[i - 1][j:])

    # n자리 숫자 중 모든 마지막 자리 수의 합이 답
    result = sum(dp[n])
    return result

def solution():
    T = int(input())  # 테스트 케이스의 개수

    for _ in range(T):
        n = int(input())  # 자리 수
        result = non_decreasing_count(n)
        print(result)

if __name__ == "__main__":
    solution()

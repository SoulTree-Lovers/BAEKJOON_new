# LCS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 맨 첫 번째 행과 열에 공백을 추가하여 인덱스 에러가 나지 않게 함.
first_string = " " + input().strip()
second_string = " " + input().strip()

n, m = len(first_string), len(second_string)

# print("first_string: " + first_string, "second_string: " + second_string)
# print("n:", n, "m:", m)

# DP를 사용할 2차원 배열을 생성함.
lcs = [[0 for _ in range(m)] for _ in range(n)]
# print(lcs)

# 각 문자열을 앞에서부터 비교한다.
for i in range(1, n):
    for j in range(1, m):
        # 현재 위치에서 문자가 같다면 1을 추가하고 두 문자열 모두에서 인덱스 1 증가
        if first_string[i] == second_string[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1

        # 현재 위치에서 문자가 다르다면 두 문자열에서 인덱스를 1 증가해서 비교해보고 둘 중 큰 수로 채택
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])



# 재귀 방식은 시간초과.. ㅠㅠ
# def LCS(i, j):
#     if i == 0 or j == 0:
#         return 0
    
#     elif first_string[i-1] == second_string[j-1]: 
#         return LCS(i-1, j-1) + 1
        
#     else:
#         return max(LCS(i, j-1), LCS(i-1, j))


print(lcs[n-1][m-1])
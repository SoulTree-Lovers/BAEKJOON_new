# 삼각형 만들기
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

# 입력받기
straws = [int(input()) for _ in range(n)]

# 내림차순으로 정렬 (길이가 긴 변부터 확인하기 위함)
straws.sort(reverse=True)

max_size = -1

for i in range(n-2):
    a = straws[i]
    b = straws[i+1]
    c = straws[i+2]

    # 삼각형 조건이 맞으면 즉시 세 변의 길이 합 저장 후 종료
    if a < b + c:
        max_size = a + b + c
        break

print(max_size)


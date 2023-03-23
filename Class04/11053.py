# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

temp = [1] * n

for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            temp[i] = max(temp[i], temp[j] + 1)

print(max(temp))

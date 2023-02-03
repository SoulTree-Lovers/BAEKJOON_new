# 구간합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 5, 3

num_list = list(map(int, input().split())) # [5, 4, 3, 2, 1]

output = [0] * (n + 1)    # [0, 5, 9, 12, 14, 15]
s = 0

for i in range(n):
    s += num_list[i]
    output[i+1] += s
#     print(s)

# print(output)

for i in range(m):
    a, b = map(int, input().split())
    print(output[b] - output[a-1])

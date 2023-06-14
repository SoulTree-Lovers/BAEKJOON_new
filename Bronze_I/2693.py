# N번째 큰 수

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num_list = sorted(list(map(int, input().split())))

    print(num_list[-3])



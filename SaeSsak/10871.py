# X보다 작은 수

import sys
input = sys.stdin.readline

n, x = map(int, input().split())

num_list = list(map(int, input().split()))

for i in num_list:
    if i < x:
        print(i)
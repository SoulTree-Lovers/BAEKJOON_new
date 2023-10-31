# 동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin_list = []

for i in range(n):
    coin_list.append(int(input()))

count = 0
index = n-1

while k > 0:
    temp = k // coin_list[index]
    k -= temp * coin_list[index]
    count += temp
    index -= 1

print(count)
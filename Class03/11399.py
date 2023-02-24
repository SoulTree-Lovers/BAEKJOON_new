# ATM
import sys
input = sys.stdin.readline

n = int(input())

time_list = list(map(int, input().split()))

time_list.sort()

total = 0

for i in range(n):
    total += (n-i) * time_list[i]

print(total)
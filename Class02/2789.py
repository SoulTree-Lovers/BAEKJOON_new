# 블랙잭
import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list = list(itertools.combinations(num_list, 3))

max_value = 0

for i in num_list:
    data = sum(i)

    if data > max_value and data <= m:
        max_value = data
    
print(max_value)
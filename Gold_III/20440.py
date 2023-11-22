# 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
count_dict = defaultdict(int)

for i in range(n):
    te, tx = map(int, input().split())
    count_dict[te] += 1
    count_dict[tx] -= 1

max_count = 0
curr_count = 0
tem = 0
txm = 0
flag = False

for i in sorted(count_dict.keys()):
    curr_count += count_dict[i]
    if curr_count > max_count:
        max_count = curr_count
        flag = True
        tem = i
    
    elif curr_count < max_count and flag:
        txm = i
        flag = False

print(max_count)
print(tem, txm)


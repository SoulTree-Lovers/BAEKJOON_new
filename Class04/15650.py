# N과 M (2)

import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = [i for i in range(1, n+1)]

answer = list(itertools.combinations(num_list, m))

for i in answer:
    for j in range(m):
        print(i[j], end=" ")
    print()
    
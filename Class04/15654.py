# N과 M (5)

import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split(" ")))

answer = list(itertools.permutations(num_list, m))

for index in range(m-1, -1, -1):
    answer = sorted(answer, key=lambda x : x[index])
    

for i in answer:
    for j in range(m):
        print(i[j], end=" ")
    print()
    
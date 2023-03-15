# N과 M (4)

import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = [i for i in range(1, n+1)]

answer = list(itertools.combinations_with_replacement(num_list, m))

# for i in range(1, n+1):
#     answer.append((i, i))

for index in range(m-1, -1, -1):
    answer = sorted(answer, key=lambda x : x[index])
    

for i in answer:
    for j in range(m):
        print(i[j], end=" ")
    print()
    
# N과 M (8)

import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

answer = list(itertools.combinations_with_replacement(num_list, m))
new_answer = []
# for i in range(1, n+1):
#     answer.append((i, i))
# print(answer)

for i in answer:
    new_answer.append(sorted(list(i)))

# print(new_answer)
for index in range(m-1, -1, -1):
    new_answer = sorted(new_answer, key=lambda x : x[index])
    

for i in new_answer:
    for j in range(m):
        print(i[j], end=" ")
    print()
    
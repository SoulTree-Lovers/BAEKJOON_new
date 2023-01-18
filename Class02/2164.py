# 카드 2
from collections import deque

n = int(input())
num_list = deque()

for i in range(1, n+1):
    num_list.append(i)

while len(num_list) > 1:
    num_list.popleft()
    num_list.append(num_list.popleft())

print(num_list[0])
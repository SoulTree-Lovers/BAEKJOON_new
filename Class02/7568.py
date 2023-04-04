# 덩치
import sys
input = sys.stdin.readline

n = int(input())

sizes = []

for i in range(n):
    size = tuple(map(int, input().split()))
    sizes.append(size)

count_list = []

# 자신보다 덩치가 큰 사람이 있으면 count += 1
for i in range(n):
    count = 1
    curr_size = sizes[i]

    for size in sizes:
        if size[0] > curr_size[0] and size[1] > curr_size[1]:
            count += 1

    count_list.append(count)
        

# count 출력
for count in count_list:
    print(count)

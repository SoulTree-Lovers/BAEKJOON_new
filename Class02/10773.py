# 제로

n = int(input())

num_list = []

for i in range(n):
    num = int(input())

    if num != 0:
        num_list.append(num)
    else:
        num_list.pop(-1)

print(sum(num_list))
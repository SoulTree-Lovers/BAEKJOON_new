# 좌표 정렬하기 2

n = int(input())


num_list = []
for i in range(n): 
    num_list.append(tuple(map(int, input().split())))

num_list.sort(key=lambda x : (x[1], x[0]))

# print(num_list)

for i in num_list:
    print(i[0], i[1])
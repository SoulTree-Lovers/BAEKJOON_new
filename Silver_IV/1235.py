# 학생 번호
import sys
input = sys.stdin.readline

n = int(input())

num_list = []

for i in range(n):
    num_list.append(input().strip())

# print(num_list)

k = -2

while True:
    temp = set()
    for i in num_list:
        temp.add(int(i[-1:k:-1]))
    
    # print(temp)

    if len(temp) == len(num_list):
        break
    

    k -= 1

print(abs(k)-1)
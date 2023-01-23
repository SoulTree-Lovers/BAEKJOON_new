# 단어 정렬
import sys
input = sys.stdin.readline

n = int(input())
str_list = []

for i in range(n):
    str_list.append(input().strip())

# print(str_list)
str_list = list(set(str_list))
str_list.sort()
str_list.sort(key=len)


for i in str_list:
    print(i)
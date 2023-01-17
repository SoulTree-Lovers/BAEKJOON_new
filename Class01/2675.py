# 문자열 반복

n = int(input())

str_list = []

for i in range(n):
    a, b = map(str, input().split())

    string = ""
    for j in b:
        string += int(a) * j
    str_list.append(string)
for i in str_list:
    print(i)
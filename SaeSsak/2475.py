# 검증수

num_list = list(map(int, input().split()))

num_list = [i ** 2 for i in num_list]

s = sum(num_list)

print(s % 10)
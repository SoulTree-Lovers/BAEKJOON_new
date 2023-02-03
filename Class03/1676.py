# 팩토리얼 0의 개수
import math

n = int(input())

number = str(math.factorial(n))
length = len(number)

# print(number)
count = 0

for i in range(length-1, -1, -1):
    if number[i] != '0':
        print(count)
        break

    count += 1
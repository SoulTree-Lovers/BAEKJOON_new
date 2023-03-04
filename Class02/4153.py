# 직각삼각형
import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    num_list = [a, b, c]
    # print(num_list)
    num_list.sort()
    # print(num_list)
    if  num_list[0]**2 + num_list[1]**2 == num_list[2]**2:
        print("right")
    else:
        print("wrong")


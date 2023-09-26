# 이진수 덧셈
import sys
input = sys.stdin.readline

n = int(input())
binary = "0b"

n_list = []

for i in range(n):
    a, b = map(str, input().split())
    output = int(binary + a, 2) + int(binary + b, 2)
    n_list.append(bin(output)[2:])

for i in n_list:
    print(i)




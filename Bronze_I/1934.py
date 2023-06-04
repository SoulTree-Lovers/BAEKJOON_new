# 최소공배수
import sys
import math
input = sys.stdin.readline

# def GCD(a, b):
#     while(b):
#         a, b = b, a % b
    
#     return a

# def LCM(a, b):
#     result = (a+b) // GCD(a, b)
#     return result


n = int(input())

for i in range(n):    
    a, b = map(int, input().split())

    print(math.lcm(a, b))

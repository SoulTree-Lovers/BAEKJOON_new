# 곱셈

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def divide_and_conquer(a, b, c):
    if b == 1:
        return a % c
    
    else:
        if b % 2 == 0:
            return (divide_and_conquer(a, b//2, c) ** 2) % c
        
        else:
            return (divide_and_conquer(a, b//2, c) ** 2 * a) % c
        
print(divide_and_conquer(a, b, c))
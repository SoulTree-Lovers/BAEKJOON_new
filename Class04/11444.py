# 피보나치 수 6
# Fm+n = Fm-1Fn + FmFn-1 (도가뉴 항등식)

import sys
from collections import defaultdict
input = sys.stdin.readline
DEV_NUM = 1000000007

n = int(input())

fibo = defaultdict(int)
fibo[1] = 1
fibo[2] = 1

def fibonacci(n):
    if fibo[n] != 0:
        return fibo[n]
    
    if n % 2 == 1:
        b = n // 2
        a = b + 1
        c = fibonacci(a)
        d = fibonacci(b)

        fibo[n] = (c ** 2 + d ** 2) % DEV_NUM
    
        return fibo[n]
    
    else:
        a = n // 2
        b = a - 1
        c = fibonacci(a)
        d = fibonacci(b)

        fibo[n] = (c ** 2 + 2 * c * d) % DEV_NUM
    
        return fibo[n]

print(fibonacci(n))



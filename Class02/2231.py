# 분해합

import sys
input = sys.stdin.readline

n = int(input())
    

curr = 1

while True:
    sum_ = curr

    for i in str(curr):
        sum_ += int(i)
    
    if sum_ == n:
        print(curr)
        break

    elif curr == n:
        print(0)
        break

    curr += 1
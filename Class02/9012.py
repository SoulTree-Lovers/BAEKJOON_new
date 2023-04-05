# 괄호

import sys
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    count = 0

    ps = input()
    isValid = True
    
    for i in ps:
        if count < 0:
            isValid = False
            break
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        
    if isValid and count == 0:
        print("YES")
    else:
        print("NO")

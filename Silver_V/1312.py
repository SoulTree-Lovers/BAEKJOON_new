# 소수
import decimal

a, b, n = map(int, input().split())

count = 0 
while True:
    if n == 0:
        print(temp)
        break

    if a >= b:
        a -= b
        count += 1

    else:
        temp = (a * 10) // b
        a = (a * 10) % b
        n -= 1
    
    # print(a)
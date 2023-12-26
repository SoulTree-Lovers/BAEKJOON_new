# 반올림

n = int(input())

cmp = 10

while True: 
    if n <= cmp:
        break

    temp = n % cmp

    if temp >= cmp // 2:
        n += cmp

    n -= temp
    cmp *= 10

print(n)

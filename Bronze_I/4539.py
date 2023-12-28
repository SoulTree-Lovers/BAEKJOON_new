# 반올림

def _round(num):
    n = num
    cmp = 10

    while True: 
        if n <= cmp:
            break

        temp = n % cmp

        if temp >= cmp // 2:
            n += cmp

        n -= temp
        cmp *= 10
    
    return n

n = int(input())

for i in range(n):
    print(_round(int(input())))

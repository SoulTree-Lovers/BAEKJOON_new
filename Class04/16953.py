# A -> B

A, B = map(int, input().split())

count = 1

while True:
    if B == A:
        break
    count += 1

    temp = B

    if B % 10 == 1:
        B = B // 10
    
    elif B % 2 == 0:
        B = B // 2

    if temp == B:
        print(-1)
        exit(0)

print(count)
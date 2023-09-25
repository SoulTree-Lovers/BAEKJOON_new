# 명령 프롬프트
import sys
input = sys.stdin.readline

n = int(input())

orders = []

for i in range(n):
    orders.append(input().strip())

if n == 1:
    print(orders[0])

else:
    length = len(orders[0])

    output = ""

    for i in range(length):
        isSame = True

        for j in range(n-1):
            if orders[j][i] != orders[j+1][i]:
                # print(orders[j][i])
                # print(orders[j+1][i])
                output += "?"
                isSame = False
                break

        if isSame:
            output += orders[0][i]

    print(output)
# A + B - 3

n = int(input())
output = []

for i in range(n):
    a, b = map(int, input().split())
    output.append(a + b)

for i in output:
    print(i)
# 피보나치 수

n = int(input())

fibos = [1, 1]

for i in range(n-2):
    fibos.append(fibos[i] + fibos[i+1])

print(fibos[-1])
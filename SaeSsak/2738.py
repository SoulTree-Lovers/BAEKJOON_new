# 행렬 덧셈

n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(n)]

C = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(A[i][j] + B[i][j])
    C.append(temp)

# print(C)
for i in C:
    for j in i:
        print(j, end=" ")
    print()
print()
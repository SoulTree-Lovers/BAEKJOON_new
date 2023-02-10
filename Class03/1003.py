# 피보나치 함수


n = int(input())

# fibo_list = [(1, 0), (0, 1)]
output = []

for i in range(n):
    fibo_num = int(input())
    fibo_list = [(1, 0), (0, 1)]

    if fibo_num == 0:
        output.append((1, 0))
    elif fibo_num == 1:
        output.append((0, 1))
    else:
        for j in range(1, fibo_num):
            fibo_list.append((fibo_list[j-1][0] + fibo_list[j][0], fibo_list[j-1][1] + fibo_list[j][1]))
        output.append(fibo_list[-1])

for i in output:
    print(i[0], i[1])



# 파도반 수열

n = int(input())

output = []

array = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] # P(1) ~ P(10)

for i in range(n):
    num = int(input())

    if num > len(array):
        for j in range(num-len(array)):
            array.append(array[-1] + array[-5])
    
    output.append(array[num-1])

for i in output:
    print(i)
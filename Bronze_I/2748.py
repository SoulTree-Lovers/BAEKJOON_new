# 피보나치 수 2

n = int(input())

def fibo(n):
    fibo_list = [1, 1]
    
    for i in range(2, n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    
    # print(fibo_list)
    return fibo_list[-1]
    
print(fibo(n))

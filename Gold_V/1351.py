# 무한 수열
import math

n, p, q = map(int, input().split())

i_dict = {0 : 1}

def add_dict(i):
    # 종료 조건
    if (i == 0):
        return 1
    
    i_p = math.floor(i/p)
    i_q = math.floor(i/q)

    # print("i:", i)
    # print("i_p: ", i_p)
    # print("i_q: ", i_q)
    
    
    if (i_p not in i_dict.keys()):
        i_dict[i_p] = add_dict(i_p)
        
    if (i_q not in i_dict.keys()):
        i_dict[i_q] = add_dict(i_q)

    
    i_dict[i] = i_dict[i_p] + i_dict[i_q]
    return i_dict[i_p] + i_dict[i_q]

# 함수 실행 
print(add_dict(n))

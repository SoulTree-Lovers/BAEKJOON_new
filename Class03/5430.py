# AC
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
output = []


for i in range(n):
    p = sys.stdin.readline().rstrip()
    arr_len = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if arr_len == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                output.append("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            output.append("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            output.append("[" + ",".join(queue) + "]")



for i in output:
    print(i)


# ---------------------- 시간초과 ----------------------
# import sys
# # import numpy as np
# # from collections import deque
# # import itertools


# input = sys.stdin.readline

# n = int(input())
# output = []
# is_error = False


# for i in range(n):
#     is_error = False
#     orders = input()
#     arr_len = int(input())
#     arr = list(input()[1:arr_len*2].split(','))
#     # arr = np.array(arr)

#     # print(orders)
#     # print(arr_len)
#     # print(arr)



#     for order in orders:
#         if len(arr) > 1 and order == 'R':
#             # arr = list(itertools.islice(len(arr), len(arr), 0, -1))
#             arr = arr[::-1]
#         elif order == 'D':
#             if len(arr) > 0 and arr[0] != '':
#                 arr.pop(0)
                
#             else:
#                 is_error = True
#                 output.append('error')
#                 break
                

    
#     if not is_error:
#         output.append(arr)

# # while output.count('error') > 0:    
# #     output.pop(output.index('error')+1)

# # print(output.index('error'))
# # print(output.count('error'))

# for i in output:
#     print(i)
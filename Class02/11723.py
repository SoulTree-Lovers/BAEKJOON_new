# 집합
import sys
input = sys.stdin.readline

n = int(input())

s = set()

output = []

for i in range(n):
    order = input().split()
    
    if order[0] == 'add':
        s.add(int(order[1]))

    elif order[0] == 'remove':
        if int(order[1]) in s:
            s.remove(int(order[1]))
    
    elif order[0] == 'check':
        if int(order[1]) in s:
            # output.append(1)
            print(1)
        else:
            # output.append(0)
            print(0)
    
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.add(int(order[1]))
    
    elif order[0] == 'all':
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    
    elif order[0] == 'empty':
        s = set()

# for i in output:
#     print(i)
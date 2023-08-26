# solved.ac
import math
import sys
input = sys.stdin.readline

n = int(input())



def _round(x):
    return int(x) + (1 if x - int(x) >= 0.5 else 0)


def solve():
    levels = []

    for i in range(n):
        levels.append(int(input()))
        
    except_num = _round(n * 0.15)

    # print(except_num)

    levels.sort()

    levels = levels[except_num:n-except_num]

    # print(levels)

    print(_round(sum(levels)/len(levels)))


if n == 0:
    print(0)

else:
    solve()


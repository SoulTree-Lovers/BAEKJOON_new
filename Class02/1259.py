# 팰린드롬 수

import sys
input = sys.stdin.readline

pal_list = []

while True:
    n = int(input())
    if n == 0:
        break

    if str(n) == str(n)[::-1]:
        pal_list.append('yes')
    else:
        pal_list.append('no')

for i in pal_list:
    print(i)
    
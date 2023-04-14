# 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))

members = sorted(members)

for member in members:
    print(member[0], member[2])

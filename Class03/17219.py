# 비밀번호 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pw_dic = dict()

for i in range(n):
    site, pw = map(str, input().split())

    pw_dic[site] = pw

output = []

for i in range(m):
    site = input().strip()

    output.append(pw_dic[site])

for i in output:
    print(i)
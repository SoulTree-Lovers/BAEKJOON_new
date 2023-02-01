# 듣보잡

n, m = map(int, input().split())
# n = 3
# m = 4

n_list = set()
m_list = set()

for i in range(n):
    n_list.add(input())

for i in range(m):
    m_list.add(input())

new_list = n_list & m_list

new_list = list(new_list)
new_list.sort()


print(len(new_list))

for i in new_list:
    print(i)


# 수 찾기

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binSearch(target):
    left = 0
    right = n-1

    while 1:
        if left > right:
            break
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True
        
        elif n_list[mid] > target:
            right = mid - 1
        
        elif n_list[mid] < target:
            left = mid + 1


for i in m_list:
    if binSearch(i):
        print(1)
    else:
        print(0)

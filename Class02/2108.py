# 통계학

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))

def num_mean(num_list):
    return round(sum(num_list) / n)

def num_median(num_list):
    num_list.sort()

    return num_list[n//2]

def num_mode(num_list):
    c = Counter(num_list)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])

    if len(modes) > 1:
        return modes[1]

    return modes[0]
    
    


def num_range(num_list):
    return max(num_list) - min(num_list)


if n == 1:
    print(num_list[0])
    print(num_list[0])
    print(num_list[0])
    print(0)
else:
    print(num_mean(num_list))
    print(num_median(num_list))
    print(num_mode(num_list))
    print(num_range(num_list))


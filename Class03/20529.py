# 가장 가까운 세 사람의 심리적 거리
import sys
input = sys.stdin.readline

def get_distance(length, MBTIs):

    min_distance = 999999999

    if people_num > 32:
        return 0
        
    else:
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    distance = 0

                    if i == j or i == k or j == k:
                        continue

                    for idx in range(4):
                        if MBTIs[i][idx] != MBTIs[j][idx]:
                            distance += 1
                        if MBTIs[i][idx] != MBTIs[k][idx]:
                            distance += 1
                        if MBTIs[j][idx] != MBTIs[k][idx]:
                            distance += 1
                    # print(total_distance)
                    min_distance = min(min_distance, distance)
    
        return min_distance
    # print(min_distance)
        

n = int(input())

for _ in range(n):
    people_num = int(input())

    MBTIs = list(map(str, input().split()))
    
    print(get_distance(people_num, MBTIs))
  

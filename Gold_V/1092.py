# 배
import sys
input = sys.stdin.readline

n = int(input()) # 크레인의 수
crane_limit = list(map(int, input().split())) # 크레인의 무게 제한
m = int(input()) # 박스의 수
box_weight = list(map(int, input().split())) # 박스의 무게

# 모든 박스를 배로 옮길 수 없으면 -1 출력
if max(crane_limit) < max(box_weight):
    print(-1)
    exit()

# 박스 무게를 내림차순으로 정렬
box_weight.sort(reverse=True)
# print(box_weight)

# 크레인 무게를 내림차순으로 정렬
crane_limit.sort(reverse=True)
# print(crane_limit)

# 걸린 시간 (분)
minutes = 0

# 박스 옮기기
while len(box_weight) > 0: # 200 (시간 복잡도)
    minutes += 1
    for crane in crane_limit: # 50
        for i, box in enumerate(box_weight):
            if crane >= box:
                box_weight.pop(i)
                break

print(minutes)
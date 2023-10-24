# 다이어트
G = int(input())

old = 1 # 과거의 몸무게를 가리키는 포인터
now = 2 # 현재의 몸무게를 가리키는 포인터

weights = [] # 조건에 맞는 현재 몸무게를 담을 리스트

for i in range(100000): # 100,000을 전부 돌려보기
    if now > old: # 현재 몸무게가 더 크다면
        if now ** 2 - old ** 2 == G: # 조건에 맞는 경우
            weights.append(now) 
            now += 1 # 두 포인터 모두 1씩 증가
            old += 1 
        elif now ** 2 - old ** 2 > G: # 현재 몸무게가 너무 큰 경우
            old += 1
        else: # 현재 몸무게가 너무 작은 경우
            now += 1
    else: # 현재 몸무게보다 과거 몸무게가 크거나 같다면, (사실 큰 경우는 없을 것이다.)
        now += 1

# 찾지 못한 경우
if len(weights) == 0:
    print(-1)

# 조건에 맞는 몸무게 출력
else:
    for weight in weights:
        print(weight)



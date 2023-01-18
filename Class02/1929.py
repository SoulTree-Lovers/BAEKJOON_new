# 소수 구하기

import math

a, b = map(int, input().split()) # a부터 b까지의 모든 수에 대하여 소수 판별
array = [True for i in range(b + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(b)) + 1): # 2부터 b의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= b:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(a, b+1):
    if array[i] and i != 1:
        print(i)
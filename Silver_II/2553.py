# 마지막 팩토리얼 수

n = int(input())

result = 1
for i in range(1, n+1): # 팩토리얼 구하기
    result *= i

result_str = str(result)[::-1] # 수 뒤집기

for digit in result_str: # 0이 아닌 숫자가 나올 때까지 반복
    if digit != '0':
        print(digit)
        break

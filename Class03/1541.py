# 잃어버린 괄호

expression = input()  # 식 입력

# 숫자와 연산자를 구분하여 리스트에 저장
numbers = []
operators = []
current_number = ""
for char in expression:
    if char.isdigit():
        current_number += char
    else:
        numbers.append(int(current_number))
        current_number = ""
        operators.append(char)
        
numbers.append(int(current_number))  # 마지막 숫자 처리

# 괄호 안의 식을 덧셈 연산으로 처리
i = 0
while i < len(operators):
    if operators[i] == '+':
        numbers[i] += numbers[i + 1]
        del numbers[i + 1]
        del operators[i]
    else:
        i += 1

# 남은 식에 대해 뺄셈 연산을 수행하여 최소값 계산
result = numbers[0]
for i in range(1, len(numbers)):
    result -= numbers[i]

print(result)  # 결과 출력

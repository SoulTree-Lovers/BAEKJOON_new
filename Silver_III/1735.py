# 분수 합

# 최대 공약수를 구하는 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 입력값 저장
a_num, a_den = map(int, input().split())
b_num, b_den = map(int, input().split())

# 두 분모의 최소공배수를 찾기
lcm = (a_den * b_den) // gcd(a_den, b_den)

# 두 분수를 동일한 분모(최소공배수)를 갖도록 변환
a_num *= lcm // a_den
b_num *= lcm // b_den

# 두 분수를 합산
result_num = a_num + b_num
result_den = lcm

# 결과 분수를 기약분수(가장 간단한 형태)로 단순화
divisor = gcd(result_num, result_den)
result_num //= divisor
result_den //= divisor

# 결과값 출력
print(result_num, result_den)

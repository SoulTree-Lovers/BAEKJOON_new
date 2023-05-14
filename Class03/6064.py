# 카잉 달력
import sys
input = sys.stdin.readline

def find_k(M, N, x, y):
    # 최대공약수를 구하는 함수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 최소공배수를 구하는 함수
    def lcm(a, b):
        return a * b // gcd(a, b)

    lcm_value = lcm(M, N)  # M과 N의 최소공배수

    while x <= lcm_value and y <= lcm_value:
        if x == y:
            return x
        elif x < y:
            x += M
        else:
            y += N

    return -1

# 입력 처리
T = int(input())  # 테스트 데이터 수

for _ in range(T):
    M, N, x, y = map(int, input().split())
    result = find_k(M, N, x, y)
    print(result)

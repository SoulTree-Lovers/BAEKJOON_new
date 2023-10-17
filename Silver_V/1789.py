# 수들의 합

# 자연수 s를 입력받는다.
# s는 서로 다른 n개 자연수의 합이다.
S = int(input()) 
total = 0
N = 1

while total + N <= S:
    total += N
    N += 1

print(N - 1)  # N을 출력할 때 1을 감소시킨 값을 출력


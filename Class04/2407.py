# 조합
import math
import fractions

n, m = map(int, input().split())

# 나눗셈 오차로 인해 Fraction 사용
print(int(fractions.Fraction(math.factorial(n), (math.factorial(m) * math.factorial(n-m)))))
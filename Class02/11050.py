# 이항 계수 1
import math
from fractions import Fraction # 부동소수점 오차 해결

n, k = map(int, input().split())

print(int(Fraction(math.factorial(n), (math.factorial(n-k) * math.factorial(k)))))

# 소수 찾기

import math

# 소수 판별
def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):	
    	if x % i == 0:
            return False
    return True		

n = int(input())
num_list = list(map(int, input().split()))
count = 0

for i in num_list:
    if primenumber(i) and i != 1:
        count += 1

print(count)
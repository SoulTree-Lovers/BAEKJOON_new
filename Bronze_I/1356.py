# 유진수

def mul_str(n):
    result = 1
    for i in n:
        result *= int(i)
    return result

n = input()

result = "NO"

for i in range(1, len(n)):
    # print(mul_str(n[:i]))
    # print(mul_str(n[i:]))
    if (mul_str(n[:i]) == mul_str(n[i:])):
        result = "YES"
        break
    
print(result)


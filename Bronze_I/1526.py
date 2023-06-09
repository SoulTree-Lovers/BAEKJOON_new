# 가장 큰 금민수

n = int(input())


curr = n
while curr <= n:
    if ("4" in str(curr) or "7" in str(curr)) and "1" not in str(curr) and "2" not in str(curr) and "3" not in str(curr) and "5" not in str(curr) and "6" not in str(curr) and "8" not in str(curr) and "9" not in str(curr) and "0" not in str(curr):
        print(curr)
        break
    curr -= 1
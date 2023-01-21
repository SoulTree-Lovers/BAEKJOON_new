# 설탕 배달

n = int(input())

five_sugar = n // 5
three_sugar = 0

total = n

while 1:
    total = n
    total -= five_sugar * 5 + three_sugar * 3
    
    if total < 3:
        if total == 0:
            print(five_sugar + three_sugar)
            break

        elif total < 0:
            print(-1)
            break
        
        if five_sugar > 0:
            five_sugar -= 1
        three_sugar += 1

    else:
    
        three_sugar += 1
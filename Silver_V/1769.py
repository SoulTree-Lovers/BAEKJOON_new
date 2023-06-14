# 3의 배수

n = input()
count = 0



while True:
    if len(n) == 1 and count == 0:
        print(0)
        if int(n) % 3 == 0:
            print("YES")
        else:
            print("NO")

        break

    count += 1
    n = str(sum([int(i) for i in n]))
    
    # print(n)
    
    if len(n) == 1:
        print(count)
        if int(n) % 3 == 0:
            print("YES")
        else:
            print("NO")

        break

    # count += 1
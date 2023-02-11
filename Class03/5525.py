# IOIOI

n = int(input())
m = int(input())
string = input()

count = 0
output = 0

i = 0

while i < m - 1:
    if string[i:i+3] == "IOI":
        count += 1
        i += 2

        if count == n:
            count -= 1
            output += 1
    else:
        i += 1
        count = 0
    

print(output)
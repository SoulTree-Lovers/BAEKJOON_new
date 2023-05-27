# 모음의 개수

import sys
input = sys.stdin.readline

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    string = input().strip()

    if string == "#":
        break
    
    count = 0
    for i in string:
        if i in vowels:
            count += 1

    print(count)


    
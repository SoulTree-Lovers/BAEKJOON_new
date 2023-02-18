# 대소문자 바꾸기

string = input()

for i in string:
    if i.islower():
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")

print()
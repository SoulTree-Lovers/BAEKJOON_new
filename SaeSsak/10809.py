# 알파벳 찾기
alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = input()

for i in alphabet:
    if i in string:
        print(string.index(i))
    else:
        print(-1)

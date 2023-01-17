# OX퀴즈

n = int(input())

for i in range(n):
    score = 0
    ox = input()

    seq = 1
    for s in ox:
        if s == 'O':
            score += seq
            seq += 1
        else:
            seq = 1

    print(score)


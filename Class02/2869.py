# 달팽이는 올라가고 싶다
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day = (V - B) // (A - B)

if (V - B) % (A - B) != 0:
    day += 1

print(day)
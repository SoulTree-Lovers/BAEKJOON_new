# 뒤집힌 덧셈

x, y = map(int, input().split())

def rev(x):
    x = str(x)

    return int(x[::-1])

print(rev(rev(x) + rev(y)))
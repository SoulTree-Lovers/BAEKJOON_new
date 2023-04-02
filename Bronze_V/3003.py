# 킹, 퀸, 룩, 비숍, 나이트, 폰

chess_pieces = [1, 1, 2, 2, 2, 8]

find_pieces = list(map(int, input().split()))

diff_pieces = []

for i in range(len(chess_pieces)):
    diff_pieces.append(chess_pieces[i] - find_pieces[i])

for i in diff_pieces:
    print(i, end=' ')

print()
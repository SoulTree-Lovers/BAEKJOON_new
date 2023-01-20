# 나무 자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

max_tree = max(trees)
min_tree = 1


while min_tree <= max_tree:
    cut = (min_tree + max_tree) // 2

    total = 0

    for i in trees:
        if i > cut:
            total += i - cut
        # print("1 cut: ", cut)
        # print("1 max tree: ", max_tree)
        # print("1 min tree", min_tree)
        
    if total >= m:
        min_tree = cut + 1
        # print("2 cut: ", cut)
        # print("2 max tree: ", max_tree)
        # print("2 min tree", min_tree)

    else:
        max_tree = cut - 1
        # print("3 cut: ", cut)
        # print("3 max tree: ", max_tree)
        # print("3 min tree", min_tree)
    
print(max_tree)

# 숫자 카드 2
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
has_card = list(map(int, input().split()))

num = int(input())
count_card = list(map(int, input().split()))


cnt = Counter(has_card)
for i in count_card:
    print(cnt[i], end=" ")
print()

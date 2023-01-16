# 평균
import math

n = int(input())

score_list = list(map(int, input().split()))

max_score = max(score_list)

for i, score in enumerate(score_list):
    score_list[i] = score / max_score * 100


print(sum(score_list)/len(score_list))
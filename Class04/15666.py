# N과 M (12)
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))
# combinations_with_replacement는 첫 파라미터의 첫 인덱스부터 뽑아내므로
# 오름차순으로 뽑아내기 위한 정렬
array.sort()  

array = list(set(combinations_with_replacement(array, m)))  # set으로 중복 제거
array.sort() 

for i in array:
    print(*i)




# ----------------------------------------------------------------
# for i in range(100000):
#     data = random.choices(array, k=m)
    
#     data.sort()
#     data = tuple(data)

#     if data not in answer:
#         answer.append(data)

# answer.sort()

# # print(answer)

# for i in answer:
#     for j in range(m):
#         print(i[j], end=" ")
#     print()

# 최소 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

output = []

for _ in range(n):
    num = int(input())
    
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            output.append(heapq.heappop(heap))
        except:
            output.append(0)


# print("----------------------------------------------------------------")
for i in output:
    print(i)
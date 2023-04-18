# 회의실 배정
# 1. 회의의 끝나는 시간을 기준으로 오름차순으로 정렬한다.
# 2. 가장 먼저 끝나는 회의를 선택한다.
# 3. 선택된 회의의 끝나는 시간 이후에 시작하는 회의 중 가장 먼저 끝나는 회의를 선택한다.
# 4. 3번 과정을 반복한다.

import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간을 기준으로 오름차순 정렬
count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time: # 이전 회의의 끝나는 시간 이후에 시작하는 회의라면
        count += 1
        end_time = end

print(count)

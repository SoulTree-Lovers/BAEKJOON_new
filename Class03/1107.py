# 리모컨

import sys
input = sys.stdin.readline
MAX_CHANNEL = 1000000 # 이동하려고 하는 채널이 50만이므로 채널을 더하거나 뺄 경우를 생각하여 100만으로 잡는다.

target = int(input())
n = int(input())
breakdown = list(map(int, input().split()))

# 현재 채널(100)에서 +혹은 -만 사용하여 이동하는 경우
min_count = abs(target - 100)


for nums in range(MAX_CHANNEL):
    nums = str(nums)
    
    for i in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break, 고장이 나지 않으면 그대로 진행
        if int(nums[i]) in breakdown:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif i == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)
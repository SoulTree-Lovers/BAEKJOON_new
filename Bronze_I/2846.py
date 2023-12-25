# 오르막길

def find_largest_increase(nums):
    max_increase = 0
    current_increase = 0
    curr_i = 0  # 현재 오르막길에서 가장 높은 값 - 1 (오르막길이 유지되는 지 비교하기 위해)
    curr_j = 1  # 현재 오르막길에서 가장 높은 값
    curr_k = 0  # 현재 오르막길에서 가장 낮은 값

    while True:
        # print(f"curr_i = {curr_i} \ncurr_j = {curr_j}")
        # print(f"current_increase = {current_increase}\nmax_increase = {max_increase}")
        if curr_j == len(nums):
            break
        
        if nums[curr_i] < nums[curr_j]:
            current_increase = nums[curr_j] - nums[curr_k]
            max_increase = max(max_increase, current_increase)

        else:
            current_increase = 0
            curr_k = curr_j
            
        curr_i += 1
        curr_j += 1

    return max_increase



# 입력 받기
N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
result = find_largest_increase(heights)
print(result)
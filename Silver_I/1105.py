# 팔

L, R = input().split()

def solution(L, R):
    if len(L) != len(R):
        return 0
    
    min_value = 0

    for i in range(len(L)):
        if L[i] == R[i]:    # and L[i] == '8' 로 묶으면 첫 번째 조건문 false 시 즉시 break하여 끝까지 탐색하지 못함.
            if L[i] == '8':
                min_value += 1
            else:
                pass
        else:
            break
    
    return min_value       


print(solution(L, R))
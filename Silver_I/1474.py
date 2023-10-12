# 밑 줄
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

strings = []
total_length = 0

for i in range(n):
    temp_string = input().strip()
    strings.append(temp_string)
    total_length += len(temp_string)

result_string = ""

# m 길이만큼 채우기 위해 필요한 밑줄 수
needed_line = m - total_length

# 문자열 사이를 채울 최소 라인 수
one_line = needed_line // (n - 1)

# 문자열 사이를 최소 라인으로 채우고 남은 라인 수 (더 채워야 할 라인)
add_line = needed_line % (n - 1)

count = n - 1

for i in range(n):
    result_string += strings[i]
    
    if count > 0:
        result_string += "_" * one_line
        count -= 1

    if add_line > 0 and i < n - 1 and strings[i+1] > "_":
        result_string += "_"
        add_line -= 1

    if add_line > 0 and add_line >= n - i - 1:
        result_string += "_"
        add_line -= 1


    
print(result_string)
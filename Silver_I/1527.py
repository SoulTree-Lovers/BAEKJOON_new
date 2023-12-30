# 금민수의 개수

def count_gumminsu(A, B):
    def generate_gumminsu(n):
        # 금민수를 생성하는 함수
        if n > B:
            return 0
        count = 0
        if n >= A:
            count += 1
        count += generate_gumminsu(n * 10 + 4)  # 4를 추가한 경우
        count += generate_gumminsu(n * 10 + 7)  # 7을 추가한 경우
        return count

    result = generate_gumminsu(0)
    return result

# 입력 받기
A, B = map(int, input().split())

# 금민수 개수 출력
result = count_gumminsu(A, B)
print(result)
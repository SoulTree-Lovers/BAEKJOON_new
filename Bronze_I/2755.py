# 이번학기 평점은 몇점?

import sys
input = sys.stdin.readline

def grade2number(grade):
    if grade == "A+":
        return 4.3
    elif grade == "A0":
        return 4.0
    elif grade == "A-":
        return 3.7
    elif grade == "B+":
        return 3.3
    elif grade == "B+":
        return 3.3
    elif grade == "B0":
        return 3.0
    elif grade == "B-":
        return 2.7
    elif grade == "C+":
        return 2.3
    elif grade == "C0":
        return 2.0
    elif grade == "C-":
        return 1.7
    elif grade == "D+":
        return 1.3
    elif grade == "D0":
        return 1.0
    elif grade == "D-":
        return 0.7
    elif grade == "F":
        return 0

# 파이썬의 round 함수의 오류를 해결하는 원래의 반올림 함수 구현
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

n = int(input())

courses = []

total_weight = 0
total_grade = 0

for i in range(n):
    course, weight, grade = input().strip().split(" ")
    total_weight += float(weight)
    total_grade += grade2number(grade) * float(weight)

result = roundTraditional(total_grade / total_weight, 2)
print("%.2f" %result)

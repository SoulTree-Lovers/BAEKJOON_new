# 음하철도 구구팔
import math

# 최대공약수를 구하는 함수
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

# 두 수를 최대공약수로 나누어 리턴하는 함수
def simplify_fraction(a, b):
    gcd = greatest_common_divisor(a, b)
    return (a // gcd, b // gcd)


# 두 좌표 사이의 거리를 구해주는 함수
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())


min_dx, min_dy = simplify_fraction(dx, dy)

min_distance = calculate_distance(xs, ys, xe, ye)

while True:
    curr_xe, curr_ye = xe + min_dx, ye + min_dy 
    curr_distance = calculate_distance(xs, ys, curr_xe, curr_ye)

    if min_distance <= curr_distance:
        print(xe, ye)
        break

    if min_distance > curr_distance:
        min_distance = curr_distance
        xe += min_dx
        ye += min_dy

    
    
# 좌표 압축

import sys
input = sys.stdin.readline

def coordinate_compression(N, coordinates):
    sorted_coords = sorted(set(coordinates))
    coord_dict = {coord: idx for idx, coord in enumerate(sorted_coords)}
    compressed_coords = [coord_dict[coord] for coord in coordinates]
    return compressed_coords

# 입력 받기
N = int(input())
coordinates = list(map(int, input().split()))

# 좌표 압축 적용
compressed_coords = coordinate_compression(N, coordinates)

# 결과 출력
print(*compressed_coords)

# n = int(input())

# num_list = list(map(int, input().split()))

# new_list = []

# for i in num_list:
#     count = 0

#     for j in num_list:
#         if i > j:
#             count += 1

#     new_list.append(count)

# print(*new_list)

# # for i in new_list:
# #     print(i, end=" ")

# # print()
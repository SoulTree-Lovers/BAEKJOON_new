# 토마토

from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

tomatoes=deque() #deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            tomatoes.append((i,j)) #익은 토마토 위치 넣기

def bfs():
    while tomatoes:
        x=tomatoes[0][0]
        y=tomatoes[0][1]
        tomatoes.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if arr[nx][ny]==0: #아직 방문하지 않은 경우
                    arr[nx][ny]=arr[x][y]+1
                    tomatoes.append((nx,ny))

def result():
    answer = 0
    for num in arr:
        if 0 in num:
            answer = -1

    if answer == -1: #토마토가 모두 익지는 못하는 상황인 경우
        print(-1)
    else:
        print(max(map(max, arr)) - 1)

bfs()
result()


# ---------------------시간초과---------------------
# import sys
# import copy
# from collections import deque
# input = sys.stdin.readline

# m, n = map(int, input().split()) # m: 가로, n: 세로

# tomatoes = deque()

# for i in range(n):
#     tomatoes.append(input().split())

# temp = copy.deepcopy(tomatoes)

# all_ripe = False


# # 처음부터 다 익어있는 경우
# for tomato in tomatoes:
#     all_ripe = True
#     if "0" in tomato:
#         all_ripe = False
#         break

# if all_ripe == True:
#     print(0)
#     exit(0)


# for days in range(n*m):
#     # print(tomatoes)
#     # 토마토가 다 익으면 break
#     for i in range(n):
#         for j in range(m):
#             if tomatoes[i][j] == "1":
#                 if i+1 < n and tomatoes[i+1][j] != "-1":
#                     temp[i+1][j] = "1"
#                 if i-1 >= 0 and tomatoes[i-1][j] != "-1":
#                     temp[i-1][j] = "1"
#                 if j+1 < m and tomatoes[i][j+1] != "-1":
#                     temp[i][j+1] = "1"
#                 if j-1 >= 0 and tomatoes[i][j-1] != "-1":
#                     temp[i][j-1] = "1"

#     tomatoes = copy.deepcopy(temp)         

#     for tomato in tomatoes:
#         all_ripe = True
#         if "0" in tomato:
#             all_ripe = False
#             break

#     if all_ripe == True:
#         print(days+1)
#         break

# if all_ripe == False:
#     print(-1)

    


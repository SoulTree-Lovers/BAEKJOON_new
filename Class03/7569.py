# 토마토 
from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

# print(m, n, h)
# print(arr)

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

tomatoes=deque() #deque

for i in range(h):
    for j in range(n):
        for k in range(m):
                if arr[i][j][k] == 1:
                    tomatoes.append((i,j,k)) #익은 토마토 위치 넣기

def bfs():
    while tomatoes:
        x=tomatoes[0][0]
        y=tomatoes[0][1]
        z=tomatoes[0][2]
        tomatoes.popleft()

        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]

            if nx>=0 and nx<h and ny>=0 and ny<n and nz>=0 and nz<m:
                if arr[nx][ny][nz] == 0 and visited[nx][ny][nz] == False: #아직 방문하지 않은 경우
                    arr[nx][ny][nz] = arr[x][y][z] + 1
                    tomatoes.append((nx,ny,nz))
                    visited[nx][ny][nz] = True

def result():
    answer = 0
    for i in arr:
        for j in i:
            for k in j:
                if k == 0:
                    return -1
            answer = max(answer, max(j))
            
    return answer - 1
    # print(arr)

# 모두 1이 아니라면
if_all_not_one = True

for i in arr:
    for j in i:
        if 1 in j:
            if_all_not_one = False

if if_all_not_one:
    print(-1)
    exit(0)

bfs()
print(result())



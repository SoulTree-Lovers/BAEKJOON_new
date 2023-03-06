# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

# 부모 저장 배열
parent_list = [0] * (n+1)

# 양방향 연결 정보 저장
graph = [[] for _ in range(n+1)]

for _ in range(n-1):

    # 양방향 연결 정보 입력 및 저장
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)

# 부모 노드 탐색
def dfs(root):

    # 현재 노드와 연결된 노드 확인
    for i in graph[root]:

        # 연결된 노드의 부모가 없다면
        if (parent_list[i] == 0):

            # 현재 노드를 연결된 노드의 부모 노드로 설정
            parent_list[i] = root

            # 연결된 노드들 기준으로 DFS 진행
            dfs(i)


# 1번 노드부터 탐색 시작
dfs(1)

# 2번 노드부터 부모 노드 번호 출력
for i in range(2, n+1):
    print(parent_list[i])

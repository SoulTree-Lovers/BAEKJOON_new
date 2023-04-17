from collections import deque

def bfs(n, k):
    queue = deque([(n, 0)])
    visited = set([n])

    while queue:
        pos, time = queue.popleft()

        if pos == k:
            return time

        for next_pos in [pos-1, pos+1, pos*2]:
            if next_pos >= 0 and next_pos <= 100000 and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, time+1))

n, k = map(int, input().split())
print(bfs(n, k))

# 먼저 collections 모듈에서 deque를 가져옵니다. deque는 스택과 큐의 기능을 모두 갖춘 자료형입니다. 큐를 구현하기에 적합하며, 이 문제에서는 BFS를 구현하기 위해 사용합니다.
# bfs 함수는 수빈이의 현재 위치 n과 동생의 위치 k를 인자로 받습니다. queue라는 빈 deque와 visited라는 빈 집합을 만들어줍니다.
# queue에는 튜플로 (현재 위치, 현재 시간)을 삽입합니다. 여기서 현재 시간은 현재 위치까지 도달하는 데까지 걸린 시간을 의미합니다.
# visited 집합은 방문한 위치를 저장하기 위한 집합입니다. 현재 위치를 방문했다는 것을 기억하기 위해 현재 위치를 집합에 추가합니다.
# queue가 빌 때까지 아래의 과정을 반복합니다.
# queue에서 가장 먼저 들어온 요소를 pos, time이라는 변수에 할당합니다. pos는 현재 위치, time은 현재 위치까지 도달하는 데까지 걸린 시간을 의미합니다.
# 현재 위치가 동생의 위치와 같다면 time을 반환합니다.
# 현재 위치에서 +1, -1, *2한 값을 next_pos라는 변수에 할당합니다.
# next_pos가 0과 100000 사이에 있으며, visited 집합에 없다면, visited 집합에 next_pos를 추가하고, queue에 (next_pos, time+1)을 삽입합니다. time+1은 next_pos까지 도달하는 데까지 걸린 시간입니다.
# 위 코드를 실행하면 입력으로 주어진 수빈이와 동생의 위치에 대해 최단 거리를 찾아 출력합니다.
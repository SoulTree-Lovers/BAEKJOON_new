# 케빈 베이컨의 6단계 법칙
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


# function to calculate Kevin Bacon number for a given user
def kevin_bacon_number(user, graph):
    # initialize distance to all users as infinity
    distances = {u: float('inf') for u in graph}
    # set distance to current user as 0
    distances[user] = 0
    # use breadth-first search to calculate distances
    queue = deque([user])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    # return the sum of distances as Kevin Bacon number
    return sum(distances.values())

# read input
N, M = map(int, input().split())
graph = defaultdict(set)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)
    graph[B].add(A)

# calculate Kevin Bacon number for each user
kevin_bacon_numbers = {user: kevin_bacon_number(user, graph) for user in graph}

# find user with smallest Kevin Bacon number
min_kevin_bacon = float('inf')
min_user = None
for user, kevin_bacon in kevin_bacon_numbers.items():
    if kevin_bacon < min_kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_user = user
    elif kevin_bacon == min_kevin_bacon and user < min_user:
        min_user = user

# print the result
print(min_user)

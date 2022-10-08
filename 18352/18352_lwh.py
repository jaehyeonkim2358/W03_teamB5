import sys
from collections import deque, defaultdict
sys.stdin = open('18352/18352_lwh.txt', 'r')
input = sys.stdin.readline

def bfs(graph, start, costs, visited):
    queue = deque([start])
    costs[start] = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                costs[i] = costs[v] + 1
                visited[i] = True
                queue.append(i)
    flag = False    
    for idx, cost in enumerate(costs):
        if cost == K:
            print(idx)
            flag = True
    if flag == False:
        print(-1)
N, M, K, X = map(int, input().split())
graph = defaultdict(list)
costs = [-1] * (N + 1)
visited = [False] * (N + 1)
for _ in range(M):
    edge = list(map(int, input().split()))
    u, v = edge[0], edge[1]
    graph[u].append(v)

bfs(graph, X, costs, visited)


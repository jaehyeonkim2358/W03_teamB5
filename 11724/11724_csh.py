from collections import deque
from sys import stdin
input = stdin.readline
 
def bfs(graph, start, visited):     
    queue = deque([start])
    visited[start] = True
 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
 
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]         
visited = [False] * (N + 1)
 
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node2].append(node1)
    graph[node1].append(node2)
 
cnt = 0
for i in range(1, N+1):     
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
print(cnt)

from sys import stdin
input = stdin.readline
 
def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)
 
pc = int(input())
link = int(input())
 
graph = [[] for _ in range(pc + 1)]
visited = [False] * (pc + 1)
cnt = 0    
 
for i in range(link):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
 
dfs(graph, 1, visited)
print(cnt)

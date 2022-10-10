from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e9))
input = stdin.readline

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]

    edges = []
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        edges.append((a, b))

    visited = [False] * (v+1)
    mark = [0] * (v+1)

    ans = "YES"

    def dfs(i):
        for j in graph[i]:
            if visited[j] == False:
                visited[j] = True
                mark[j] = -mark[i]
                dfs(j)
    
    for i in range(1, v+1):
        if visited[i] == False:
            visited[i] = True
            mark[i] = 1
            dfs(i)

    for edge in edges:
        if mark[edge[0]] == mark[edge[1]]:
            ans = "NO"
            break
    print(ans)

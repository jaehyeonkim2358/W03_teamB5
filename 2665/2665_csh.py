from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def dijkstra():
    q = []
    heappush(q, [0, 0, 0])
    visited[0][0] = 1
    while q:
        cost, x, y = heappop(q)
        if x == n - 1 and y == n - 1:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n -1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    heappush(q, [cost + 1, nx, ny])
                else:
                    heappush(q, [cost, nx, ny])


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

print(dijkstra())

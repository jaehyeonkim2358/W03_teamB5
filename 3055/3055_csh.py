from collections import deque
from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*":
                queue.appendleft((i, j))
                visited[i][j] = 0
            elif graph[i][j] == "S":
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not 0 <= nx < r or not 0 <= ny < c:
                continue
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] == "*" or graph[nx][ny] == "X":
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "*":
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "S":
                return visited[x][y] + 1

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            graph[nx][ny] = graph[x][y]

    return "KAKTUS"


print(bfs())

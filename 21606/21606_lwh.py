import sys
from collections import deque, defaultdict
sys.stdin = open('21606/21606_lwh.txt', 'r')
input = sys.stdin.readline

# 실내 1
# 실외 0 
# 갔던 곳 2

# 각 실내 (u.cost == 1 )에서 출발. 모든 실내 포인트 스택에 넣어주고 dfs 한번 실행하면 될듯
# v.cost == 1 만나면 종료, count += 1, visited ==2 만나면 그냥 종료
# v.cost == 0 만나면 v.cost = 2 로 갱신 (방문)
# 결과 count 출력하면 시간초과~~

def dfs(places, graph, node):
    h = []
    h.append(node)

    places[node] = 2
    
    n = 0

    while h:
        u = h.pop()
        for v in graph[u]:
            if not places[v]:
                places[v] = 2
                h.append(v)
            elif places[v] == 1:
                n += 1
    return n            

def init():
    graph = defaultdict(set)

    N = int(input())

    places = deque(list(map(int, list(input().rstrip()))))
    places.appendleft([False])
    outdoors = set()
    for idx in range(1, N+1):
        if not places[idx]:
            outdoors.add(idx)

    cnt = 0
    for _ in range(N-1):
        u, v = map(int, input().split())
        if places[u] and places[v] :
            cnt += 2
            continue 
        graph[u].add(v)
        graph[v].add(u)

    for idx in range(len(outdoors)):
        node = outdoors.pop()
        if places[node] == 2:   # 이미 체크한 덩어리 패스
            continue
        n = dfs(places, graph, node)
        cnt += n*(n-1)

    print(cnt)

init()

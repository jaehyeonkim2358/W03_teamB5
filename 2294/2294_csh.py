from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
check = [0 for _ in range(k+1)]

def bfs(coins, k):
    queue = deque()
    for coin in coins:
        if coin > k:
            continue
        queue.append([coin, 1])
        check[coin] = 1

    flag = True
    while queue:
        val, cnt = queue.popleft()
        if val == k:
            print(cnt)
            flag = False
            break
            
        for coin in coins:
            if val + coin > k:
                continue
            if check[val+coin] == 0:
                check[val+coin] = 1
                queue.append([val+coin, cnt+1])
                
    if flag:
        print(-1)

bfs(coins, k)

# 숨바꼭질
# https://www.acmicpc.net/problem/1697

import sys
from collections import deque

def bfs(v):
    dq = deque([v])
    while dq:
        v = dq.popleft()
        if v == K:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                dq.append(i)

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
print(bfs(N))

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not visited[next_v]:
                visited[next_v] = visited[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
print(bfs(n))
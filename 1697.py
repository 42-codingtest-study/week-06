#꼭꼭 숨어라 머리카락 보일라
import sys
input = sys.stdin.readline
from collections import deque

MAX = 100001
n, k = map(int, input().split())
result = [0] * MAX

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return result[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i < MAX and not result[i]:
                result[i] = result[v] + 1
                q.append(i)

print(bfs(n))
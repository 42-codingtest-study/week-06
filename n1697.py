
from collections import deque

def bfs(n):
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k: # 수빈이 위치 = 동생 위치
            return visited[x]

        for j in (x - 1, x + 1, x * 2):
            if 0 <= j <= MAX and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

n, k = map(int, input().split(" "))
MAX = 100000

visited = [[0] * (MAX + 1)]
print(bfs(n))
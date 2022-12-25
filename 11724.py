#hmm
import sys
input = sys.stdin.readline
#재귀 허용 깊이를 수동으로 늘려주는 코드
sys.setrecursionlimit(10 ** 9)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count+=1
        dfs(i)

print(count)
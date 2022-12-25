#아이스아이스 페엥귄은 귀여웡
import sys
input = sys.stdin.readline
# 재귀함수 횟수 제한을 늘려줌
sys.setrecursionlimit(10 ** 9)

N, S, P = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

Broken = []
visited = [0] * (N+1)

def dfs(n, cnt):
    # 펭귄치면 끝
    if n == P:
        Broken.append(cnt)
        return
    visited[n] = 1
    for i in graph[n]:
        # 해당 얼음과 연결된 얼음 탐색
        if not visited[i]:
            dfs(i, cnt + 1)

# 6개의 얼음 기둥 탐색
for i in range(1, S+1):
	if not visited[i] :
		dfs(i, 0)

Broken.sort()

print(N - 1 - Broken[0] - Broken[1])
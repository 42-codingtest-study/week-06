
import sys

input = sys.stdin.readline

n, s, p = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

BrokenIce = []
visited = [0] * (n + 1)

def dfs(x, cnt):
    # 방문한 얼음에 펭귄이 서있으면 얼음에 연결된 얼음 갯수 반환
    if x == p:
        BrokenIce.append(cnt)
        return

    visited[x] = 1

    for i in graph[x]:
        # 연결된 얼음 탐색
        if not visited[i]:
            dfs(i, cnt + 1)

for i in range(1, s + 1):
    dfs(i, 0)

# 전체 - 연결 제일 적은 기둥 2개 - 펭귄 있는 얼음
print(n - BrokenIce[0] - BrokenIce[1] - 1)
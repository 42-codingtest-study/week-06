import sys
sys.setrecursionlimit(999999)
input = sys.stdin.readline

def dfs(start, end):
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i, end + 1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (1 + N)
count = 0 

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = count # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색을 돈다.
            count += 1  # 개수를 +1

print(count)
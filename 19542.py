# 전단지 돌리기
# https://www.acmicpc.net/problem/19542

N, S, D = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1) :
    x, y = map(int, input().split())
    graph[x].append(y)
    # graph[y].append(x)

def dfs(curr) :		# D를 어떻게 써야할지 모르겠다 ...
    if len(graph[curr]) == 0 :
        visited[curr] = 0
        # print(curr, visited)
        return
    visited[curr] = 1
    # print(curr, visited)
    for i in graph[curr] :
        if visited[i] == 0 :
            dfs(i)
            
dfs(S)
print(graph)
print(visited)
print(sum(visited) * 2)
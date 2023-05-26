# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(t) :
    visited[t] = 1
    for next in graph[t] :
        if visited[next] == 0 :
            dfs(next)
    
answer = 0
visited = [0] * (N + 1)
for i in range(1, N + 1) :
    if (visited[i] == 0) :
        dfs(i)
        answer += 1

print(answer)
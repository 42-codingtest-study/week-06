# 색칠하기
# https://www.acmicpc.net/problem/13265

import sys
from collections import deque

input = sys.stdin.readline
def dfs(v) :
    if 0 not in set(visited) :
        return
    for i in graph[v] :
        if visited[i] == 0 :
            if visited[v] == 1 :
                visited[i] = 2
                dfs(i)
            else :
                visited[i] = 1
                dfs(i)

T = int(input())
for _ in range(T) :
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [0] * n
    for _ in range(m) :
        x, y = map(int, input().split())
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    visited[0] = 1
    dfs(0)
    for i in range(n) :
        if visited[i] == 0 :
            dfs(i)
            
    answer = True
    for i in range(len(graph)) :
        c = visited[i]
        for j in graph[i] :
            if visited[j] == c :
                answer = False
    if answer :
        print("possible")
    else :
        print("impossible")
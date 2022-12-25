# _*_ coding: utf-8 _*_
#백준 11724 > 연결 요소의 개수
#풀이방식: dfs

import sys
sys.setrecursionlimit(10 ** 6) #런타임에러 허용 범위 넓혀주기
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1) #사용하기 편하도록 N + 1 크기로 선언하여 인덱스 자체를 정점 번호로 사용함
count  = 0 #연결 요소 개수
    
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
# _*_ coding: utf-8 _*_
#백준 21738 > 얼음깨기 펭귄
#얼음 블록의 개수 N, 지지대 역할 S, 펭귄이 위치한 번호 P

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) #런타임에러 허용 범위 넓혀주기

N, S, P = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

broken = []
visited = [0] * (N + 1) #방문한 얼음

def dfs(N, count):
    if N == P: #현재 방문한 얼음이 펭귄이 서있는 곳과 동일하면
        broken.append(count) #기둥의 연결 얼음 갯수 반환
        return
    visited[N] = 1
    for i in graph[N]:
        if not visited[i]:
            dfs(i, count + 1) #해당 얼음과 관련된 탐색(dfs)

for i in range(1, S + 1): #6개의 얼음 기둥 탐색
    dfs(i, 0)

broken.sort()
print(N - broken[0] - broken[1] - 1) #전체 얼음 - 가장 연결갯수가 적은 기둥 2개 - 펭귄 서있는 얼음
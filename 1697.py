# _*_ coding: utf-8 _*_
#백준 1697 > 숨바꼭질
#풀이방식: bfs

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
max = 100000 #N, K 범위 0부터 1000000
visited = [0] * (max + 1) #배열을 최대수만큼 생성하고 0으로 초기화

def bfs():
    q = deque() #큐를 빠르게 해주기 위해 deque 사용
    q.append(N) #수빈이가 있는 위치(=출발점)을 넣어준다
    
    while q:
        x = q.popleft()
        if x == K: #N == K가 된다면 이동한 거리 출력하기
            print(visited[x])
            break
        
        for i in (x - 1, x + 1, x * 2):
            if 0<=i<=max and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

bfs()
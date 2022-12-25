#헤이토니~
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    global res
	
    q.append(x)
    visited[x] = 1
    # 색깔 변수(기본값으로 그냥 2 해줬음)
    color = 2
    while q:
        circle_num = q.popleft()
        # 그 번호의 동그라미 색과 다른 색을 color 변수에 저장
        if visited[circle_num] == 1:
            color = 2
        else:
            color = 1
        # 해당 동그라미 이웃 방문
        for i in info[circle_num]:
            if visited[i] == 0:
                visited[i] = color
                q.append(i)
            else:
				# 서로의 색 비교해서 같으면
                if visited[circle_num] == visited[i]:
                    res = 1
        if res == 1 : break


test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    info = [[] for _ in range(n + 1)]
    # 양방향으로 데이터 받기
    for i in range(m):
        x, y = map(int, input().split())
        info[x].append(y)
        info[y].append(x)
	
    # 기본 값으로 possible
    res = 0
    q = deque()
    bfs(1)

	# 끊어진 그래프가 나올수 있기 때문에 한번 더 탐색
    for i in range(n+1):
        if visited[i] == 0:
            bfs(i)

    if(res == 0):
        print("possible")
    else:
        print("impossible")
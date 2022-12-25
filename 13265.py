from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    global res
	
    # x는 1이 들어옴
    q.append(x)
    # 1번 동그라미의 색은 1
    visited[x] = 1
    # 색깔 변수(기본값으로 그냥 2 해줬음)
    color = 2
    while q:
    	# 큐에서 pop해서
        circle_num = q.popleft()
        # 그 번호의 동그라미 색과 다른 색을 color 변수에 저장(1이라면 2를, 2라면 1을)
        if visited[circle_num] == 1:
            color = 2
        else:
            color = 1
        # 해당 동그라미 이웃 방문
        for i in graph[circle_num]:
        	# 만약 방문을 안한 원이면
            if visited[i] == 0:
            	# 색을 칠하고
                visited[i] = color
                # 큐에 넣어주기
                q.append(i)
            # 방문을 한 동그라미라면
            else:
            	# 서로의 색 비교해서 같으면 impossible로 한 뒤 break!
                if visited[circle_num] == visited[i]:
                    res = 'impossible'
        if res == 'impossible': break


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    visited = [0] * (n+1)
    graph = [[] for k in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
	
    # 기본 값으로 possible
    res = 'possible'
    q = deque()
    bfs(1)

	# 색칠 안된 것들도 있을 수 있으니 한번 더 bfs탐색 
    for i in range(n+1):
        if visited[i] == 0:
            bfs(i)

    print(res)
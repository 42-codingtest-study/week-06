
from collections import deque

def bfs(x):
    q.append(x)
    circles[x] = 1

    color = 1 # 기본값

    while q:
        circles_num = q.popleft()

        # 동그라미 색과 다른 색을 color 변수에 저장
        if circles[circles_num] == 1:
            color = 2
        else:
            color = 1

        for i in graph[circles_num]:
            if circles[i] == 0: # 첫 방문일때
                circles[i] == color
                q.append(i)
            else:
                if circles[circles_num] == circles[i]: # 색 비교해서 같으면 impossible
                    output = "impossible"

        if output == "impossible":
            break



t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    circles = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

output = "possible" # 기본값
q = deque()

bfs(1)

# 색칠 안된 부분이 있는지 다시 탐색
for i in range(n + 1):
    if graph[i] == 0:
        bfs(i)

print(output)
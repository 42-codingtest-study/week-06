#n단 논법스
import sys
input = sys.stdin.readline

n = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
N = len(alphabet)

graph = [[0] * N for _ in range(N)]

for _ in range(n):
    x, y = map(alphabet.index, input().rstrip().split(" is "))
    graph[x][y] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] + graph[i][k] == 2:
                graph[j][k] = 1
            #graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

n2 = int(input())

for _ in range(n2):
    x, y = map(alphabet.index, input().rstrip().split(" is "))

    if graph[x][y] == 0:
        print("F")
    else:
        print("T")
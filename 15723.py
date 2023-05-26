# n단 논법
# https://www.acmicpc.net/problem/15723

def dfs(a, b) :
    if a == b :
        print("T")
        return
    if len(graph[a]) == 0 :
        print("F")
        return
    visited[a] = 1
    for next in graph[a] :
        if visited[next] == 0 :
            dfs(next, b)

n = int(input())
graph = [[] for _ in range(26)]
for _ in range(n) :
    a, _, b = input().split()
    graph[ord(a) - 97].append(ord(b) - 97)
    
m = int(input())
for _ in range(m) :
    a, _, b = input().split()
    visited = [0] * 26
    dfs(ord(a) - 97, ord(b) - 97)

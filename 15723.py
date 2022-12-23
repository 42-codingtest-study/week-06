import sys
input = sys.stdin.readline

def dfs(first, last):
    if first == last:
        print("T")
        return
    if len(graph[first]) == 0:
        print("F")
        return
    for i in graph[first]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, last)
    
n = int(input())
graph = [[] for i in range(26)]
for _ in range(n):
    first, mid, last = input().split()
    first_idx = ord(first) - ord('a')
    # print(first_idx)
    last_idx = ord(last) - ord('a')
    # graph[first_idx] += graph[last_idx]
    graph[first_idx].append(last_idx)
    
    
M = int(input())
for _ in range(n):
    first, mid, last = input().split()
    visited = [0] * 26 # for i in range(26)]
    # print(first, second)
    first_idx = ord(first) - ord('a')
    last_idx = ord(last) - ord('a')
    visited[first_idx] = 1
    dfs(first_idx, last_idx)    
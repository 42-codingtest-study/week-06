# _*_ coding: utf-8 _*_
#백준 15723 > n단 논법

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) #런타임에러 허용 범위 넓혀주기

n = int(input())
graph = {i:[] for i in range(26)}
level = {i:0 for i in range(26)}

def dfs(cur_node, Target):
    if cur_node == Target:
        return True
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            if dfs(next_node, Target):
                return True

for _ in range(n):
    first, arrow, end = input().split()
    first_num = ord(first) - 97 #알파벳
    end_num = ord(end) - 97
    graph[first_num] += [end_num]
    
m = int(input())   
for _ in range(m):
    first, arrow, end = input().split()
    visited = {i: False for i in range(26)}
    first_num = ord(first) - 97
    end_num = ord(end)-97
    visited[first_num] = True
    print('T' if dfs(first_num, end_num) else 'F')
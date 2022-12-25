# _*_ coding: utf-8 _*_
#백준 13265 > 색칠하기
#오류 있음> 메모리 초과

import sys
input = sys.stdin.readline
# from collections import deque
sys.setrecursionlimit(10 ** 6)

t = int(input())
output = ''
n, m = map(int, input().split())
graph = [[]for _ in range(n + 1)]
check = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, n + 1):
    if not check[j]:
        stack = [[j, 1]]
        result = 'possible'
        
        while stack:
            cur_node, next_color = stack.pop()
            if check[cur_node] and check[cur_node] != cur_node:
                result = 'impossible'
                break
            check[next_color] = cur_node
            
            for next_node in graph[cur_node]:
                if not check[next_node]:
                    stack.append([next_node, -next_color])
        
        if result == 'impossible':
            output += result + '\n'
            break
    if result == 'possible':
        output += result + '\n'
print(output)
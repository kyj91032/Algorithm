
# 11724 연결 요소의 개수 - input = sys.stdin.readline. dfs가 끝나도 visited를 계속 이용

import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [0] * (n + 1)

cnt = 0

def dfs(graph, v, visited):
	visited[v] = 1
	for i in graph[v]:
		if visited[i] == 0:
			dfs(graph, i, visited)

for i in range(1, n + 1):
	if not visited[i]: # 방문하지 않은 것만. visited 의 연결. dfs가 끝나도 visited를 이용해 탐색여부를 판단하고, 연결요소의 개수를 구할 수 있음
		dfs(graph, i, visited)
		cnt += 1
print(cnt)
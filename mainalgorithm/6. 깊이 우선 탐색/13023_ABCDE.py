
# 13023 ABCDE - 그래프임은 확실, 깊이가 5이상인지 판단하는 것 => dfs. 모든 경우를 탐색해야 하므로, 인접노드를 다 확인한 노드는 자취를 지움.

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m): # 순회하며 확인해야 하므로, 인접 리스트 방식으로 그래프 저장
	tmp = list(map(int, input().split()))
	for j in range(n):
		if tmp[0] == j:
			graph[j].append(tmp[1])
			graph[tmp[1]].append(j)
			break
visited = [0] * n
s = []
m = 0

def dfs(graph, v, visited):
	visited[v] = 1
	s.append(v)
	global m # 전역변수 m 선언. 외부 m과 연결됨. s는 리스트라서 재할당시에만 global 필요함
	m = max(m, len(s))
	if m >= 5:
		for p in range(n):
			visited[p] = 1
		return
	for k in graph[v]:
		if visited[k] == 0:
			dfs(graph, k, visited)
	s.pop()
	visited[v] = 0 # dfs 중에 자취(visited)를 지워가며 dfs를 한다. 모든 경우를 순회하기 위해서. 지우는 타이밍은 pop()을 할 때와 동일.

for i in range(n):
	dfs(graph, i, visited)
	if m >= 5:
		print(1)
		break
	visited = [0] * n
	

if m <= 4:
	print(0)

# 13549 숨바꼭질3 - bfs의 조건. 모든 간선의 가중치가 동일해야 한다는 전제 조건. 이 문제는 *2를 먼저 실행해야 통과됨. 아마 0초인걸 먼저해야 최초의 visited가 최소가 돼서 그런듯.

from collections import deque

n, k = map(int, input().split())

graph = [0] * 100001

d = [-1, 1]

def bfs(start, end):
	queue = deque([start])
	graph[start] += 1
	while queue:
		v = queue.popleft()
		nx = v * 2
		if nx >= 0 and nx <= 100000 and graph[nx] == 0:
			queue.append(nx)
			graph[nx] = graph[v]
		for i in range(2):
			nx = v + d[i]
			if nx < 0 or nx > 100000 or graph[nx] != 0:
				continue
			queue.append(nx)
			graph[nx] = graph[v] + 1
		if graph[k]:
			print(graph[k] - 1)
			break
bfs(n, k)


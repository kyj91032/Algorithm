# 7562 나이트의 이동 - 격자그래프, bfs의 탐색 경로 정의

from collections import deque

T = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	graph[x][y] = 1
	while queue:
		x, y = queue.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= n:
				continue
			if graph[nx][ny] == 0:
				graph[nx][ny] = graph[x][y] + 1
				queue.append((nx, ny))
	print(graph[p][q] - 1)
	return

for _ in range(T):
	n = int(input())
	a, b = map(int, input().split())
	p, q = map(int, input().split())
	graph = [[0] * n for i in range(n)]
	
	bfs(a, b)

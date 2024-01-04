
# 1261 알고스팟 - bfs에서 조건에 따라 우선적으로 실행하는 방법: queue.appendleft()하면 됨, 격자그래프에서 visited 사용

from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)] # 격자그래프지만 graph의 값이 따로 정보를 갖고있다면 visited를 따로 써야함

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	visited[x][y] = 0
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx >= m or nx < 0 or ny < 0 or ny >= n:
				continue
			if visited[nx][ny] != -1:
				continue
			if graph[nx][ny] == 0:
				visited[nx][ny] = visited[x][y]
				queue.appendleft((nx, ny)) # 벽 없는곳 먼저 뚫기
			if graph[nx][ny] == 1:
				visited[nx][ny] = visited[x][y] + 1
				queue.append((nx, ny))
	print(visited[m-1][n-1])
bfs(0, 0)
# 넓이 우선 탐색(BFS): 가중치가 1인 그래프에서, 탐색하지 않은 인접 노드를 우선으로 최대한 넓게 탐색하여 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 방법이다.
# 큐가 선입선출이라 넓이 우선 탐색이 가능한 것. bfs는 큐를 이용하므로 큐와 반복문을 같이 쓴다.

# BFS의 기본적인 동작 과정과 코드

1. 탐색 시작 노드를 매개변수로 받아 방문 처리를 하고 큐에 추가한다.
2. 탐색한 노드를 큐에서 빼고, 그 노드의 탐색 안한 인접 노드를 큐에 넣으며 탐색 처리를 한다.


# BFS

from collections import deque

graph = [ # 인접 리스트 방식.
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

def bfs(graph, start, visited):
  queue = deque([start]) # 1. 탐색 시작 노드를 큐에 enque하며 큐 선언
  visited[start] = True # 탐색 처리를 한다.
  while queue:
    v = queue.popleft() # 2. 탐색한 노드를 큐에서 빼고
    for i in graph[v]:
      if not visited[i]: # 탐색 안한 인접 노드들을
        queue.append(i) # 큐에 넣으며
        visited[i] = True # 탐색 처리를 한다.

+ dfs는 재귀함수로 구현을 하기 떄문에 순서를 어떻게 하느냐에 따라 방법이 나뉠 수 있지만, bfs는 그냥 정해진 순서가 있다.


# 2178 미로 탐색 - 격자그래프, bfs의 탐색 경로 정의
# bfs에서 격자 그래프는 queue를 써야하기 때문에 (x, y)튜플로 queue에 넣고 빼고 하는 것. dfs도 stack을 써야됬다면 (x,y)로 해야됨

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] # 인접 노드 포인터를 얻기 위함.
dy = [0, 0, -1, 1]

def bfs(x, y): # bfs의 매개변수: 시작 노드 포인터 (x, y)
	queue = deque()
	queue.append((x, y)) # 큐 선언, 초깃값
	while queue:
		x, y = queue.popleft() # duque
		for i in range(4): # 현재 위치에서 네 방향 (인접노드)
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if graph[nx][ny] == 0:
				continue
			if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 최단거리 기록(이전 노드 거리기록+1).
				queue.append((nx, ny)) # 인접노드 넣으며
				graph[nx][ny] = graph[x][y] + 1 # 탐색처리(최단거리 기록) **따로 변수 설정하면 중복되서 값이 더 크게 나옴.
	return graph[n - 1][m - 1] # 최단거리 리턴.

print(bfs(0, 0))


# 1707 이분 그래프 - 그래프 탐색을 하면서, 인접노드와 다른 방문처리를 함으로 이분 그래프인지 판단한다.

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, group):
    queue = deque([start])  # 시작 정점 값을 큐에 담는다.
    visited[start] = group  # 시작 정점 그룹을 설정
    while queue:  # 큐가 존재할때까지 돈다.

        x = queue.popleft()  # 큐의 맨앞 원소를 빼낸다.

        for i in graph[x]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]:  # 만약 그 정점들을 아직 방문하지 않았다면
                queue.append(i)  # 그 정점들을 추가하고
                visited[i] = -1 * visited[x]  # 상위 정점과 다른 그룹으로 편성
            elif visited[i] == visited[x]:  # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
                return False  # False를 바로 리턴
    return True  # 위의 조건에 걸리지 않았다면 True를 리턴


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')


# 7576 토마토 - 격자그래프, bfs의 시작 노드 여러개 정의

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j]) # 시작노드 미리 넣어두고 밑에서 bfs 시작

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1) # -1이 있으면 0
            exit(0)
    res = max(res, max(i)) # max(visited)
print(res - 1)


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


# 1697 숨바꼭질 - bfs vs dp.. dp가 되려면 1.점화식 써짐 2.dp테이블전체를 채울만한 시간복잡도. 이 문제는 100000^2라서 불가능. 점화식이 써지지도 않음.
# 1차원 좌표에서 bfs. 좌표에서의 bf는 그래프 탐색을 할 수 있다는 걸 염두해야함.

from collections import deque

n, k = map(int, input().split())

graph = [0] * 100001

d = [-1, 1]

def bfs(start, end):
	queue = deque([start])
	graph[start] += 1
	while queue:
		v = queue.popleft()
		for i in range(2):
			nx = v + d[i]
			if nx < 0 or nx > 100000 or graph[nx] != 0: # 최초로 visited가 새겨진 값이 최솟값임. bfs 순서 상 덮어써지는 값은 무조건 최초값보다 크거나 같음.
				continue
			queue.append(nx)
			graph[nx] = graph[v] + 1
		nx = v * 2
		if nx >= 0 and nx <= 100000 and graph[nx] == 0:
			queue.append(nx)
			graph[nx] = graph[v] + 1
		if graph[k]:
			print(graph[k] - 1)
			break
bfs(n, k)


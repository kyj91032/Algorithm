# 넓이 우선 탐색(BFS): 가중치가 1인 그래프에서(모든간선의 가중치가 동일한 그래프에서), 탐색하지 않은 인접 노드를 우선으로 최대한 넓게 탐색하여 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 방법이다.
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
            queue.append([i, j]) # 시작노드 미리 넣어두고 밑에서 bfs 시작. 그러면 여러 시작점에서 번갈아가며 bfs함

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


# 1697 숨바꼭질 - bfs vs dp.. dp가 되려면 1.점화식 써짐 2.dp 테이블전체를 채울만한 시간복잡도. 이 문제는 100000^2라서 불가능. 점화식이 써지지도 않음.
'''
bfs VS dp에 대해서.
일단 둘 다 완전 탐색을 기반으로 하고 있고 바텀 업 방식으로 탐색해 나가는 것까지 유사한데
bfs는 visited를 이용해 노드의 탐색 여부를 기억하며 나아가고
dp는 dp테이블을 이용해 기억한 값을 점화식을 통해 나아간다는 점에서 차이가 존재한다.
그래서 문제마다 dp bfs 각자 유리한 방식이 있을거다. 둘 다 될 수도 있고, 하나만 될 수도 있고..
'''

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


# 13913 숨바꼭질4 - bfs에서의 경로 출력. 모든 노드가 자신의 이전 노드만 기억하면 됨

from collections import deque

n, k = map(int, input().split())

graph = [0] * 100001
move = [0] * 100001 # 이전 노드를 담는 배열.

d = [-1, 1]

def bfs(start, end):
	queue = deque([start])
	graph[start] += 1
	while queue:
		v = queue.popleft()
		for i in range(2):
			nx = v + d[i]
			if nx < 0 or nx > 100000 or graph[nx] != 0:
				continue
			queue.append(nx)
			graph[nx] = graph[v] + 1
			move[nx] = v
		nx = v * 2
		if nx >= 0 and nx <= 100000 and graph[nx] == 0:
			queue.append(nx)
			graph[nx] = graph[v] + 1
			move[nx] = v
		if graph[k]:
			print(graph[k] - 1)
			break
bfs(n, k)
'''
arr.append(k)
arr.append(move[k])
arr.append(move[move[k]])
tmp을 이용해 tmp = move[tmp]로 계속 재정의
'''
arr = []
tmp = k
for _ in range(graph[k]):
	arr.append(tmp)
	tmp = move[tmp]
arr.reverse()
print(' '.join(map(str, arr)))


# 14226 이모티콘 - 개수가 1000개면 2차원 가능성 높음. 처음에 [v][2]크기로 접근했다가 실패. 중복없이 횟수기록이 되게, (화면 이모티콘 개수, 클립보드 이모티콘 개수)를 리스트로.
# v*2는 특정 화면일때 클립값이 묶여있어서 모든 상태를 표현할 수 없음. 하지만 v*v는 특정화면일때 모든 클립값에 대해 횟수기록이 됨.

from collections import deque
n = int(input())
dist = [[-1] * (n + 1) for _ in range(n + 1)]
q = deque()
q.append((1, 0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수. 그리고 이 이차원 리스트에 방문처리를 하면서(횟수 기록) 탐색.
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if dist[s][s] == -1: # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1 # 클립보드에 복사
        q.append((s, s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1 # 
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]
print(answer)


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


# 16197 두 동전 - 방문처리가 필요 없음. 다시 돌아가는 탐색을 또 해도 count<10이라 시간복잡도 만족, 두개의 좌표에 대한 노드 (x1, y1, x2, y2)

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while queue:
        x1, y1, x2, y2, cnt = queue.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽이라면
                if board[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                queue.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())

    queue = deque()
    board = []
    temp = []
    for i in range(n):
        board.append(list(input().strip()))
        for j in range(m):
            if board[i][j] == "o":
                temp.append((i, j))

    queue.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

    print(bfs())

# 13460 구슬탈출2


N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]  # Board
dx = [-1, 1, 0, 0]  # x축 움직임
dy = [0, 0, -1, 1]  # y축 움직임
queue = []  # BFS : queue 활용
# Red(rx,ry)와 Blue(bx,by)의 탐사 여부 체크
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  # 초기화
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    pos_init()  # 시작 조건
    while queue:  # BFS : queue 기준
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if B[nbx][nby] != 'O':  # 실패 조건이 아니면
                if B[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()
'''

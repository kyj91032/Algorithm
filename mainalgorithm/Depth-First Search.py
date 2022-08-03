# 깊이 우선 탐색(DFS): 가중치가 1인 그래프에서, 탐색하지 않은 인접 노드를 우선으로 최대한 깊숙이 탐색하여 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 방법이다.
# 스택이 선입후출이라 깊이 우선 탐색이 가능한 것. dfs는 스택을 이용하는데 이게 재귀함수와 동작이 일치하기 때문에 그냥 스택의 선언 없이 재귀함수만 써도 된다. 
# 백트래킹과 동작이 일치한다. 방문했는지가 가지치기.

# DFS의 기본 동작 과정

1. 탐색 시작 노드를 매개변수로 받아 방문 처리를 한다.
2. 인접 노드를 차례로 돌며 탐색하지 않은 경우(인접 노드의 탐색 여부가 재귀 조건) 재귀 호출을 하고, 모두 탐색한 경우 함수를 종료한다.
(+ 인접 노드의 탐색 여부를 종료 조건으로 해서 재귀 호출을 하므로 탐색하지 않은 인접 노드에 대해서만 재귀 호출을 하기 때문에 호출량이 적다.)

1. 탐색 시작 노드를 매개변수로 받아
2. 탐색하지 않은 경우(현재 노드의 탐색 여부가 재귀 조건) 방문 처리 후 인접 노드를 차례로 돌며 재귀 호출을 하고, 탐색한 경우 함수를 종료한다.
(+ 현재 노드의 탐색 여부를 종료 조건으로 해서 재귀 호출을 하기 때문에, 매번 모든 인접 노드에 대하여 재귀 호출을 해야해서 호출량이 많아진다.)


# DFS

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
visited = [False] * 9

def dfs(graph, v, visited):
	visited[v] = True
  for i in graph[v]:
    if not visited[i]: # 인접 노드의 방문 여부가 재귀 조건: 방문 안한 인접 노드면 호출, 방문 한 인접노드면 호출X
      dfs(graph, i, visited)

def dfs(graph, v, visited):
	if not visited[v]: # 현재 노드의 방문 여부가 재귀 조건: 호출 시 방문 안한 노드면 방문처리, 방문 했으면 탈출
		visited[v] = True
		for i in graph[v]:
			dfs(graph, i, visited)


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


# 2667 단지번호붙이기 - dfs에서 깊이값 출력하기

n = int(input())

graph = []

for _ in range(n):
	graph.append(list(map(int, input())))
	# 간선 정보가 필요없는 그래프는 visited를 graph의 값으로 대신해서 쓴다.
num = []

def dfs(x, y):
	if x <= -1 or x >= n or y <= -1 or y >= n:
		return False
	if graph[x][y] == 1: # 시작 노드의 방문 여부로 dfs
		global count
		count += 1 # 스택이 다시 비었을때, count값이 유지되도록 해야함 그리고 다시 0으로 돌려주기
		graph[x][y] = 0
		dfs(x - 1, y)
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False

count = 0
result = 0
for i in range(n):
	for j in range(n): # 모든 노드를 확인하며 단지를 확인함. 아파트가 하나 발견되면 바로 단지를 정복하게됨.
		if dfs(i, j) == True:
			num.append(count) 
			count = 0 # (i, j) 에 대해 바로 count를 유지하면서 더해주며 단지를 정복하므로, 단지가 끝나면 dfs(i, j)가 종료되는데, 종료되면 count = 0으로 돌려주면 됨.
			result += 1
			
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])



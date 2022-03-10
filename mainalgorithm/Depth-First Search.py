# 깊이 우선 탐색(DFS): 가중치가 1인 그래프에서, 탐색하지 않은 인접 노드를 우선으로 최대한 깊숙이 탐색하여 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 방법이다.

# DFS의 기본 동작 과정
'''
1. 탐색 시작 노드를 매개변수로 받아 방문 처리를 한다.
2. 인접 노드를 차례로 돌며 탐색하지 않은 경우(인접 노드의 탐색 여부가 재귀 조건) 재귀 호출을 하고, 모두 탐색한 경우 함수를 종료한다.
+ 인접 노드의 탐색 여부를 종료 조건으로 해서 재귀 호출을 하므로 탐색하지 않은 인접 노드에 대해서만 재귀 호출을 하기 때문에 호출량이 적다.

1. 탐색 시작 노드를 매개변수로 받아
2. 탐색하지 않은 경우(현재 노드의 탐색 여부가 재귀 조건) 방문 처리 후 인접 노드를 차례로 돌며 재귀 호출을 하고, 탐색한 경우 함수를 종료한다.
+ 현재 노드의 탐색 여부를 종료 조건으로 해서 재귀 호출을 하기 때문에, 매번 모든 인접 노드에 대하여 재귀 호출을 해야해서 호출량이 많아진다.
'''

''' DFS

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
    if not visited[i]: # 인접 노드의 방문 여부가 재귀 조건: 방문 안 했으면 재귀 호출, 방문 다 했으면 함수 종료.
      dfs(graph, i, visited)

def dfs(graph, v, visited):
	if not visited[v]: # 현재 노드의 방문 여부가 재귀 조건: 방문 안 했으면 재귀 호출, 방문 다 했으면 함수 종료.
		visited[v] = True
		for i in graph[v]:
			dfs(graph, i, visited)
'''


''' 음료수 얼려 먹기

N, M = map(int, input().split())

graph = []
for i in range(N):
	graph.append(list(map(int, input()))) # **map은 iteralbe의 요소마다 지정된 함수를 적용시켜준다. list(string)은 각 문자가 요소가 되는 리스트로 변환된다.

def dfs(x, y):
	if x <= -1 or x >= n or y <= -1 or y >= m: # 종료 조건 1
		return False

	if graph[x][y] == 0: # 현재 노드의 방문 여부가 재귀(종료) 조건 2: 방문 안 했으면 재귀 호출, 방문 했으면 함수 종료.
		graph[x][y] = 1
		dfs(x - 1, y)
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False

result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True: # 한 얼음 노드가 노드 포인터가 됬을 때, 그 얼음 덩어리를 틀 처리 해버려서 중복 없이 얼음 모양의 개수를 셀 수 있다.
			result += 1
print(result)
'''


''' n과 m (1)

n, m = list(map(int, input().split()))
 
s = [] # 재귀 조건을 설정하는 과정에서 스택이 필요해서 정의.

def rec(): # BF, 반복 안되서 재귀로 접근.
    if len(s) == m: # 재귀 조건 1. (m의 값 조건 고려)
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i not in s: # i가 s에 없으면, 재귀 조건 2. (중복 안되는 조건 고려) 
            s.append(i) # push
            rec() # 재귀 호출
            s.pop() # 종료 호출 시 pop하고 다음 i로 반복을 통해 가지치기 구현
rec()
'''

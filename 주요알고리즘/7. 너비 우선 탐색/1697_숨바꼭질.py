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

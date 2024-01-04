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
